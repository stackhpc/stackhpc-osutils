#!/usr/bin/env python
import os.path

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

long_description = ""
with open('README.md') as f:
    long_description = f.read()
with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name='osutils',
    version=open(os.path.join('osutils', 'VERSION')).read().strip(),
    author='Bharat Kunwar',
    author_email='bharat@stackhpc.com',
    packages=['osutils', 'osutils.tests'],
    package_data={'osutils': [os.path.join('tests'), 'VERSION']},
    scripts=['bin/osnode', 'bin/tmuxipmi'],
    url='https://github.com/stackhpc/stackhpc-osutils',
    license='Apache (see LICENSE file)',
    description='OpenStack utilities',
    long_description=long_description,
    python_requires=">=2.7",
    install_requires=requirements,
    test_suite='osutils.tests'
)
