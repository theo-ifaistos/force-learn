#! /usr/bin/env python
"""Plug and play Reinforcement Learning."""

import codecs
import os

from setuptools import find_packages, setup

ver_file = os.path.join('flearn', '_version.py')
with open(ver_file) as f:
    exec(f.read())

DISTNAME = 'force-learn'
DESCRIPTION = 'Plug and play Reinforcement Learning.'
with codecs.open('README.rst', encoding='utf-8-sig') as f:
    LONG_DESCRIPTION = f.read()
MAINTAINER = 'G. Douzas'
MAINTAINER_EMAIL = 'gdouzas@icloud.com'
URL = 'https://github.com/georgedouzas/force-learn'
LICENSE = 'MIT'
DOWNLOAD_URL = 'https://github.com/georgedouzas/force-learn'
VERSION = __version__
INSTALL_REQUIRES = ['gym>=0.18']
CLASSIFIERS = ['Intended Audience :: Science/Research',
               'Intended Audience :: Developers',
               'License :: OSI Approved',
               'Programming Language :: Python',
               'Topic :: Software Development',
               'Topic :: Scientific/Engineering',
               'Operating System :: Microsoft :: Windows',
               'Operating System :: POSIX',
               'Operating System :: Unix',
               'Operating System :: MacOS',
               'Programming Language :: Python :: 3.6',
               'Programming Language :: Python :: 3.7',
               'Programming Language :: Python :: 3.8']

setup(
    name=DISTNAME,
    maintainer=MAINTAINER,
    maintainer_email=MAINTAINER_EMAIL,
    description=DESCRIPTION,
    license=LICENSE,
    url=URL,
    version=VERSION,
    download_url=DOWNLOAD_URL,
    long_description=LONG_DESCRIPTION,
    zip_safe=False,
    classifiers=CLASSIFIERS,
    packages=find_packages(),
    install_requires=INSTALL_REQUIRES,
)