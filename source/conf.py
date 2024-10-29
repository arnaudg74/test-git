import os
import sys
sys.path.insert(0, os.path.abspath('../Python'))  


project = 'MyPython'
copyright = '2024, Moi'
author = 'Moi'
release = '001'

extensions = ['sphinx.ext.autodoc']

templates_path = ['_templates']
exclude_patterns = []


html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']


source_suffix = {
    '.rst': 'restructuredtext',
    '.txt': 'markdown',
    '.md': 'markdown',
}