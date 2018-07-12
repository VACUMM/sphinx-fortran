# -*- coding: utf-8 -*-
"""
test_fortran_autodoc
====================

Test the fortran_autodoc extension.

Adapted from sphinx/tests/test_autodoc.py.
"""
from __future__ import print_function

import pickle

import pytest

from sphinx import addnodes

#def print_node(label, node):
#    print(label, len(node), repr(node.astext()))

@pytest.mark.sphinx('dummy', testroot='fortran-autodoc')
def test_autodoc_module_assim(app, status, warning):
    app.builder.build_all()

    module_assim = pickle.loads((app.doctreedir / 'module_assim.doctree').bytes())
    utl_matsqrt = module_assim[0][2]
    utl_matsqrt_sig, utl_matsqrt_desc = utl_matsqrt
    utl_matsqrt_desc_header, utl_matsqrt_desc_params = utl_matsqrt_desc
    assert utl_matsqrt_sig[0].astext().strip() == 'subroutine'
    assert utl_matsqrt_sig[1].astext().strip() == 'utl_matsqrt'
    assert utl_matsqrt_desc_header.astext().strip() == 'Calculate square root of an error covariance matrix'
    assert utl_matsqrt_desc_params[0].astext() == 'Parameters\n\npa (kn,kn) [real,inout] :: on entry, the original matrix; on exit, the sqrt matrix\n\nzsign [real,in] :: sign of the exponent'
    assert utl_matsqrt_desc_params[1].astext() == 'Options\n\nkn [integer,in,optional/default=shape(pa,0)] :: order of the matrix\n\nprintinformation_opt [logical,in,optional] :: request more verbose output'
