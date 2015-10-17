# -*- coding: utf-8 -*-

u"""
.. module:: setup
"""

import os
from setuptools import setup


REPO_ROOT = os.path.dirname(__file__)


with open(os.path.join(REPO_ROOT, 'README.md')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='plantingjs.org',
    version='alpha',
    packages=['src'],
    include_package_data=True,
    license='MIT License',
    description='Simple Flask app which is running on http://plantingjs.org.',
    long_description=README,
    test_suite='tests',
    url='http://plantingjs.org/',
    author='Tomasz Magulski',
    author_email='tomasz.magulski@gmail.com',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Flask',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
