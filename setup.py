# -*- coding: utf-8 -*-
"""Distribute 'setuplib', the core library for extensions of *setuptools*.

Additional local options for this *setup.py* module:
   --sdk:
       Requires sphinx, epydoc, and dot-graphics.

   --no-install-requires: 
       Suppresses installation dependency checks,
       requires appropriate PYTHONPATH.

   --offline: 
       Sets online dependencies to offline, or ignores online
       dependencies.

"""
from __future__ import absolute_import
from __future__ import print_function

try:
    # optional remote debug
    from rdbg import start        # load a slim bootstrap module
    start.start_remote_debug()    # check whether '--rdbg' option is present, if so accomplish bootstrap
except:
    pass


import os
import sys
import re

import setuptools

#
# setup extension modules
#

import yapyutils.files.utilities


#***
# the following parts are required as for the setuplib itself
# others may use the entry points
#***

# setup library functions
# import setuplib.setuplib
from setuplib.setuplib import SetupListEntryPointsX

# setup extension modules
import setupdocx

# documents
from setupdocx.build_docx import BuildDocX
from setupdocx.dist_docx import DistDocX
from setupdocx.install_docx import InstallDocX
from setupdocx.build_apiref import BuildApirefX
from setupdocx.build_apidoc import BuildApidocX

# unittests
import setuptestx.testx
from setuptestx.testx import TestX



__author__ = 'Arno-Can Uestuensoez'
__author_email__ = 'acue_sf2@sourceforge.net'
__license__ = "Artistic-License-2.0 + Forced-Fairplay-Constraints"
__copyright__ = "Copyright (C) 2015-2019 Arno-Can Uestuensoez @Ingenieurbuero Arno-Can Uestuensoez"
__uuid__ = "239b0bf7-674a-4f53-a646-119f591af806"

__vers__ = [0, 1, 5, ]
__version__ = "%02d.%02d.%03d" % (__vers__[0], __vers__[1], __vers__[2],)
__release__ = "%d.%d.%d" % (__vers__[0], __vers__[1], __vers__[2],) + '-rc0'
__status__ = 'beta'


__sdk = False
"""Set by the option "--sdk". Controls the installation environment."""
if '--sdk' in sys.argv:
    __sdk = True
    sys.argv.remove('--sdk')


# required for various interfaces, thus just do it
_mypath = os.path.dirname(os.path.abspath(__file__))
"""Path of this file."""
sys.path.insert(0, os.path.abspath(_mypath))


#--------------------------------------
#
# Package parameters for setuptools
#
#--------------------------------------

_name = 'setuplib'
"""package name"""

__pkgname__ = _name
"""package name"""

_version = "%d.%d.%d" % (__vers__[0], __vers__[1], __vers__[2],)
"""assembled version string"""

_author = __author__
"""author of the package"""

_author_email = __author_email__
"""author's email """

_license = __license__
"""license"""

#_packages = setuptools.find_packages('setuplib')
_packages = ['setuplib',]
"""Python packages to be installed."""

print("4TEST:" + str(_packages))
_packages_sdk = _packages

_scripts = [
]
"""Scripts to be installed."""

_package_data = {
    'setuplib': [
        'README.md', 'ArtisticLicense20.html', 'licenses-amendments.txt',
    ],
}
"""Provided data of the package."""

_url = 'https://sourceforge.net/projects/setuplib/'
"""URL of this package"""

# _download_url="https://github.com/ArnoCan/setuplib/"
_download_url = "https://sourceforge.net/projects/setuplib/files/"


_install_requires = [
    'pythonids >= 0.1.0',
    'yapyutils >= 0.1.0',
    'yapydata >= 0.1.0',
    'sourceinfo >= 0.1.0',
]
"""prerequired non-standard packages"""


_description = "Support library functions for extensions and entry points of setuptools / distutils."

_README = os.path.join(os.path.dirname(__file__), 'README.md')
_long_description = open(_README).read()
"""detailed description of this package"""


