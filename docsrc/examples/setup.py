"""
Python setup.py setuptools template for Python 2.6 or greater.

Python Packaging Guide: https://packaging.python.org/en/latest/index.html
"""
# pylint: disable=line-too-long

from __future__ import print_function

import os
import sys

try:
    from pkg_resources import parse_version
    from setuptools    import Extension, find_packages, setup

    import setuptools
except ImportError as err:
    print('Python 2.6 or greater and setuptools is required for install:', file=sys.stderr)
    print('\thttps://packaging.python.org/en/latest/installing.html#requirements-for-installing-packages',
          file=sys.stderr)
    sys.exit(1)

def read_file(file_name):
    """
    File read wrapper for loading data unmodified from arbritrary file.
    """

    file_data = None

    try:
        with open(file_name, 'r') as fin:
            file_data = fin.read()
    except Exception as err: # pylint: disable=broad-except
        print('Failed to read data from file \'%s\': %s' % (file_name, str(err)), file=sys.stderr)
        sys.exit(1)

    return file_data

if issubclass(sys.version_info.__class__, tuple):
    PYTHON_VERSION = ".".join(map(str, sys.version_info[:3]))
else:
    PYTHON_VERSION = '.'.join(map(str, [sys.version_info.major, sys.version_info.minor, sys.version_info.micro]))

if parse_version(PYTHON_VERSION) < parse_version('2.6'):
    print('Python 2.6 or greater is required.')
    sys.exit(1)

PYTHON_3_EXTRAS = {}

if parse_version(PYTHON_VERSION) >= parse_version('3'):
    setuptools.use_2to3_on_doctests = True
    # List of doctest source files that need to be converted with 2to3.
    PYTHON_3_EXTRAS['convert_2to3_doctests'] = [
        'doctest.py'
        ]
    # Convert the source code from Python 2 to Python 3 with 2to3 during the build process.
    PYTHON_3_EXTRAS['use_2to3'] = True
    # A list of modules to exclude for additional fixers to be used during the 2to3 conversion.
    PYTHON_3_EXTRAS['use_2to3_exclude_fixers'] = [
        'lib2to3.fixes.fix_import'
        ]
    # A list of modules to search for additional fixers to be used during the 2to3 conversion.
    PYTHON_3_EXTRAS['use_2to3_fixers'] = [
        'your.fixers'
        ]

