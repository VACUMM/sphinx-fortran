# -*- coding: utf-8 -*-
# Inits
from setuptools import setup, find_packages
import sys
import os

# Version, etc
sys.path.insert(0, 'sphinxfortran')
from  sphinxfortran import ( __version__ as version, __author__ as author,
    __email__ as author_email)
del sys.path[0]

# From files
base = os.path.dirname(__file__)
with open(os.path.join(base, 'README.rst')) as f:
    long_description = f.read()
with open(os.path.join(base, 'requirements.txt')) as f:
    requires = filter(None, f.read().split('\n'))


# Other infos
description = 'Fortran domain and autodoc extensions to Sphinx'
maintainer = author
maintainer_email = author_email
license = "CeCiLL-A"
url = "http://sphinx-fortran.readthedocs.org"
classifiers = [
        "License :: OSI Approved :: CEA CNRS Inria Logiciel Libre License, version 2.1 (CeCILL-2.1)",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        ]


if __name__ == '__main__':

    # Lauch setup
    setup(name='sphinx-fortran',
        version=version,
        description=description,
        long_description=long_description,
        author=author,
        author_email=author_email,
        maintainer=author,
        maintainer_email=author_email,
        license=license,
        url=url,
        classifiers=classifiers,
        packages=find_packages(),
        install_requires=requires,
    )



