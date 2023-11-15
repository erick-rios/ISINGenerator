# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
sys.path.insert(0, os.path.abspath('..'))

from isingenerator import __about__

# -- Project information -----------------------------------------------------

project = __about__.__title__
copyright = __about__.__copyright__
author = __about__.__author__

# The full version, including alpha/beta/rc tags
release = __about__.__version__

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'recommonmark',
    'sphinx.ext.autodoc',
    'sphinx.ext.intersphinx',
    'sphinx.ext.doctest',
    'sphinx.ext.autosectionlabel',
    'sphinx.ext.viewcode',
    'sphinx.ext.todo',
]

templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build']

autoclass_content = 'both'
autodoc_member_order = 'groupwise'

todo_include_todos = True

source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
    '.txt': 'markdown'
}

intersphinx_mapping = {
    'python': ('https://docs.python.org/3', None),
    'hypothesis': ('https://hypothesis.readthedocs.io/en/latest', None)
    # 'pathlib': ('https://docs.python.org/3/library/pathlib.html', None)
}


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.

html_theme = 'alabaster'

html_theme_options = {
    'show_powered_by': False,
    'github_user': 'erick-rios',
    'github_repo': 'ISINGenerator',
    'github_banner': True,
    'show_related': False,
    'note_bg': '#FFF59C',
    'github_button': True,
    'github_type': 'star',
    'description': __about__.__summary__,
    #'extra_nav_links': {'ISINGenerator @ PyPI': ''},
    'analytics_id': 'UA-109078714-2',
}

html_static_path = ['_static']