# All options to setup are passed through to distutils 'Distribution' instances based on
# the command provided at the cli. For a list of distributions and options see
# the API reference for distutils at https://docs.python.org/2.6/distutils/apiref.html
# Setup also accepts additional parameters when building Python extensions that arent listed
# below at https://docs.python.org/2.6/distutils/apiref.html#module-distutils.core
setup( # pylint: disable=star-args
    # package author's nameclass distutils.core.Extension
    author='John Doe',
    # email address of the package author
    author_email='John_Doe@missing.com',
    # a list of classifiers from https://pypi.python.org/pypi?:action=list_classifiers
    classifiers=[
        'classifier one',
        'classifier two'
        ],
    # A mapping of command names to Command subclasses
    cmdclass={
        'cmd_name': 'module.someclass'
        },
    # A list of data files to install
    data_files=[
        'data/myfile'
        ],
    # A list of strings naming URLs to be searched when satisfying dependencies.
    # These links will be used if needed to install packages specified by setup_requires or
    # tests_require. They will also be written into the egg's metadata for use by tools like
    # EasyInstall to use when installing an .egg file.
    # The URLs must be either:
    #   1. direct download URLs,
    #   2. the URLs of web pages that contain direct download links, or
    #   3. the repository's URL
    # pointing to:
    #   - an egg, in the standard distutils sdist format,
    #   - a single .py file, or
    #   - a VCS repository (Subversion, Mercurial, or Git).
    # If you depend on a package that's distributed as a single .py file, you must include an
    # '#egg=project-version' suffix to the URL, to give a project name and version number. (Be
    # sure to escape any dashes in the name or version by replacing them with underscores.)
    # EasyInstall will recognize this suffix and automatically create a trivial setup.py to wrap
    # the single .py file as an egg.
    # In the case of a VCS checkout, you should also append #egg=project-version in order to identify
    # for what package that checkout should be used. You can append @REV to the URL's path (before
    # the fragment) to specify a revision. Additionally, you can also force the VCS being used by
    # prepending the URL with a certain prefix. Currently available are:
    #
    #   - svn+URL for Subversion,
    #   - git+URL for Git, and
    #   - hg+URL for Mercurial
    #
    # A more complete example would be:
    #    'vcs+proto://host/path@revision#egg=project-version'
    # Be careful with the version. It should match the one inside the project files. If you want to
    # disregard the version, you have to omit it both in the requires and in the URL's fragment.
    dependency_links=[
        'http://dependencysite.com/depenecy_dl_link'
        ],
    # short, summary description of the package
    description='package description',
    # the Distribution class to use
    distclass=setuptools.Distribution,
    # location where the package may be downloaded
    download_url='http://www.missing.com/doe/404.pkg',
    # A list of strings naming resources that should be extracted together, if any of them
    # is needed, or if any C extensions included in the project are imported. This argument
    # is only useful if the project will be installed as a zipfile, and there is a need to have
    # all of the listed resources be extracted to the filesystem as a unit. Resources listed here
    # should be '/'-separated paths, relative to the source root, so to list a resource foo.png in
    # package bar.baz, you would include the string bar/baz/foo.png in this argument.
    # If you only need to obtain resources one at a time, or you don't have any C extensions that
    # access other files in the project (such as data files or shared libraries), you probably do NOT
    # need this argument and shouldn't mess with it.
    eager_resources=[
        ],
    # A dictionary mapping entry point group names to strings or lists of strings defining
    # the entry points. Entry points are used to support dynamic discovery of services or plugins
    # provided by a project.
    entry_points={
        'console_scripts': [
            'foo = my_package.some_module:main_func',
            'bar = other_module:some_func',
            'rst2pdf = project_name.tools.pdfgen [PDF]' # Brackets define one of the extras required
            ],
        'gui_scripts': [
            'baz = my_package_gui:start_func'
            ],
        # Non Windows eggsecutable scripts
        # For the executable prelude to run, the appropriate version of Python must be available via
        # the PATH environment variable, under its "long" name. That is, if the egg is built for Python
        # 2.3, there must be a python2.3 executable present in a directory on PATH.
        'setuptools.installation': [
            'eggsecutable = my_package.some_module:main_func'
            ]
        },
    # The exclude_package_data option is a dictionary mapping package names to lists of wildcard patterns,
    # just like the package_data option. And, just as with that option, a key of '' will apply the given pattern(s)
    # to all packages. However, any files that match these patterns will be excluded from installation, even if
    # they were listed in package_data or were included as a result of using include_package_data.
    #
    # In summary, the three options allow you to:
    #
    # include_package_data
    #     Accept all data files and directories matched by MANIFEST.in or found in source control.
    # package_data
    #     Specify additional patterns to match files and directories that may or may not be matched by MANIFEST.in
    #     or found in source control.
    # exclude_package_data
    #     Specify patterns for data files and directories that should not be included when a package is installed,
    #     even if they would otherwise have been included due to the use of the preceding options.
    #
    # NOTE: Due to the way the distutils build process works, a data file that you include in your project and then
    # stop including may be "orphaned" in your project's build directories, requiring you to run setup.py clean --all
    # to fully remove them. This may also be important for your users and contributors if they track intermediate
    # revisions of your project using Subversion; be sure to let them know when you make changes that remove files
    #from inclusion so they can run setup.py clean --all.
    exclude_package_data={
        'namespace_module_name': ['__init__.py']
        },
    # A list of Python extensions to be built
    ext_modules=[
        Extension(
            # list of macros to define; each macro is defined using a 2-tuple (name, value), where value is either the
            # string to define it to or None to define it without a particular value (equivalent of #define FOO in
            # source or -DFOO on Unix C compiler command line)
            define_macros=[('STUPIDCDEF', 1)],
            # list of files that the extension depends on
            depends=['/some/file'],
            # list of symbols to be exported from a shared extension. Not used on all platforms, and not generally
            # necessary for Python extensions, which typically export exactly one symbol: init + extension_name.
            export_symbols=['init', 'extension_name'],
            # any extra platform- and compiler-specific information to use when compiling the source files in 'sources'.
            # For platforms and compilers where a command line makes sense, this is typically a list of command-line
            # arguments, but for other platforms it could be anything.
            extra_compile_args=['arg1', 'arg2'],
            # any extra platform- and compiler-specific information to use when linking object files together to create
            # the extension (or to create a new static Python interpreter). Similar interpretation as for
            # 'extra_compile_args'.
            extra_link_args=['arg1', 'arg2'],
            # list of extra files to link with (eg. object files not implied by 'sources', static library that must be
            # explicitly specified, binary resource files, etc.)
            extra_objects=['data.o'],
            # list of directories to search for C/C++ header files (in Unix form for portability)
            include_dirs=['/usr/lib/include'],
            # extension language (i.e. 'c', 'c++', 'objc'). Will be detected from the source extensions if not provided.
            language='c++',
            # list of library names (not filenames or paths) to link against
            libraries=['pthread'],
            # list of directories to search for C/C++ libraries at link time
            library_dirs=['/usr/lib'],
            # the full name of the extension, including any packages - ie. not a filename or pathname, but Python
            # dotted name
            name='extension_name',
            # list of directories to search for C/C++ libraries at run time (for shared extensions, this is when the
            # extension is loaded)
            runtime_library_dirs=['myapp/lib'],
            # list of source filenames, relative to the distribution root (where the setup script lives), in Unix form
            # (slash-separated) for portability. Source files may be C, C++, SWIG (.i), platform-specific resource
            # files, or whatever else is recognized by the build_ext command as source for a Python extension.
            sources=['/some/file.c'],
            # list of macros to undefine explicitly
            undef_macros=['STUPIDCDEF']
            )
        ],
    # A dictionary mapping names of "extras" (optional features of your project) to strings or lists
    # of strings specifying what other distributions must be installed to support those features.
    # Sometimes a project has "recommended" dependencies, that are not required for all uses of the project.
    # For example, a project might offer optional PDF output if ReportLab is installed, and reStructuredText
    # support if docutils is installed. These optional features are called "extras", and setuptools allows you to
    # define their requirements as well.
    extras_require={
        'optional_feature_name': ['pkg_required_for_opt_feature'],
        'PDF':  ['ReportLab>=1.2', 'RXP'],
        'reST': ['docutils>=0.3']
        },
    # If set to True, this tells setuptools to automatically include any data files it finds inside your
    # package directories, that are either under CVS or Subversion control, or which are specified by your
    # MANIFEST.in file. (They can also be tracked by another revision control system, using an appropriate
    # plugin. See the
    # http://pythonhosted.org/setuptools/setuptools.html#adding-support-for-other-revision-control-systems
    # for information on how to write such plugins.)
    # If the data files are not under version control, or are not in a supported version control system, or if
    # you want finer-grained control over what files are included (for example, if you have documentation files
    # in your package directories and want to exclude them from installation), then you can also use the package_data
    # keyword.
    # Note: although the package_data argument was previously only available in setuptools, it was also added to the
    # Python distutils package as of Python 2.4. If using the setuptools-specific include_package_data argument,
    # files specified by package_data will not be automatically added to the manifest unless they are tracked by a
    # supported version control system, or are listed in the MANIFEST.in file.
    # The MANIFEST.in file format documentation can be found at https://docs.python.org/2/distutils/sourcedist.html
    include_package_data=True,
    # A string or list of strings specifying what other distributions need to be installed when this one is.
    install_requires=[
        'required_package_name',
        'docutils >= 0.3',
        'BazSpam ==1.1, ==1.2, ==1.3, ==1.4, ==1.5, ==1.6, ==1.7',
        'PEAK[FastCGI, reST, extras_pkg_name_3]>=0.5a4', # Brackets mark the extras required which are normally optional
        'setuptools==0.5a7'
        ],
    # license for the package
    license='GPLv2',
    # longer description of the package
    long_description=read_file(os.path.join(os.path.dirname(__file__), 'README.md')),
    # A list of additional keywords to be used to assist searching for the package in a larger catalog.
    keywords='some tags',
    # package maintainer's name
    maintainer='John Doe',
    # email address of the package maintainer
    maintainer_email='John_Doe@missing.com',
    # name of the package
    name='package-name',
    # A list of strings naming the project's "namespace packages". A namespace package is
    # a package that may be split across multiple project distributions. For example, Zope
    # 3's zope package is a namespace package, because subpackages like zope.interface and
    # zope.publisher may be distributed separately. The egg runtime system can automatically
    # merge such subpackages into a single parent package at runtime, as long as you declare
    # them in each project that contains any subpackages of the namespace package, and as long
    # as the namespace package's __init__.py does not contain any code other than a namespace declaration.
    #
    # For all namspace packages, you need to add an __init__.py with the following and *nothing*
    # else (note that if you package this as an RPM, these __init__.py files will have to be held in a
    # different RPM than the current package and that those RPMs for the namespace modules will
    # have to be shared by all packages belonging to that namespace):
    #
    #   import pkg_resources
    #
    #   pkg_resources.declare_namespace(__name__)
    #
    # For more information see PEP 420: https://www.python.org/dev/peps/pep-0420/
    namespace_packages=[
        'company',
        'company.team'
        ],
    # default options for the setup script
    options='',
    # A dictionary mapping package names to lists of glob patterns. You do not need to use this option
    # if you are using include_package_data, unless you need to add e.g. files that are generated by your
    # setup script and build process. (And are therefore not in source control or are files that you don't
    # want to include in your source distribution.)
    package_data={
        '': ['*.txt', '*.rst'],
        'hello': ['*.msg']
        },
    # A mapping of package to directory names
    package_dir={
        '': 'package_name', #Default package
        'package': 'package_dir'
        },
    # A list of Python packages that distutils will manipulate
    # find_packages() takes a source directory and two lists of package name patterns to exclude and include.
    # If omitted, the source directory defaults to the same directory as the setup script.
    # Inclusion and exclusion patterns are package names, optionally including wildcards.
    packages=find_packages('pkg_dir', exclude=[]),
    # a list of platforms
    platforms=[
        'platform one',
        'platform two'
        ],
    # A list of Python modules that distutils will manipulate
    py_modules=[
        'company.team.module'
        ],
    # Arguments to supply to the setup script
    script_args=[
        'arg1',
        'arg2'
        ],
    # The name of the setup.py script
    script_name=sys.argv[0],
    # A list of standalone script files to be built and installed
    scripts=[
        'bin/script'
        ],
    # A string or list of strings specifying what other distributions need to be present
    # in order for the setup script to run. setuptools will attempt to obtain these (even
    # going so far as to download them using EasyInstall) before processing the rest of the
    # setup script or commands. This argument is needed if you are using distutils extensions
    # as part of your build process; for example, extensions that process setup() arguments and
    # turn them into EGG-INFO metadata files.
    # (Note: projects listed in setup_requires will NOT be automatically installed on the system
    # where the setup script is being run. They are simply downloaded to the ./.eggs directory if
    # they're not locally available already. If you want them to be installed, as well as being
    # available when the setup script is run, you should add them to install_requires and setup_requires.)
    setup_requires=[
        'required_package_name',
        'docutils >= 0.3',
        'BazSpam ==1.1, ==1.2, ==1.3, ==1.4, ==1.5, ==1.6, ==1.7',
        'PEAK[FastCGI, reST, extras_pkg_name_3]>=0.5a4', # Brackets mark the extras required which are normally optional
        'setuptools==0.5a7'
        ],
    # If you would like to use a different way of finding tests to run than
    # what setuptools normally uses, you can specify a module name and class name in
    # this argument. The named class must be instantiable with no arguments, and its
    # instances must support the loadTestsFromNames() method as defined in the Python
    # unittest module's TestLoader class. Setuptools will pass only one test "name" in
    # the names argument: the value supplied for the test_suite argument. The loader you
    # specify may interpret this string in any way it likes, as there are no restrictions
    # on what may be contained in a test_suite string/
    # The module name and class name must be separated by a :. The default value of this
    # argument is 'setuptools.command.test:ScanningLoader'. If you want to use the default
    # unittest behavior, you can specify 'unittest:TestLoader' as your test_loader argument
    #instead. This will prevent automatic scanning of submodules and subpackages.
    # The module and class you specify here may be contained in another package, as long as
    # you use the tests_require option to ensure that the package containing the loader class
    # is available when the test command is run.
    test_loader='setuptools.command.test:ScanningLoader',
    # If your project's tests need one or more additional packages besides those
    # needed to install it, you can use this option to specify them. It should be a
    # string or list of strings specifying what other distributions need to be present
    # for the package's tests to run. When you run the test command, setuptools will
    # attempt to obtain these (even going so far as to download them using EasyInstall).
    # Note that these required projects will not be installed on the system where the
    # tests are run, but only downloaded to the project's setup directory if they're not
    # already installed locally.
    tests_require=[
        'required_package_name',
        'docutils >= 0.3',
        'BazSpam ==1.1, ==1.2, ==1.3, ==1.4, ==1.5, ==1.6, ==1.7',
        'PEAK[FastCGI, reST, extras_pkg_name_3]>=0.5a4', # Brackets mark the extras required which are normally optional
        'setuptools==0.5a7'
        ],
    # A string naming a unittest.TestCase subclass (or a package or module containing
    # one or more of them, or a method of such a subclass), or naming a function that
    # can be called with no arguments and returns a unittest.TestSuite. If the named
    # suite is a module, and the module has an additional_tests() function, it is called
    # and the results are added to the tests to be run. If the named suite is a package,
    # any submodules and subpackages are recursively added to the overall test suite.
    # Specifying this argument enables use of the test command to run the specified test
    # suite, e.g. via setup.py test.
    test_suite='your.module.tests',
    # home page for the package
    url='http://www.missing.com/doe/404.html',
    # version of this release
    version=read_file(os.path.join(os.path.dirname(__file__), 'VERSION')).strip(),
    # A boolean (True or False) flag specifying whether the project can be safely
    # installed and run from a zip file. If this argument is not supplied, the bdist_egg
    # command will have to analyze all of your project's contents for possible problems each time it builds an egg.
    zip_safe=True,
    **PYTHON_3_EXTRAS
)
