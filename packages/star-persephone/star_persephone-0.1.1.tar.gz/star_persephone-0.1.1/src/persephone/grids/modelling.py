import numpy as np
import persephone
import warnings
import pygyre as pg

"""
A set of functions dedicated to perform
stellar modelling on a MESA grid. 
"""

def check_observables (history, observable_names) :
  """
  Check that observable names are available
  in the history data file. 

  Parameters
  ----------
  history : dict
    History dictionary loaded through the 
    ``get_history_data`` function.

  observable_names : array-like
    List of observables to check.
  """
  for obs_n in observable_names :
    for keys, h_dict in history.items () :
      if not obs_n in h_dict.bulk_names :
        raise Exception ("{} is missing from {} model".format (obs_n, keys))

def chi_square_one_set (h_dict, observables,
                        observable_names, err_observables=None) :
  '''
  Compute chi-square with observables for one set
  of stellar parameters listed in a dictionary.
  It assumes that all the observables actually
  exist in the dictionary.

  Parameters
  ----------
  h_dict : MesaData
    ``MesaData`` object with the elements loaded from the history 
    data file.

  observables : array-like
    Observable to use to compute chi square.

  observable_names : array-like or List
    The corresponding list of observable names.

  err_observables : array-like
    Uncertainties to consider for the observable set.
    If no uncertainties are provided, ``1`` will be set
    for every parameter (not recommended).
    Optional, default ``None``.

  Returns
  -------
  ndarray
    The computed chi-square array.
  '''
  if err_observables is None :
    err_observables = 1
  else :
    err_observables = np.array (err_observables)
  param = np.array ([h_dict.bulk_data[obs_name] for obs_name in observable_names]).T
  chi_square = np.sum ((param - observables)**2 / err_observables**2, axis=1) 
  return chi_square
  
def chi_square_identifier (model, h_dict) :
  '''
  Make identifier so each chi-square computed values
  is easily traceable.
  '''
  return (np.full (h_dict.model_number.size, model), 
          h_dict.model_number)
 
def compute_chi_square_grid (history, observables, 
                             observable_names, 
                             err_observables=None) :
  '''
  Compute chi-square with observables for all set
  of stellar parameters listed a dictionary 
  (created through the ``get_history_data`` function) 
  from ``history.data`` files of the whole grid.
  '''
  observables = np.array (observables)
  check_observables (history, observable_names)
  model_id, model_number, chi_square = [], [], []
  for model, h_dict in history.items () :
    _id, _number = chi_square_identifier (model, h_dict)
    _chi_sq = chi_square_one_set (h_dict, observables,
                                     observable_names, 
                                     err_observables=err_observables)
    model_id.append (_id)
    model_number.append (_number)
    chi_square.append (_chi_sq)
  model_id = np.concatenate (model_id)
  model_number = np.concatenate (model_number)
  chi_square = np.concatenate (chi_square)
  return model_id, model_number, chi_square
    
def get_mode_frequencies (filename) :
  """
  Get mode order, degrees, azimuthal number and 
  frequencies from a GYRE summary file. 

  Returns 
  -------
  ndarray
    An array of four columns with, in this order,
    order ``n``, degree ``ell``, azimuthal number
    ``m`` and frequency ``nu`` of the mode. 
  """
  s = pg.read_output (filename) 
  if "m" in s.colnames :
    modes = np.c_[s["n_pg"].data, s["l"].data, 
                  s["m"].data, s["freq"].data.real]
    return modes
  else :
    warnings.warn ("No azimuthal numbers found, assuming m=0.")
    modes = np.c_[s["n_pg"].data, s["l"].data, 
                  np.zeros (len (s)), s["freq"].data.real]
    return modes

def select_modes (model_modes, obs_order, obs_degree) :
  """
  Select the model modes to have an array fitting
  input observed list of modes.
  """
  model_n_l = np.copy (model_modes[:,[0,1]])
  # Using np.ascontiguous array to avoid raising a ValueError
  _, _, indices = intersect2d (np.c_[obs_order, obs_degree],
                               np.ascontiguousarray (model_n_l))
  return model_modes[indices,:]

def intersect2d (a, b) :
  """
  Intersect row-wise numpy arrays
  """
  nrows, ncols = a.shape
  dtype={'names':['f{}'.format(i) for i in range(ncols)],
         'formats':ncols * [a.dtype]}

  c, ind_a, ind_b = np.intersect1d (a.view(dtype), b.view(dtype),
                                    return_indices=True)
  c = c.view(a.dtype).reshape(-1, ncols)
  return c, ind_a, ind_b
