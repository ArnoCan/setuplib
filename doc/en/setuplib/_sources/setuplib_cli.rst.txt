
.. _SETUPLIBCLI:

**********************
Command Line Interface
**********************

The package *setuplib* provides extensions for the standard 
command line interface of *setup.py* from the *setuptools* / *distutils*.

* *setup.py* extension commands:

   .. raw:: html

      <style>
         div.tmptab table.docutils col {
            width: auto;
         }
         div.tmptab table td:nth-child(1) {
            width: 30ch;
         }
      </style>
   
      <div class="tmptab">
      <div class="overviewtab">
   
   +---------------------------------------------------------------+-------------------------------------------------------------------+
   | :ref:`list_entry_points <setuplibCOMMANDS_list_entry_points>` | Display extended information on python packages and entry points. |
   +---------------------------------------------------------------+-------------------------------------------------------------------+

   .. raw:: html
   
      </div>
      </div>

                  

.. _setuplibCLISYNOPSIS:

SYNOPSIS
========

.. parsed-literal::

   :ref:`setup.py <SETUP_PY>` :ref:`[Global-OPTIONS] <setuplibCLIOPTIONS>` :ref:`[COMMANDS-with-context-OPTIONS] <setuplibCOMMANDS>` 

.. _setuplibCLIOPTIONS:


OPTIONS
=======


.. _setuplibCOMMANDS:

COMMANDS
========
The commands could be combined within one call and are than processed from-left-to-right.
But be aware that each command is a separate module, thus only knows it's own options,
which are the right-hand side options util the following next command.

   .. index::
      pair: command; enum
      pair: command; info
      pair: command; list
      pair: command; show

   
   .. raw:: html

      <div class="tmptab">
      <div class="overviewtab">
   
   +---------------------------------------------------------------------------------------------------+-----------------------------------+
   | :ref:`setuplibCOMMANDS_list_entry_points`   [:ref:`setuplib-options <list_entry_points_OPTIONS>`] | display commands and entry points |
   +---------------------------------------------------------------------------------------------------+-----------------------------------+

   .. raw:: html
   
      </div>
      </div>


.. index::
   pair: setuplib; list_entry_points
   pair: setuplib; lsep
   pair: lsep; list_entry_points

.. _setuplibCOMMANDS_list_entry_points:

list_entry_points
-----------------


.. _list_entry_points_OPTIONS:

.. index::
   pair: break_on_err; --break-on-err

.. _list_entry_points_OPTIONS_break_on_err:

-\-break-on-err
^^^^^^^^^^^^^^^

   Exits the build process on first error. 
   
      .. parsed-literal::
      
         --break-on-error
   
         # default := False


.. index::
   pair: enum; --debug

.. _list_entry_points_OPTIONS_debug:

-\-debug
^^^^^^^^
   Raises degree of debug traces of current context. Supports repetition.
   Each raises the command verbosity level of the context by one.


.. index::
   pair: break_on_err; --break-on-err

.. _list_entry_points_OPTIONS_exit:

-\-exit
^^^^^^^
   Exit after command 'setuplib' immediately, ignore following. ::
   
      Default := off.


.. index::
   pair: filter; --filter

.. _list_entry_points_OPTIONS_filter:

