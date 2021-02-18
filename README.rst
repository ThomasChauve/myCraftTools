myCraftTools
============

This reposirotory contain CraFT tools to performed simulation.

It has been tested to run using python 3.7

Dependancy : 
************

1. paraview-python should be installed.


Installation :
**************

You can clone the git repository :

.. code:: bash

    git clone https://github.com/ThomasChauve/myCraftTools

The folder should be in the .bashrc or .bash_profil of your system

.. code:: bash

    export PATH="mylocalpath/myCraftTools/myCraftTools:$PATH"

To be able to execute the script you should make the files in myCraftTols executable

.. code:: bash

    chmod 755 neper2craft.py
    chmod 755 craft_ice_input.py

Functions list :
****************

**neper2craft.py**

neper2craft.py is converting a neper microstructure generation to a craft microstructure input file.

.. code:: bash

    neper2craft.py neper_micro.vtk
    
**craft_ice_input.py**

craft_ice_input.py is helping you to create all craft input file

.. code:: bash

    craft_ice_input.py
