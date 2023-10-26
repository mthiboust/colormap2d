from importlib import resources

import numpy as np
    
N = 50 # number of samples inside the colormap data

def _load_npy(relative_path):
    
    with resources.path(__package__ + '.data', relative_path) as path:
        return np.load(path)

def _apply_colormap(arr, colormap):

    if not isinstance(arr, np.ndarray):
        raise TypeError(f"Parameter must be a numpy array, not {type(arr)}")
    if arr.shape[-1] != 2:
        raise ValueError(f"Last dimension of array shape {arr.shape} must be 2.")

    arr = np.round(arr * N).astype(np.int32)
    colormap_data = _load_npy(colormap + '.npy')
    return colormap_data[arr[...,0], arr[...,1]]

def pinwheel(arr):
    """Converts 2D coordinates into 3D RGB values.
    
    Args:
        arr: Numpy array whose last dimension is 2 and whose values belong to [0,1]
    """

    return _apply_colormap(arr, 'pinwheel')


def cyclic_pinwheel(arr):
    """Converts 2D coordinates into 3D RGB values which are the same at each XY border.
    
    Args:
        arr: Numpy array whose last dimension is 2 and whose values belong to [0,1]
    """

    return _apply_colormap(arr, 'cyclic_pinwheel')