-\-filter=
^^^^^^^^^^
   A list of filters for one or more fields.
   The filter is applied to all records.
   The degin is kept simple, thus a few keywords are defined only. 
   
   ::
   
      filter := <filter-rules> 
   
      filter-rules := <filter-rule> [; [ <LOGIC> ; ] <filter-rules>]
      filter-rule := <fieldname> ':' <python-re-expression>
      fieldname := "a present field name"
      python-re-expression := "a valid python regexpr"
   
      LOGIC := (
           AND    # True if all match
         | OR     # True if any matches
         | NAND   # True if not all match
         | NOR    # True if none match
         | XOR    # True if one only matches
      )
   
   The *--filter* option supports for one or more filter rules, where each is assigned to a given field.
   The filter rules are applied sequentially, by default with a resulting *AND* combination.
   The regular expressions are compiled by *re.compile()* and applied with the *re.search()* function.
   Records not matching all rules are dropped.  
   
   Examples are::
   
      python setup.py setuplib --group=console_scripts  --filter='dist.egg_info:Sphinx,module_name:quick'
      python setup.py setuplib --group=console_scripts  --filter='dist.egg_info:Sphinx;and;module_name:quick'
      python setup.py setuplib --group=console_scripts  --filter='dist.egg_info:Sphinx;or;module_name:quick'
      python setup.py setuplib --group=console_scripts  --filter='or;dist.egg_info:Sphinx;module_name:quick'
   
   The logic key is applied to the complete record, the position within the filter is arbitrary.
   The last occurance is the resulting  - LIFO.
   
   The filter is based on the *re* module, which performs a string search. 
   This requires the nodes to be converted to strings before searchin for the filter pattern. 
   The drawback for this method arises from the custom types, where the '*__str__*' and/or
   '*__repr__*' mehods return not the value of the noded only, but for example the class with it's
   parameters. 
   For example the *EntryPoint* class of the base type of the *setuptools* returns::
   
      __repr__: EntryPoint.parse('virtualenv = virtualenv:main')
      __str__:  virtualenv = virtualenv:main
   
   In both cases the string is the prefixed, either by the 'EntyrPoint.name' attribute,
   or simply by the class name and the parser call *EntryPoint.parse(*. 
   The '*re.search*' still matches as a floating regurlar expression, but does not
   when restrictions such as position tags are included.
   
   Anyhow, this effects nodes of type custom class only, where the *__str__* method is
   returns more than the value only.
   The standard data types of *Python* work flawless.
   The remaining quality of resulting accuracy is still pretty favourible for
   the actual required applications and tasks.
   
   The *setuplib* utilizes the *__str__**, just do not use on nodes which are
   not standard types, or have a custom *__str__* replacement::
   
      '^[asd123]*'
      '[asd123]*$'
      '^[asd123]*$'


.. index::
   pair: format; --format

.. _list_entry_points_OPTIONS_format:

-\-format=
^^^^^^^^^^
   Define display format parameters for current :ref:`--layout <list_entry_points_OPTIONS_layout>`.
   The format specifier supports the selection of names and the handling of the resulting values.
   
   ::
   
      format := <output-entries>
   
      output-entries := (
           <output-entries-table>
         | <output-entries-list>
         | <output-entries-json>
         | <output-entries-xml>
         | <output-entries-yaml>
      )
      
      output-entries-table := <column-entry> [ ',' <output-entries-table> ]
      column-entry := <field-name>[ ':' <field-width> [ ':' <width-overflow> [ ':' <special-content-opt>]]]
      field-name := "valid string of field name"
      field-width := "the display size of the field contents, depends on other parameters"
      width-overflow := "the behavior of field width processing"
      special-content-opt := "specific context format opts "
      
      output-entries-list := <list-item-entry> [ ',' <output-entries-list> ]
      list-item-entry := <field-name>[ ':' <field-width-list> [ ':' <width-overflow-list> [ ':' <special-content-opt>]]]
      field-width-list := "ignored"
      width-overflow-list := "ignored"
   
      Default: name,module_name,dist.key
   
   The detailed semantics of the fields are:
   
   * **field-name**:
   
      The name of the fied to be displayed. Valid field names are entity names below
      extension points. These are standard *Python* names with optional dotted object 
      identifier notation. The field name could be used multiple times, which results
      in multiple display of the same value. Each could have different additional
      parameters. The support comprises all *Python* data types, for the path
      resolution and valid syntax entries see 
      *yapydata.datatree.datatree.DataTree.__call__* [yapydata]_.
      The field name serves also as the parameter for :ref:`--sort <list_entry_points_OPTIONS_sort>`.
      The supported addressable container types are: ::
   
         list, dict
         tuple, set, frozenset
   
      Examples are: ::
   
         name
         module_name
   
         dist                          # dispalys the __str__/__repr__ output
         dist.extras                   # displays the list
         dist.extras.0                 # displays the first item in the list
         dist.egg_info                 # same as dist._provider.egg_info
   
         dist._provider
         dist._provider.module_path
         dist._provider.module_path
         dist._provider.egg_info       # same as dist.egg_info
   
   
   * **field-width**:
   
     Defines the width of displayed field contents. This may vary in it's behavior and
     size in dependence of the defined *field-overflow*. A special meaning ha the value
     of '0', which forces the *auto* mode for *field-overflow*. 
   
   
   * **field-overflow**:
   
     * *auto*
   
       The field is set to the length of the value with the maximum size.
       The value is an initial proposal size, when longer values occur, 
       the field width is adapted. 
   
     * *cr* 
   
       The field is cut at right end to the defined length. 
   
     * *cl* 
   
       The field is cut at start beginning at the defined length. 
   
     * *clip* 
   
       The field is folded to the defined length to the next line 
       at right end. 
   
   
   * **special-content-opt**:
   
     * *fname*
   
       Displays the file path name as the basename only.
       The option *--long* restores the display of the full file path name.
   
     * *fabs*
   
       Displays the file path name as the absolute path name.
   
   
   For example in case of a table::
   
      setup.py setuplib --layout=table --format=name:30,module_name:30:cr,dist.key,dist.location:40:cl
   
   The values of the example are set as:
   
   * *name:30*
     Sets a inital proposal to the variable field length in *auto* mode. 
   
   * *module_name:30:cr*
     The attribute *module_name* in the entry point instance.
     The fixed size if *30*, overflow is cut from the right side.
   
   * *dist.key*
   
     The attribute *dist.key* in the entry point instance.
     The size is adapted to the maximum size of present values.
   
   
   * *dist.location:40:cl*
     The attribute *dist.location* in the entry point instance.
     The fixed size if *40*, overflow is cut from the left side.
   
   It is possible to select special nodes, which are present in some entry points only.
   
   ::
   
      python setup.py setuplib --group=none --format='name,dist._ep_map.console_scripts.virtualenv'
   
   This requires the handling of multiple aspects.
   
   #. First the default behavior in case of missing addressed nodes is to throw an exception.
      This happens here because the command *virtualenv* is present in exactly one entry point only. 
      The behavior is controlled by the option '*--ignore-missing*'. 
      This option suppresses the exception and just ignores missing fields.
      For example::
      
         python setup.py setuplib --format='name,dist._ep_map.console_scripts.virtualenv' --ignore-missing
      
      or short::
      
         python setup.py setuplib --format='name,dist._ep_map.console_scripts.virtualenv' --i
   
   #. This leads to the printout of all nodes, including of those without the addressed node.
      Anyhow, it is in most cases not the target to see all nodes, but the selected one only.
      Thus a filter is required, in order to filter out the entries without *virtualenv*. :: 
      
         python setup.py setuplib --format='name,dist._ep_map.console_scripts.virtualenv' --filter='or;dist._ep_map.console_scripts.virtualenv:;'
      
      In this case the option *--ignore-missing* is no longer required, because the filter 
      pre-selects only the present entry points.
   
   #. Another option is to preselct a :ref:`group <list_entry_points_OPTIONS_group>`, in this case *virtualenv*::
   
         python setup.py setuplib --group=virtualenv --format='name,dist._ep_map.console_scripts.virtualenv'
   
      In this case the not additional filter and ignore options are required, because this group
      contains one item only. ::
      
         python setup.py setuplib --group=virtualenv


.. index::
   pair: group; --group

.. _list_entry_points_OPTIONS_group:

-\-group=
^^^^^^^^^
   Sets the *group* of entry points for scan. 
   See also "Entry points specification" [PYPA]_ and [PEP376]_. ::
   
      group := (
           'none'
         | 'help'
         | <valid-group-name>
      )
      none := "scans for all known groups"
      valid-group-name :=  "valid group name in accrodance to [PEP376]_ and [PYPA]_"
      
      help := "display a list of all present groups, see also '--list-groups'"

      Default: 'distutils.commands'


   Call examples are::
   
      python setup.py setuplib --group=none
      python setup.py setuplib --group=distutils.commands
      python setup.py setuplib --group=console_scripts
      python setup.py setuplib --group=setuplib


.. index::
   pair: ignore-missing; --ignore-missing

.. _list_entry_points_OPTIONS_ignore_missing:

-\-ignore-missing
^^^^^^^^^^^^^^^^^
   Ignore errors due to missing components, and continue.
   For example in case of missing an optional. ::
   
      Default: False.



.. index::
   pair: layout; --layout

.. _list_entry_points_OPTIONS_layout:

-\-layout=
^^^^^^^^^^
   Define display layout.
   See '--format=help'. ::
   
      table, list
      json, xml, yaml, csv


.. index::
   pair: list_groups; --list-groups

.. _list_entry_points_OPTIONS_list_groups:

-\-list-groups=
^^^^^^^^^^^^^^^
   Displays a list of groups with optional registered commands by the additional
   options.
   The standard call displays the current available groups by their names only. ::
   
      python setup.py setuplib --list-groups --long
   
   The option :ref:`--long <list_entry_points_OPTIONS_long>` adds the registered items. ::
   
      python setup.py setuplib --list-groups --long
      python setup.py setuplib --list-groups -l
   
   The repetition of the :ref:`--long / -l <list_entry_points_OPTIONS_long>` option raises the
   adjustment of the output format.
   
   * '-l' simply displays the additional commands
   * '-l -l' displays the additional commands with adjustment to the keys within the group
   * '-l -l -l' displays the additional commands with adjustment to the keys of all groups
   
   
   The same information could be displayed by direct attribute access via the
   :ref:`--format <list_entry_points_OPTIONS_format>` option. ::
   
      python setup.py setuplib --group=none --format='dist._ep_map'
      python setup.py setuplib --group=none --format='dist._ep_map.console_scripts'
      python setup.py setuplib --group=none --format='dist._ep_map.console_scripts.virtualenv'
   
   The display via the :ref:`--format <list_entry_points_OPTIONS_format>` option is
   not recommended, because it accesses the internal data, which is defined
   by a method API. 

.. index::
   pair: long; --long

.. _list_entry_points_OPTIONS_long:

-\-long
^^^^^^^
   List long format, similar to shell command 'ls -l'. ::
   
      --long | -l
      
      Default: off
   
   Supports repetition, which raises the detail level.
   In some cases avoids some mismatches for extremmely different sizes
   of the displayed items, e.g. for table views.

.. index::
   pair: sort; --sort

.. _list_entry_points_OPTIONS_sort:

-\-sort=
^^^^^^^^
   Sort the output data by a specified field name. ::
   
      Default: name

   Examples are::

      --sort=name
      --sort=module_name
      --sort=dist.egg_info
      

.. index::
   pair: build_docx; --verbose

.. _list_entry_points_OPTIONS_verbose:

-\-verbose
^^^^^^^^^^
   Verbose flag for the local command context.
   Each repetition raises the level. 



DESCRIPTION
===========

The call interface *setuplib* provides command line extensions for 
the interface of *setup.py*.

The addressing of common python nodes is based on the library *yapyutils*, for additional
infomation on abstract addressing capabilities of *Python* data structures see [yapydata]_.

The command *setuplib* is registered as an entry point, could be used as an imported class
for local custom classes.


.. _setuplibEXAMPLES:
 

EXAMPLES
========

Some additional call examples.

.. _examples:

   .. parsed-literal::
   
      python setup.py  setuplib --sort=dist.key  --format='name,dist.key,dist._provider.egg_info' --layout=table
      python setup.py  setuplib --sort=dist.key  --format='name,dist.key,dist.egg_info' --layout=table
      python setup.py setuplib --layout=table --format=name,module_name,dist.egg_info:::fname
   
      python setup.py setuplib --group=console_scripts

      python setup.py setuplib --group=console_scripts  --filter='dist.egg_info:Sphinx,module_name:quick'
      python setup.py setuplib --group=console_scripts  --filter='dist.egg_info:Sphinx;and;module_name:quick'
      python setup.py setuplib --group=console_scripts  --filter='dist.egg_info:Sphinx;or;module_name:quick'
      python setup.py setuplib --group=console_scripts  --filter='or;dist.egg_info:Sphinx;module_name:quick'

      python setup.py setuplib --layout=table --format=name:30,module_name:30:cr,dist.key,dist.location:40:cl
      python setup.py setuplib --group=none --format='name,dist._ep_map.console_scripts.virtualenv'
      python setup.py setuplib --format='name,dist._ep_map.console_scripts.virtualenv' --ignore-missing
      python setup.py setuplib --format='name,dist._ep_map.console_scripts.virtualenv' --i
      python setup.py setuplib --format='name,dist._ep_map.console_scripts.virtualenv' --filter='or;dist._ep_map.console_scripts.virtualenv:;'
      python setup.py setuplib --group=virtualenv --format='name,dist._ep_map.console_scripts.virtualenv'
      python setup.py setuplib --group=virtualenv

SEE ALSO
========
   :ref:`Quick Start <QUICKSTART>`, :ref:`setup.py <SETUPPYSRC>`,
   :ref:`setuplib <SETUPLIBCLI>`,
   [setuptools]_, [distutils]_


LICENSE
=======
   :ref:`modified Artistic License <MODIFIED_ARTISTIC_LICENSE_20>` = :ref:`ArtisticLicense20 <ARTISTIC_LICENSE_20>` + :ref:`Peer-to-Peer-Fairplay-amendments <LICENSES_AMENDMENTS>` 

   For configuration files only:
   
      :ref:`MIT License <MIT_LICENSE>` 

COPYRIGHT
=========
   Copyright (C)2019 Arno-Can Uestuensoez @Ingenieurbuero Arno-Can Uestuensoez
