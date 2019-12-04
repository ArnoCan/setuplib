
.. _setuplibSETUPLIB:

.. raw:: html

   <div class="shortcuttab">


setuplib.setuplib
=================

For current help refer tot the online help:

   .. parsed-literal::
   
      python setup.py setuplib --help

Alternative implementations are:

   .. parsed-literal::
   
      ipython setup.py setuplib --help
      jython  setup.py setuplib --help  # requires special install of setuptools, refer to the manuals 
      pypy    setup.py setuplib --help

      ipw.exe setup.py setuplib --help  # IronPython on Windows

With current output:

   .. parsed-literal::
   
      Options for 'setuplib' command:
        --debug (-d)           Raises degree of debug traces of current context.
                               Supports repetition. Each raises the debug verbosity
                               level of the context by one.
        --exit (-e)            Exit after command 'setuplib' immediately, ignore
                               following. Default := off.
        --filter               Define a filter, for details refer to the manual. See
                               '--filter=help. Default: ''
        --format (-f)          Define display format. See '--format=help. Default:
                               'name,module_name,dist.egg_info:::fname'
        --group (-g)           Set group for scan, '--group=none' scans all. See
                               'PyPA.io'.Default: 'distutils.commands'
        --ignore-missing (-i)  Ignore errors due to missing components, and
                               continue.  For example in case of missing an
                               optional. Default: False. 
        --layout               Define display layout. See '--format=help'. Default:
                               table
        --long (-l)            List long format, similar to shell command 'ls -l'.
                               Default: off
        --quiet (-q)           Suppress display including warnings. Display error
                               messages only.Default: off
        --search-path (-P)     Set the search path for requested resources. Default:
                               'sys.path'
        --sort                 Sort a specified field number. Default: 0
        --verbose (-v)         Raises verbosity of current context. Supports
                               repetition. Each raises the command verbosity level
                               of the context by one. The value is defined by the
                               global option defined in 'Distribution'. Refer to the
                               manuals for the special behaviour when used as either
                               a global option(start 'verbose=1'), or as a command
                               context option(start 'verbose=0'). Default:=1.


Module
------
.. automodule:: setuplib.setuplib


SetupListEntryPointsX
---------------------
.. autoclass:: SetupListEntryPointsX

.. _SPEC_SetupListEntryPointsX_finalize_options:

finalize_options
^^^^^^^^^^^^^^^^
.. automethod:: SetupListEntryPointsX.finalize_options

.. _SPEC_SetupListEntryPointsX_initialize_options:

initialize_options
^^^^^^^^^^^^^^^^^^
.. automethod:: SetupListEntryPointsX.initialize_options

.. _SPEC_SetupListEntryPointsX_run:

run
^^^
.. automethod:: SetupListEntryPointsX.run


MyDistributionData
------------------
.. autoclass:: MyDistributionData

.. _SPEC_MyDistributionData__init__:

__init__
^^^^^^^^
.. automethod:: MyDistributionData.__init__

.. _SPEC_MyDistributionData_enumerate:

enumerate
^^^^^^^^^
.. automethod:: MyDistributionData.enumerate

.. _SPEC_MyDistributionData_print:

print
^^^^^
.. automethod:: MyDistributionData.print

.. _SPEC_MyDistributionData_print_groups:

print_groups
^^^^^^^^^^^^
.. automethod:: MyDistributionData.print_groups

.. _SPEC_MyDistributionData_print_groups_list:

print_groups_list
^^^^^^^^^^^^^^^^^
.. automethod:: MyDistributionData.print_groups_list


.. _SPEC_MyDistributionData_print_list:

print_list
^^^^^^^^^^
.. automethod:: MyDistributionData.print_list


.. _SPEC_MyDistributionData_print_table:

print_table
^^^^^^^^^^^
.. automethod:: MyDistributionData.print_table

.. _SPEC_MyDistributionData_print_alias_list:

Exceptions
----------

.. autoexception:: SetuplibCommandsxError

.. raw:: html

   </div>

