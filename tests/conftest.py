# -*- coding: utf-8 -*-
"""pytest config
================

Adapted from sphinx/tests/conftest.py.
"""
from __future__ import print_function
import os
import shutil
import sys

import pytest

from sphinx.testing.path import path

pytest_plugins = 'sphinx.testing.fixtures'

# Exclude 'roots' dirs for pytest test collector
collect_ignore = ['roots']

## Disable Python version-specific
#if sys.version_info < (3,):
#    collect_ignore += ['py3']
#
#if sys.version_info < (3, 5):
#    collect_ignore += ['py35']


@pytest.fixture(scope='session')
def rootdir():
    return path(os.path.dirname(__file__) or '.').abspath() / 'roots'


def pytest_report_header(config):
    return 'Running Sphinx test suite (with Python %s)...' % (
        sys.version.split()[0])


def _initialize_test_directory(session):
    testroot = os.path.join(str(session.config.rootdir), 'tests')
    tempdir = os.path.abspath(os.getenv('SPHINX_TEST_TEMPDIR',
                              os.path.join(testroot, 'build')))
    os.environ['SPHINX_TEST_TEMPDIR'] = tempdir

    print('Temporary files will be placed in %s.' % tempdir)

    if os.path.exists(tempdir):
        shutil.rmtree(tempdir)

    os.makedirs(tempdir)


def pytest_sessionstart(session):
    _initialize_test_directory(session)
