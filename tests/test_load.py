"""Test package import."""

from importlib_metadata import version

from pygopher import interfaces


def test_version():
    """Test access to the package version."""
    assert interfaces.__version__ == version("pygopher-interfaces")
