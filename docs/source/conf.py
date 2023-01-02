# pylint: disable=invalid-name
"""Sphinx configuration."""
import typing as tp

from importlib import metadata


project = "pygopher-interfaces"
author = "Mark Rogaski"
copyright = f"2023, {author}"  # pylint: disable=redefined-builtin

release = metadata.version("pygopher-interfaces")
version = release.rsplit(".", 1)[0]
if "dev" in release:
    release = version = "UNRELEASED"

extensions = ["sphinx.ext.autodoc", "sphinx.ext.doctest"]
templates_path = ["_templates"]
exclude_patterns: tp.List[str] = []
html_theme = "sphinx_rtd_theme"
html_static_path = []

default_role = "any"
add_function_parentheses = True
autodoc_typehints = "description"
autodoc_typehints_description_target = "documented"
