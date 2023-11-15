"""2D colormap.

`matplotlib` provides many colormaps that map scalars to colors. 
However, it does not provide such colormaps for 2D vectors. 
Representing 2D vectors as colors may be helpful when dealing with 
complex numbers or 2D coordinates. This library provides 2 colormaps 
for this purpose.
"""

from importlib import resources

import numpy as np


N = 50  # number of samples inside the colormap data


def _load_npy(relative_path):
    with resources.path(__package__ + ".data", relative_path) as path:
        return np.load(path)


def _apply_colormap(arr, colormap, mode="RGBA", dtype=np.float64):
    if not isinstance(arr, np.ndarray):
        raise TypeError(f"Parameter must be a numpy array, not {type(arr)}")
    if arr.shape[-1] != 2:
        raise ValueError(f"Last dimension of array shape {arr.shape} must be 2.")
    if np.min(arr) < 0 or np.max(arr) > 1:
        raise ValueError("Array values must be in the range [0:1].")
    if mode not in ["RGB", "RGBA"]:
        raise ValueError(f"Mode must be either 'RGB' or 'RGBA', not '{mode}'.")
    if dtype not in [np.float64, np.uint8]:
        raise ValueError(
            f"Dtype must be either 'np.float64' for float values between 0 and 1, "
            f"or 'np.uint8' for integer between 0 and 255, not '{dtype}'."
        )

    arr = np.round(arr * N).astype(np.int32)
    colormap_data = _load_npy(colormap + ".npy")
    out = colormap_data[arr[..., 0], arr[..., 1]]

    # Add an alpha channel filled with ones
    if mode == "RGBA":
        alpha = np.ones(arr.shape[:-1] + (1,), dtype=np.uint8) * 255
        out = np.concatenate((out, alpha), axis=-1)

    # Convert back the values in the [0:1] range like `matplotlib.cm`` functions
    if dtype == np.float64:
        out = out / 255

    return out


def pinwheel(arr, **kwargs):
    """Converts 2D coordinates into 3D RGB values.

    Args:
        arr: Numpy array whose last dimension is 2 and whose values belong to [0,1].
        **kwargs:
            mode: 'RGB' or 'RGBA'. Default to 'RGBA'.
            dtype: np.uint8 or np.float64. Default to np.float64.
    """
    return _apply_colormap(arr, "pinwheel", **kwargs)


def cyclic_pinwheel(arr, **kwargs):
    """Converts 2D coordinates into 3D RGB values which are the same at each XY border.

    Args:
        arr: Numpy array whose last dimension is 2 and whose values belong to [0,1].
        **kwargs:
            mode: 'RGB' or 'RGBA'. Default to 'RGBA'.
            dtype: np.uint8 or np.float64. Default to np.float64.
    """
    return _apply_colormap(arr, "cyclic_pinwheel", **kwargs)
