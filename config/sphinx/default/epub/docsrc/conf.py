# -*- coding: utf-8 -*-
"""Custom configuration of *conf.py*.
to be appended to the file:
    ::

        ${BUILDDIR}/sphinx/apidoc/conf.py

"""

import sys
import os
import sphinx

from distutils.version import LooseVersion


__author__ = 'Arno-Can Uestuensoez'
__license__ = "Artistic-License-2.0 + Forced-Fairplay-Constraints"
__copyright__ = "Copyright (C) 2016 Arno-Can Uestuensoez" \
                " @Ingenieurbuero Arno-Can Uestuensoez"
__version__ = '0.1.36'
__uuid__ = "239b0bf7-674a-4f53-a646-119f591af806"

__docformat__ = "restructuredtext en"


#
# add path for temporary tools required for this configuration
#
sys.path.insert(0, os.path.abspath(os.path.dirname(os.getcwd())))
sys.path.insert(0, os.path.abspath(os.getcwd()))


#
# global metadata
#
project = 'setupdocx'
copyright = __copyright__
license = __license__
version = __version__
uuid = __uuid__


# authoring support
#
todo_include_todos = False


#
# required minimal sphinx version
#
# needs_sphinx = '1.0'


#
# required extensions
#
extensions = []
if LooseVersion(sphinx.__version__) < LooseVersion('1.4'):
    extensions.extend(  # @UndefinedVariable
        [
            'sphinx.ext.pngmath.',
        ]
    )  #: provided by present conf.py @UndefinedVariable
# else:
#     extensions.extend(  # @UndefinedVariable
#         [
#             'sphinx.ext.imgmath.',
#         ]
#     )  #: provided by present conf.py @UndefinedVariable

extensions.extend(  # @UndefinedVariable
    [
        # 'javasphinx',
#         'matplotlib.sphinxext.only_directives',
#         'matplotlib.sphinxext.plot_directive',
        'sphinx.ext.autodoc',
        'sphinx.ext.doctest',
        'sphinx.ext.githubpages',
        'sphinx.ext.inheritance_diagram',
        'sphinx.ext.todo',
        'sphinx.ext.ifconfig',
    ]
)  #: provided by present conf.py @UndefinedVariable


extensions.extend(  # @UndefinedVariable
    [
        'setupdocx.sphinx.ext.imagewrap',
    ]
)  #: provided by present conf.py @UndefinedVariable

#
# master document of toctree
#
master_doc = 'index'

#
# source_suffix = ['.rst', '.md']
#
source_suffix = '.rst'

#
# language for generated text by sphinx
#
# language = None

#
# patterns to ignore - relative to source directory
# (affects also html_static_path and html_extra_path)
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# style for syntax highlighting
pygments_style = 'sphinx'


###############################
#                             #
#        *** html ***         #
#                             #
###############################


#
# theme name
#
html_theme = 'epub_demo'                                              

html_title =  'SetupDocX'
#html_short_title = None

# html_show_copyright = False


#
# logo and favicon
#
html_logo = "_static/logo.png"
html_favicon = "_static/favicon.ico"  # 64x64 - 4bit/16    


#
# search paths - relative to the build directory + target directory
#
html_static_path = ['_static']
html_tepmplate_path = ['_templates']
html_theme_path = ['_themes']



#
# custom sidebar templates
#
#
# The default sidebars (for documents that don't match any pattern) are
# defined by theme itself.
#
#   html_sidebars = {
#      default: ``['localtoc.html', 'relations.html', 'sourcelink.html', 'searchbox.html']``
#   }
#


#
# html options
#
html_theme_options = {}



###############################
#                             #
#        *** epub ***         #
#                             #
###############################

epub_author = u'Arno-Can Uestuensoez'
epub_publisher = u'Ingenieurbuero Arno-Can Uestuensoez'
epub_copyright =  u'(C) 2019 Arno-Can Uestuensoez @Ingenieurbuero Arno-Can Uestuensoez'
epub_scheme = 'UUID'
epub_identifier = '45167c30-3261-4a38-9de4-d7151348ba48'
epub_uid = epub_identifier

# epub_cover = ('', 'epub-cover.html')
epub_tocdepth = 5
# epub_tocscope = 'includehidden'
epub_tocdup = False
# epub_guide
# epub_exclude_files = []


def setup(app):
    app.add_stylesheet('custom.css')
    
    if os.environ.get('DOCX_APIREF') == '1':
        # create API reference, activates 'quick navigation' menu entry
        app.add_config_value('apiref', '1', 'env')

    else:
        app.add_config_value('apiref', '0', 'env')

    app.add_config_value('variant', 'epub', 'env')
    