"""Test package import."""

import sys

from pygopher import interfaces


if sys.version_info < (3, 8):
    from importlib_metadata import version
else:
    from importlib.metadata import version


def test_version():
    """Test access to the package version."""
    assert interfaces.__version__ == version("pygopher-interfaces")
