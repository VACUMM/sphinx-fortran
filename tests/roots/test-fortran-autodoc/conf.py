# -*- coding: utf-8 -*-

import sys
import os
this_dir = os.path.dirname(__file__)
src_dir = os.path.abspath(os.path.join(this_dir, '..', '..', '..'))
sys.path.insert(0, src_dir)
import sphinxfortran

extensions = ['sphinxfortran.fortran_domain',
              'sphinxfortran.fortran_autodoc']
import sphinxfortran.fortran_autodoc
print sphinxfortran.fortran_autodoc

master_doc = 'index'
html_theme = 'classic'
exclude_patterns = ['_build']

# Fortran autodoc
fortran_src = [os.path.abspath(os.path.join(this_dir, 'module_assim.f90'))]
print fortran_src


