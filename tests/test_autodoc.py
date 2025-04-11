# -*- coding: utf-8 -*-
"""
test_fortran_autodoc
====================

Test the fortran_autodoc extension.

Adapted from sphinx/tests/test_autodoc.py.
"""
import pickle
import os
import warnings
import difflib

import pytest

this_dir = os.path.dirname(__file__)


def checkdir(path):
    pdir = os.path.dirname(path)
    if not os.path.exists(pdir):
        os.makedirs(pdir)


def check_result(test_name, result):
    xml_result = result[0].pformat()

    ref_file = os.path.join(this_dir,
                            'references',
                            'test-fortran-autodoc',
                            test_name + '.xml')
    out_file = os.path.join(this_dir,
                            'outputs',
                            'test-fortran-autodoc',
                            test_name + '.xml')
    if not os.path.exists(ref_file):
        warnings.warn('Creating missing reference file: ' + ref_file)
        checkdir(ref_file)
        with open(ref_file, 'w') as f:
            f.write(xml_result)
    else:
        checkdir(out_file)
        with open(out_file, 'w') as f:
            f.write(xml_result)
        with open(ref_file) as f:
            xml_ref = f.read()
        xml_result = xml_result.replace("u'", "'")
        equal = xml_ref == xml_result
        assert equal, (
                'Invalid xml result. \n' +
                'Reference file: {}\n'.format(ref_file) +
                'Actual output: {}\n'.format(out_file) +
                'Differences:\n' +
                '\n'.join(difflib.context_diff(xml_ref.split('\n'),
                                               xml_result.split('\n'))))


@pytest.mark.sphinx('dummy', testroot='fortran-autodoc')
def test_autodoc_module_assim(app, status, warning):
    app.builder.build_all()
    result = pickle.loads((app.doctreedir / 'module_assim.doctree').read_bytes())
    check_result('module_assim', result)


#    utl_matsqrt = module_assim[0][2]
#    utl_matsqrt_sig, utl_matsqrt_desc = utl_matsqrt
#    utl_matsqrt_desc_header, utl_matsqrt_desc_params = utl_matsqrt_desc
#    assert utl_matsqrt_sig[0].astext().strip() == 'subroutine'
#    assert utl_matsqrt_sig[1].astext().strip() == 'utl_matsqrt'
#    assert utl_matsqrt_desc_header.astext().strip() == 'Calculate square root of an error covariance matrix'
#    assert utl_matsqrt_desc_params[0].astext() == 'Parameters\n\npa (kn,kn) [real,inout] :: on entry, the original matrix; on exit, the sqrt matrix\n\nzsign [real,in] :: sign of the exponent'
#    assert utl_matsqrt_desc_params[1].astext() == 'Options\n\nkn [integer,in,optional/default=shape(pa,0)] :: order of the matrix\n\nprintinformation_opt [logical,in,optional] :: request more verbose output'


@pytest.mark.sphinx('dummy', testroot='fortran-autodoc')
def test_autodoc_module_generic(app, status, warning):
    app.builder.build_all()
    result = pickle.loads((app.doctreedir / 'module_generic.doctree').read_bytes())
    check_result('module_generic', result)


@pytest.mark.sphinx('dummy', testroot='fortran-autodoc')
def test_autodoc_misc_routines(app, status, warning):
    app.builder.build_all()
    result = pickle.loads((app.doctreedir / 'misc_routines.doctree').read_bytes())
    check_result('misc_routines', result)
