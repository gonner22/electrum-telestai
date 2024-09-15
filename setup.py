#!/usr/bin/env python3

# python setup.py sdist --format=zip,gztar

import os
import sys
import platform
import importlib.util
import argparse
import subprocess

from setuptools import setup, find_packages
from setuptools.command.install import install

MIN_PYTHON_VERSION = "3.8.0"
_min_python_version_tuple = tuple(map(int, (MIN_PYTHON_VERSION.split("."))))


if sys.version_info[:3] < _min_python_version_tuple:
    sys.exit("Error: Electrum-TLS requires Python version >= %s..." % MIN_PYTHON_VERSION)

with open('contrib/requirements/requirements.txt') as f:
    requirements = f.read().splitlines()

with open('contrib/requirements/requirements-hw.txt') as f:
    requirements_hw = f.read().splitlines()

# load version.py; needlessly complicated alternative to "imp.load_source":
version_spec = importlib.util.spec_from_file_location('version', 'electrum_tls/version.py')
version_module = version = importlib.util.module_from_spec(version_spec)
version_spec.loader.exec_module(version_module)

data_files = []

if platform.system() in ['Linux', 'FreeBSD', 'DragonFly']:
    # note: we can't use absolute paths here. see #7787
    data_files += [
        (os.path.join('share', 'applications'),               ['electrum-tls.desktop']),
        (os.path.join('share', 'pixmaps'),                    ['electrum_tls/gui/icons/electrum-tls.png']),
        (os.path.join('share', 'icons/hicolor/128x128/apps'), ['electrum_tls/gui/icons/electrum-tls.png']),
    ]

extras_require = {
    'hardware': requirements_hw,
    'gui': ['pyqt5'],
    'crypto': ['cryptography>=2.6'],
    'tests': ['pycryptodomex>=3.7', 'cryptography>=2.6', 'pyaes>=0.1a1'],
    'qml_gui': ['pyqt6', 'Pillow>=8.4.0']
}
# 'full' extra that tries to grab everything an enduser would need (except for libsecp256k1...)
extras_require['full'] = [pkg for sublist in
                          (extras_require['hardware'], extras_require['gui'], extras_require['crypto'])
                          for pkg in sublist]
# legacy. keep 'fast' extra working
extras_require['fast'] = extras_require['crypto']


setup(
    name="Electrum-tls",
    version=version.ELECTRUM_VERSION,
    python_requires='>={}'.format(MIN_PYTHON_VERSION),
    install_requires=requirements,
    extras_require=extras_require,
    packages=(['electrum_tls',]
              + [('electrum_tls.'+pkg) for pkg in
                 find_packages('electrum_tls', exclude=["tests"])]),
    package_dir={
        'electrum_tls': 'electrum_tls'
    },
    # Note: MANIFEST.in lists what gets included in the tar.gz, and the
    # package_data kwarg lists what gets put in site-packages when pip installing the tar.gz.
    # By specifying include_package_data=True, MANIFEST.in becomes responsible for both.
    include_package_data=True,
    scripts=['electrum_tls/electrum-tls'],
    data_files=data_files,
    description="Lightweight Telestai Wallet",
    author="Ahmed Bodiwalaa",
    author_email="ahmedbodi@crypto-expert.com",
    license="MIT Licence",
    url="https://telestai.io",
    long_description="""Lightweight Telestai Wallet""",
)