if __sdk:  # pragma: no cover
    try:
        import sphinx_rtd_theme  # @UnusedImport
    except:
        sys.stderr.write(
            "WARNING: Cannot import package 'sphinx_rtd_theme', cannot create local 'ReadTheDocs' style.")

    _install_requires.extend(
        [
            'pythonids',
            'sphinx >= 1.4',
            'epydoc >= 3.0',
        ]
    )

    _packages = _packages_sdk

_test_suite = "tests.CallCase"

__no_install_requires = False
if '--no-install-requires' in sys.argv:
    __no_install_requires = True
    sys.argv.remove('--no-install-requires')

__offline = False
if '--offline' in sys.argv:
    __offline = True
    __no_install_requires = True
    sys.argv.remove('--offline')


if __no_install_requires:
    print("#")
    print("# Changed to offline mode, ignore install dependencies completely.")
    print("# Requires appropriate PYTHONPATH.")
    print("# Ignored dependencies are:")
    print("#")
    for ir in _install_requires:
        print("#   " + str(ir))
    print("#")
    _install_requires = []


class setuplibx(SetupListEntryPointsX):
    """For pre-installation, and test and debug of setuplib.
    Standard application sshould use the provided entry points. 
    """
    def __init__(self, *args, **kargs):
        SetupListEntryPointsX.__init__(self, *args, **kargs)


class build_docx(BuildDocX):
    """For pre-installation, and test and debug of setuplib. 
    Standard application sshould use the provided entry points. 
    """
    def __init__(self, *args, **kargs):
        BuildDocX.__init__(self, *args, **kargs)


class install_docx(InstallDocX):
    """For pre-installation, and test and debug of setuplib. 
    Standard application sshould use the provided entry points. 
    """
    def __init__(self, *args, **kargs):
        InstallDocX.__init__(self, *args, **kargs)


class dist_docx(DistDocX):
    """For pre-installation, and test and debug of setuplib. 
    Standard application sshould use the provided entry points. 
    """
    def __init__(self, *args, **kargs):
        DistDocX.__init__(self, *args, **kargs)


class build_apidoc(BuildApidocX):
    """For pre-installation, and test and debug of setuplib. 
    Standard application sshould use the provided entry points. 
    """
    def __init__(self, *args, **kargs):
        BuildApidocX.__init__(self, *args, **kargs)


class build_apiref(BuildApirefX):
    """For pre-installation, and test and debug of setuplib. 
    Standard application sshould use the provided entry points. 
    """
    def __init__(self, *args, **kargs):
        BuildApirefX.__init__(self, *args, **kargs)


class testx(setuptestx.testx.TestX):
    """For pre-installation, and test and debug of setuplib. 
    Standard application sshould use the provided entry points. 
    """
    def __init__(self, *args, **kargs):
        setuptestx.testx.TestX.__init__(self, *args, **kargs)


#
# see setup.py for remaining parameters
#
setuptools.setup(
    author=_author,
    author_email=_author_email,
    cmdclass={
        'build_apidoc': build_apidoc,
        'build_apiref': build_apiref,
        'build_docx': build_docx,
        'dist_docx': dist_docx,
        'install_docx': install_docx,
        'list_entry_points': setuplibx,
        'testx': testx,
    },
    description=_description,
#    distclass=setuplib.dist.Distribution,  # extends the standard help-display of setuptools
    download_url=_download_url,
    entry_points={
        'distutils.commands': 'lsep = setuplib.setuplib:SetupListEntryPointsX',
        'distutils.commands': 'list_entry_points = setuplib.setuplib:SetupListEntryPointsX',
    },
    install_requires=_install_requires,
    license=_license,
    long_description=_long_description,
    name=_name,
    package_data=_package_data,
    packages=_packages,
    scripts=_scripts,
    url=_url,
    version=_version,
    zip_safe=False,
)

sys.exit(0)

