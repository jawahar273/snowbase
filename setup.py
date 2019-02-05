#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

def parse_requirements(filename):
    """ load requirements from a pip requirements file
        refer: `link <https://stackoverflow.com/questions/25192794/no-module-named-pip-req/>`_
    """
    lineiter = (line.strip() for line in open(filename))
    return [line for line in lineiter if line and not line.startswith("#")]


requirements = parse_requirements("requirements.txt")

setup_requirements = [ ]

test_requirements = [ ]

setup(
    author="Jawahar S",
    author_email='jawahar273@gmail.com',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    description="snowbase is python package for storeing the result data from task such as POS tag, Keywords etc.. as this restul can be retrive for reprocessing(one way of efficiency)",
    install_requires=requirements,
    license="MIT license",
    long_description=readme,
    include_package_data=True,
    keywords='snowbase',
    name='snowbase',
    packages=find_packages(include=['snowbase']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/jawahar273/snowbase',
    version='0.1.0',
    zip_safe=False,
)
