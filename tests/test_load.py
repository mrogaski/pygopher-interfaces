"""Test package import."""

from pygopher import interfaces


def test_version():
    """Test access to the package version."""
    assert interfaces.__version__
