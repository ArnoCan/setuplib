
.. _QUICKSTART:

***********
Quick Start
***********

Use from the command line call for example by:

   .. parsed-literal::
   
      python setup.py  setuplib --sort=dist.key  --format='name,dist.key,dist._provider.module_path' --layout=table
      python setup.py  setuplib --sort=dist.key  --format='name,dist.key,dist._provider.egg_info' --layout=table
      python setup.py  setuplib --sort=dist.key  --format='name,dist.key,dist.egg_info' --layout=table
      python setup.py setuplib --layout=table --format=name,module_name,dist.egg_info:::fname

      python setup.py setuplib --group=console_scripts
