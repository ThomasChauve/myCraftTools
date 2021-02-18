# myCraftTools
This reposirotory contain CraFT tools to performed simulation

The tools are meant to be use in commandeline. paraview python should be installed.
export PATH="mylocalpath/myCraftTools/myCraftTools:$PATH"

To be able to execute the script you should make the files in myCraftTols executable
chmod 755 neper2craft.py

Function :
**neper2craft.py**
neper2craft.py is converting a neper microstructure generation to a craft microstructure input file.
It should be use in the terminal :
neper2craft.py neper_micro.vtk
