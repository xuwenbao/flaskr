# -*- coding: utf-8 -*-
"""
    Flaskr Tests
    ~~~~~~~~~~~~

    Tests the Flaskr application.

    :copyright: © 2010 by the Pallets team.
    :license: BSD, see LICENSE for more details.
"""

from setuptools import setup, find_packages

setup(
    name='flaskr',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'flask',
    ],
    setup_requires=[
        'pytest-runner',
    ],
    tests_require=[
        'pytest',
    ],
)
