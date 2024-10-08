"""Sphinx configuration."""
project = "{{cookiecutter.friendly_name}}"
author = "{{cookiecutter.author}}"
copyright = "{{cookiecutter.copyright_year}}, {{cookiecutter.author}}"
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx_click",
    "myst_parser",
    "sphinx_markdown_builder",
]
autodoc_typehints = "description"
html_theme = "furo"
