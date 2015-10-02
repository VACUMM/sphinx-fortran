Purpose
-------

This package provides two Sphinx (http://www.http://sphinx.pocoo.org/) extensions 
to the Fortran (90) language:

- ``sphinxfortran.fortran_domain``: Sphinx domain for fortran.
- ``sphinxfortran.fortran_autodoc``: Auto-documenting fortran code.

License
-------

This package has the same license as VACUMM (http://www.ifremer.fr/vacumm) 
from which it originates: CeciLL-A (http://www.cecill.info/licences/Licence_CeCILL_V2.1-en.html),
which is compatible with the GPL.

Prerequisites
-------------

The ``sphinx`` and ``numpy`` packages.

Installation
------------

Using ``pip``::

    pip install sphinxfortran

From sources::

    python setup.py install

Quick start
-----------

1. Add this extension to you sphinx ``conf.py``.
2. List you fortran source files in the variable
   ``fortran_src`` of your ``conf.py``.
3. Generate their documentation in rst files using
   directives like::
   
       .. f:automodule:: mymodule

Documentation
-------------

Website:

