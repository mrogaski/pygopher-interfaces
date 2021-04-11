# pylint: disable=invalid-name
"""Sphinx configuration."""
from typing import List

project = "pygopher-interfaces"
copyright = "2021, Mark Rogaski"  # pylint: disable=redefined-builtin
author = "Mark Rogaski"

extensions = ["sphinx.ext.autodoc"]
templates_path = ["_templates"]
exclude_patterns: List[str] = []
html_theme = "sphinx_rtd_theme"
html_static_path = ["_static"]
