# 2D Colormap 

`matplotlib` provides [many colormaps](https://matplotlib.org/stable/users/explain/colors/colormaps.html) that map scalars to colors. However, it does not provide such colormaps for 2D vectors. Representing 2D vectors as colors may be helpful when dealing with complex numbers or 2D coordinates. This library provides 2 colormaps for this purpose including a cyclic one.

<p align="center">
    <img src="https://raw.githubusercontent.com/mthiboust/colormap2d/main/docs/pinwheel_colormap.png" width="350">
    <img src="https://raw.githubusercontent.com/mthiboust/colormap2d/main/docs/cyclic_pinwheel_colormap.png" width="350">
</p>

## Installation

```shell
pip install colormap2d
```

## Usage 

```python
import numpy as np
import colormap2d

some_2d_vectors = np.random.rand(5, 2) 

# Random 2D vectors between 0 and 1:
# array([[0.91270668, 0.60020465],
#        [0.51569033, 0.79642031],
#        [0.36533928, 0.31441287],
#        [0.41346207, 0.45163162],
#        [0.99135696, 0.05691322]])

colormap2d.pinwheel(some_2d_vectors)

# RGBA float values between 0 and 1 (default)
# array([[0.69019608, 0.6627451 , 0.24705882, 1.        ],
#        [0.25490196, 0.74509804, 0.82352941, 1.        ],
#        [0.41960784, 0.2       , 0.79215686, 1.        ],
#        [0.18823529, 0.29803922, 0.20392157, 1.        ],
#        [0.24705882, 0.24705882, 0.66666667, 1.        ]])

colormap2d.pinwheel(some_2d_vectors, mode="RGB", dtype=np.uint8)
# RGB integers between 0 and 255:
# array([[166, 179,  50],
#        [ 50,  66,  94],
#        [ 63,  98, 212],
#        [ 66,  66, 196],
#        [222, 199, 169]], dtype=uint8)

```

## Behind the scene

The colormap data has been created using Self-Organizing Maps. 


