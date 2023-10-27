"""Tests for the main colormap2d functions."""

import colormap2d
import numpy as np
import pytest


def test_pinwheel_values():
    """Checks if colormap2d is outputing the expected values."""
    v = np.array([[0.91270668, 0.60020465], [0.51569033, 0.79642031]])
    rgb = colormap2d.pinwheel(v)

    np.testing.assert_allclose(
        rgb, np.array([[166, 179, 50], [50, 66, 94]], dtype=np.uint8)
    )


def test_pinwheel_multidim():
    """Checks if any shape is any provided the last dimension is 2."""
    v = np.random.rand(5, 5, 5, 2)
    rgb = colormap2d.pinwheel(v)

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
