
.. _QUICKSTART:

***********
Quick Start
***********
The commandline interface *list_entry_points* displays information about current accessible
entry points.
This includes various options for filtering and custom output layouts.

The standard default call prints a list including module names:
 
.. parsed-literal::

   python setup.py list_entry_points

The option :ref:`--long <list_entry_points_OPTIONS_long>` or :ref:`-l <list_entry_points_OPTIONS_long>` displays the full path names of the actual filesystem location:
 
.. parsed-literal::

   python setup.py list_entry_points :ref:`--long <list_entry_points_OPTIONS_long>`
   python setup.py list_entry_points:ref:`-l <list_entry_points_OPTIONS_long>`

The current available *groups* [PYPA]_ can be displayed by:
 
.. parsed-literal::

   python setup.py list_entry_points :ref:`--group=help <list_entry_points_OPTIONS_group>`

or with details and optional filtering:

.. parsed-literal::

   python setup.py list_entry_points :ref:`--list-groups <list_entry_points_OPTIONS_list_groups>`           # group names
   python setup.py list_entry_points :ref:`--list-groups <list_entry_points_OPTIONS_list_groups>` -l        # 1x adds commands 
   python setup.py list_entry_points :ref:`--list-groups <list_entry_points_OPTIONS_list_groups>` -l -l     # 2x adds adjusted groups
   python setup.py list_entry_points :ref:`--list-groups <list_entry_points_OPTIONS_list_groups>` -l -l -l  # 3x adds adjusted over all groups 
 
The current available console scripts [PYPA]_ could be easily listed by:
 
.. parsed-literal::

   python setup.py list_entry_points --group=console_scripts
   python setup.py list_entry_points --group=console_scripts -l  # displays the full path name

The layout of the output display of the data could be selected by the :ref:`--layout <list_entry_points_OPTIONS_layout>` option.
Current release supports *list* and *table*, soon available are more such as *JSON*, *XML*, *YAML*,
*CSV*, *INI*, and *.properties*.
 
.. parsed-literal::

   python setup.py list_entry_points :ref:`--layout=list <list_entry_points_OPTIONS_layout>`
   python setup.py list_entry_points :ref:`--layout=list <list_entry_points_OPTIONS_layout>`

The additional parameter defining the details of the selected layout is the option :ref:`--format <list_entry_points_OPTIONS_format>`.
The format option defines the actual seletion of the resulting display.
It supports for the selction of arbitrary addressable *Pyhton* data nodes as supported
by the namebinding package *yapydata* with the subpackage *yapydata.datatree* [yapydata]_.

The specified node addresses are relative to the *EntryPoint* objects as provided by
*pkg_resource* interface.
The address is specified as a string in common ordinary dottet path notation.
The nodes may include arbitrary Python nodes such as standard data types and 
custom classes.
These could be intermixed list indexes, dictionary keys, object attrbutes for branches
with intermediate path nodes, and any type for terminal nodes as leafs.

.. parsed-literal::

   dist._provider.egg_info
   dist._provider.module_path
   dist.egg_info
   dist.key
   dist.key,dist.egg_info
   module_name
   name

The application examples are:

.. parsed-literal::

   python setup.py  list_entry_points --format='name,dist.key,dist._provider.module_path' --layout=table
   python setup.py  list_entry_points --format='name,dist.key,dist._provider.egg_info' --layout=table
   python setup.py  list_entry_points --format='name,dist.key,dist.egg_info' --layout=table
   python setup.py list_entry_points --layout=table --format=name,module_name,dist.egg_info:::fname
   python setup.py list_entry_points --layout=table --format=name,module_name,dist.egg_info:::fname --long

For further details *yapydata* [yapydata]_, and 
the options specification see :ref:`--format <list_entry_points_OPTIONS_format>`.

The presented order could be sorted for any valid field by the option :ref:`--sort=dist.key <list_entry_points_OPTIONS_sort>`:

.. parsed-literal::

   python setup.py  list_entry_points :ref:`--sort=dist.key <list_entry_points_OPTIONS_sort>` --format='name,dist.key,dist._provider.module_path' --layout=table
   python setup.py  list_entry_points :ref:`--sort=dist.key <list_entry_points_OPTIONS_sort>`  --format='name,dist.key,dist._provider.egg_info' --layout=table
   python setup.py  list_entry_points :ref:`--sort=dist.key <list_entry_points_OPTIONS_sort>`  --format='name,dist.key,dist.egg_info' --layout=table



The scanned data from *pkg_resource* could be further reduced by the option :ref:`--filter <list_entry_points_OPTIONS_filter>`.
The filter provides *Python* regular expressions to be used by the interface *re.compile()*, and is applied here with 
the *re.search()* interface.
Therefore the nodes are converted to strings by *str*.
The search is required, due to the possible replacements by custom *__str__*, which provide basically unreliable formats of node information.
Thus positional regular expressions should be avoided for generic access.
In case of well known nodes no restrictions exist.   
For detailed information refer to the option :ref:`--filter <list_entry_points_OPTIONS_filter>`.

.. parsed-literal::

   python setup.py list_entry_points --group=console_scripts  --filter='dist.egg_info:Sphinx,module_name:quick'
   python setup.py list_entry_points --group=console_scripts  --filter='dist.egg_info:Sphinx;and;module_name:quick'
   python setup.py list_entry_points --group=console_scripts  --filter='dist.egg_info:Sphinx;or;module_name:quick'
   python setup.py list_entry_points --group=console_scripts  --filter='or;dist.egg_info:Sphinx;module_name:quick'

The option supports access to any native member, which is one of the data bindings and thus could be addresses
by attribute-access, index-access, or key-access.
This includes marked private internal data, which is not reliable, but in some cases the only-and-one
possibility to get the information.
The following demonstrates the access to *console_scripts* of the groups *virtualenv*.

.. parsed-literal::

   python setup.py list_entry_points --format='name,dist._ep_map.console_scripts.virtualenv' --filter='or;dist._ep_map.console_scripts.virtualenv:;'
   python setup.py list_entry_points --group=virtualenv --format='name,dist._ep_map.console_scripts.virtualenv'
   python setup.py list_entry_points --group=virtualenv


      