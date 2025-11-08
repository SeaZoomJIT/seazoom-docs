# Configuration file for Sphinx documentation builder.
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import os
import sys
from pathlib import Path

# Add source path
sys.path.insert(0, os.path.abspath('../src'))

# -- Project information -------------------------------------------------------
project = 'SeaZoom AI Suite'
author = 'Dr. Antiope Politi'
copyright = '2025, SeaZoom AI'
release = 'v2.1.1e'
version = '2.1.1e'

# -- General configuration -------------------------------------------------------
extensions = [
    'myst_parser',
    'sphinx_rtd_theme',
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- MyST Parser Configuration --------------------------------------------------
myst_enable_extensions = [
    "deflist",
    "colon_fence",
    "html_image",
    "html_admonition",
]

# -- HTML output configuration --------------------------------------------------
html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
html_title = "SeaZoom AI Suite Documentation"

# Logo and favicon (optional - will be added later)
# html_logo = '_static/seazoom_logo.png'
# html_favicon = '_static/favicon.ico'

# RTD Theme options
html_theme_options = {
    'collapse_navigation': False,
    'sticky_navigation': True,
    'navigation_depth': 3,
    'style_nav_header_background': '#002B45',
    'logo_only': False,
    'prev_next_buttons_location': 'bottom',
    'style_external_links': True,
}

# GitHub integration
html_context = {
    "display_github": True,
    "github_user": "SeaZoomJIT",
    "github_repo": "seazoom-voyage-optimizer",
    "github_version": "main",
    "conf_py_path": "/docs/",
}

# -- Options for HTML output
html_use_smartquotes = True
html_show_sourcelink = False
html_show_sphinx = False
html_show_copyright = True

# -- Sphinx configuration
master_doc = 'index'
language = 'en'

