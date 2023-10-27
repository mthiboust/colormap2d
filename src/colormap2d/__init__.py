"""2D colormap.

`matplotlib` provides many colormaps that map scalars to colors. 
However, it does not provide such colormaps for 2D vectors. 
Representing 2D vectors as colors may be helpful when dealing with 
complex numbers or 2D coordinates. This library provides 2 colormaps 
for this purpose.
"""

from .cm import cyclic_pinwheel, pinwheel


__all__ = ["pinwheel", "cyclic_pinwheel"]
