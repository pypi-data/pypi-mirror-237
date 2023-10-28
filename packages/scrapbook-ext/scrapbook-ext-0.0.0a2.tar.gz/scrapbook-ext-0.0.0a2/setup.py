#!/usr/bin/env python3

import setuptools
import pathlib

this_directory = pathlib.Path(__file__).parent

setuptools.setup(
    name='scrapbook-ext',
    version='0.0.0a2',
    description='Extensions for scrapbook',
    long_description=(this_directory / 'README.md').read_text(),
    long_description_content_type='text/markdown',
    python_requires='>=3.6',
    package_dir={
        '': 'packages'
    },
    packages=setuptools.find_packages(where='packages'),
    install_requires=[
        'scrapbook'
    ],
    extras_require={
        'dev': []
    }
)
