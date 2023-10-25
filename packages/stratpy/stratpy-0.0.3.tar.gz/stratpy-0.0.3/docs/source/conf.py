# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'stratpy'
copyright = '2023, Fredrik Ofstad'
author = 'Fredrik Ofstad'

release = '0.1'
version = '0.1.0'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'myst_parser',
    'sphinx_copybutton'
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

myst_enable_extensions = [
    "colon_fence",
    "deflist",
]
myst_heading_anchors = 3

# -- Options for HTML output

html_static_path = ["_static"]
html_theme = "furo"
html_theme_options = {
    "light_logo": "light.png",
    "dark_logo": "dark.png",
    "sidebar_hide_name": True,
}

# -- Options for EPUB output
epub_show_urls = 'footnote'
