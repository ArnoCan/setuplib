
*********
Blueprint
*********

.. _REFERENCE_ARCHITECTURE:

The modern landscapes of information infrastructures are commonly designed 
and organized as stacks of heterogeneous runtime environments
with comon frameworks.
This frequently requires the installation of specific components for various
platforms, including the generation of adapted packages, extended documentation,
and the automation of distributed large-scale tests.
The *setupdocxs* extends the *setuptools* for the required commands and options.

.. only:: singlehtml

   .. container:: figabstract
   
      .. figurewrap:: _static/setuplib-architecture.png
         :width-singlehtml: 250
         :target-html: _static/setuplib-architecture.png
         :align: center
         
      Figure: SetupLib Integration


.. only:: not singlehtml

   .. figurewrap:: _static/setuplib-architecture.png
      :width: 250
      :target-html: _static/setuplib-architecture.png
      :align: center
      
      Figure: SetupLib Integration

* Display comprehensive information on Python distributions, packages, and entrypoints: 

   .. parsed-literal::
   
      python :ref:`setup.py <SETUPPYSRC>` :ref:`setuplib <setuplibSETUPLIB>`
      