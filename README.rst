Sphinx-Fortran extensions
=========================

.. image:: https://badge.fury.io/py/sphinx-fortran.svg
    :target: https://badge.fury.io/py/sphinx-fortran

.. image:: https://travis-ci.org/VACUMM/sphinx-fortran.svg?branch=master
    :target: https://travis-ci.org/VACUMM/sphinx-fortran

.. image:: https://readthedocs.org/projects/sphinx-fortran/badge/?version=latest
    :target: http://sphinx-fortran.readthedocs.org/en/latest/?badge=latest


Purpose
-------

This package provides two Sphinx (http://sphinx.pocoo.org/) extensions
to the Fortran (90) language:

- ``sphinxfortran.fortran_domain``: Sphinx domain for fortran.
- ``sphinxfortran.fortran_autodoc``: Auto-documenting fortran code.


License
-------

This package has the same license as VACUMM (http://www.ifremer.fr/vacumm)
from which it originates: CeciLL-A
(http://www.cecill.info/licences/Licence_CeCILL_V2.1-en.html),
which is compatible with the GPL.


Prerequisites
-------------

The ``sphinx`` and ``numpy`` packages.


Installation
------------

With ``pip``::

    pip install sphinx-fortran


With ``conda``::

    conda install -c vacumm -c conda-forge sphinx-fortran

From sources::

    git clone https://github.com/VACUMM/sphinx-fortran.git
    cd sphinx-fortran
    python setup.py install


Quick start
-----------

1. Add this extension to your sphinx ``conf.py``.
2. List you fortran source files in the variable
   ``fortran_src`` of your ``conf.py``.
3. Generate their documentation in rst files using
   directives like::

       .. f:automodule:: mymodule


Bugs and requests
-----------------

Please go to this GitHub page:
https://github.com/VACUMM/sphinx-fortran/issues


Authors
-------

Stephane Raynaud (stephane.raynaud(at)gmail.com)

Thanks: Thomas Gastine and other pull request contributors.


Documentation
-------------

Website: http://sphinx-fortran.readthedocs.org

