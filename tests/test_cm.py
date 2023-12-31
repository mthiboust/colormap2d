"""Tests for the main colormap2d functions."""

import colormap2d
import numpy as np
import pytest


def test_pinwheel_values():
    """Checks if colormap2d is outputing the expected values."""
    v = np.array([[0.91270668, 0.60020465], [0.51569033, 0.79642031]])

    rgb = colormap2d.pinwheel(v, mode="RGB", dtype=np.uint8)
    np.testing.assert_allclose(
        rgb, np.array([[166, 179, 50], [50, 66, 94]], dtype=np.uint8)
    )

    rgba = colormap2d.pinwheel(v, mode="RGBA", dtype=np.uint8)
    np.testing.assert_allclose(
        rgba, np.array([[166, 179, 50, 255], [50, 66, 94, 255]], dtype=np.uint8)
    )

    rgb = colormap2d.pinwheel(v, mode="RGB", dtype=np.float64)
    np.testing.assert_allclose(
        rgb,
        np.array(
            [
                [0.65098039, 0.70196078, 0.19607843],
                [0.19607843, 0.25882353, 0.36862745],
            ],
            dtype=np.float64,
        ),
    )

    rgba = colormap2d.pinwheel(v, mode="RGBA", dtype=np.float64)
    np.testing.assert_allclose(
        rgba,
        np.array(
            [
                [0.65098039, 0.70196078, 0.19607843, 1.0],
                [0.19607843, 0.25882353, 0.36862745, 1.0],
            ],
            dtype=np.float64,
        ),
    )


def test_pinwheel_multidim():
    """Checks if any shape is any provided the last dimension is 2."""
    v = np.random.rand(5, 5, 5, 2)

    rgba = colormap2d.pinwheel(v)
    assert rgba.shape == v.shape[:-1] + (4,)

    rgba = colormap2d.pinwheel(v, mode="RGBA")
    assert rgba.shape == v.shape[:-1] + (4,)

    rgb = colormap2d.pinwheel(v, mode="RGB")
    assert rgb.shape == v.shape[:-1] + (3,)


def test_pinwheel_errors():
    """Checks if exceptions."""
    with pytest.raises(TypeError) as excinfo:
        colormap2d.pinwheel([0.5, 0.5])

    assert excinfo.type == TypeError

    with pytest.raises(ValueError) as excinfo:
        colormap2d.pinwheel(np.random.rand(5, 3))

    assert excinfo.type == ValueError

    with pytest.raises(ValueError) as excinfo:
        colormap2d.pinwheel(np.array([1.91270668, -0.60020465]))

    assert excinfo.type == ValueError
