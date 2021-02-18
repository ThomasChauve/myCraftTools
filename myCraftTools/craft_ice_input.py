#!/usr/bin/env python3
import sys
import os
import datetime

print('Welcome to craft input generator v0.1')
print('####################################')
# Find the vtk and input file
cwd = os.getcwd()
file=os.listdir(cwd)
for ifile in file:
    if ifile[-3::]=='vtk':
        print('Find VTK file : '+ifile)
        vtk_file=ifile
    elif ifile[-5::]=='phase':
        print('Find phase file : '+ifile)
        phase_file=ifile
        
if len(vtk_file)==0:
    print('Break : No vtk file in this folder')
elif len(phase_file)==0:
    print('Break : No phase file in this folder')
else:
    print('####################################')
    print('######### Simulation name ##########')
    print('####################################')
    name_simu = str(input())
            
    print('####################################')
    print('##### Start writing load file ######')
    print('####################################')

    imp_cond = str(input('Loading condation (S-stress direction imposed, C-stress imposed (default), D-Strain imposed) : '))
    if len(imp_cond)==0:
        imp_cond='C'

    print('------------------------------------')
    print('Give the strain or stress tensor wanted')
    tensor=str(input('t11 t22 t33 t12 t13 t23 (default "0 -0.5 0 0 0 0") : '))

    if len(tensor)==0:
        tensor='0 -0.5 0 0 0 0'
        
    out_load=open(name_simu + '.load','w');
    out_load.write('#------------------------------------------------------------\n')
    out_load.write('# Date ' + str(datetime.date.today()) + '      Manip: ' + name_simu + '\n')
    out_load.write('#------------------------------------------------------------\n')
    out_load.write('# choix du type de chargement \n')
    out_load.write('# direction contrainte imposée: S \n')
    out_load.write('# contrainte imposée:          C \n')
    out_load.write('# déformation imposée:         D \n')
    out_load.write(imp_cond+'\n')
    out_load.write('#------------------------------------------------------------\n')
    out_load.write('# nb de pas    temps        direction            facteur\n')
    out_load.write('#                            11 22 33 12 13 23\n')
    print('------------------------------------')
    print('Time end is the number for the end of this loading path.')
    print(' ')
    print('Time step is the incremental time step to reach Time end.')

    step=2
    while step!=0:
        if step!=2:
            out_load.write(nb_pas+'           '+time_end+'            '+tensor+'    1\n')
        
        step=str(input('Do you want add one loading line ? (0-no,1-yes,default 1) : '))
        if len(step)==0:
            step=1
        else:
            step=int(step)
        
        if step!=0:
            time_end=str(input('Time end : '))
            nb_pas=str(input('Time step : (deault,only one step, %2% time step =2 ) : '))
            if len(nb_pas)==0:
                nb_pas='     '
        
        


    out_load.write('#\n')
    out_load.write('#------------------------------------------------------------\n')
    out_load.close()

    print('####################################')
    print('#### Start writing output file #####')
    print('####################################')
    add_hdf5 = int(input('Add hdf5 backup (0-no/1-yes) : '))

    print('There is different way to enter the time step you want to save.')
    print('------------------------------------')
    print('10.,20, 30.:40.:@2, 45.:@100')
    print('Point files at times: t = 10s, t = 20s, once at every two time steps between t = 30s and t = 40s, at every time steps between t = 45s and the 100th steps')
    print('------------------------------------')
    print('begin:end:@10')
    print('Point files once at every ten time steps between the beginning and the end of the loading path')
    print('------------------------------------')
    time_step_save = str(input('Enter the time step you want to save (empty - only last one) : '))


    if len(time_step_save)=='0':
        time_step_save=''

    out_output=open(name_simu + '.output','w')
    out_output.write('#------------------------------------------------------------\n')
    out_output.write('# Date ' + str(datetime.date.today()) + '      Manip: ' + name_simu + '\n')
    out_output.write('#------------------------------------------------------------\n')
    out_output.write('generic name='+name_simu+'\n')
    out_output.write('im_format=vtk\n')
    out_output.write('#------------------------------------------------------------\n')
    out_output.write('equivalent stress image = yes '+time_step_save+'\n')
    out_output.write('equivalent strain image = yes '+time_step_save+'\n')
    out_output.write('#\n')
    out_output.write('stress image = yes '+time_step_save+'\n')
    out_output.write('strain image = yes '+time_step_save+'\n')
    out_output.write('#\n')
    out_output.write('backstress image = yes '+time_step_save+'\n')
    out_output.write('#\n')
    out_output.write('gamma image = yes '+time_step_save+'\n')
    out_output.write('#\n')
    out_output.write('rotation image = yes '+time_step_save+'\n')
    out_output.write('#\n')
    if add_hdf5:
        out_output.write('variables = yes '+time_step_save+'\n')
        

    out_output.close() 

    print('####################################')
    print('##### Start writing input file #####')
    print('####################################')

    out_in=open(name_simu + '.in','w');
    out_in.write('#------------------------------------------------------------\n')
    out_in.write('# Date ' + str(datetime.date.today()) + '      Manip: ' + name_simu + '\n')
    out_in.write('#------------------------------------------------------------\n')
    out_in.write('#\n')
    out_in.write('#\n')
    out_in.write('#------------------------------------------------------------\n')
    out_in.write('# name of the file of the image of the microstructure\n')
    out_in.write('microstructure=../'+ vtk_file+'\n')
    out_in.write('#\n')
    out_in.write('#------------------------------------------------------------\n')
    out_in.write('# name of the file of the description of phases\n')
    out_in.write('phases=../'+phase_file+'\n')
    out_in.write('#\n')
    out_in.write('#------------------------------------------------------------\n')
    out_in.write('# name of the file describing the materials the phases are made of:\n')
    out_in.write('materials=../glace3_oc2_5mai2011.mat\n')
    out_in.write('#\n')
    out_in.write('#------------------------------------------------------------\n')
    out_in.write('# file of the loading conditions:\n')
    out_in.write('loading=../'+name_simu + '.load\n')
    out_in.write('#\n')
    out_in.write('#------------------------------------------------------------\n')
    out_in.write('# file telling the outputs one wants to obtain:\n')
    out_in.write('output=../' +name_simu + '.output\n')
    out_in.write('#\n')
    out_in.write('#------------------------------------------------------------\n')
    out_in.write('# The parameter C0 has to be set by craft:\n')
    out_in.write('C0=auto\n')
    out_in.write('#\n')
    out_in.write('#------------------------------------------------------------\n')
    out_in.write('# # required precision for equilibrium and for loading conditions:\n')
    out_in.write('precision=1.e-4, 1.e-4\n')
    out_in.write('#------------------------------------------------------------\n')
    out_in.close()

    print('####################################')
    print('#### Start oar file for gricad #####')
    print('####################################')

    gricad_proj=str(input('Whats is the gricad project on which you want to run the simulation (default, rheolefice) : '))
    if len(gricad_proj)==0:
        gricad_proj='rheolefice'
    print('------------------------------------')
    nb_cpu=str(input('How many cpu do you want (default, 32) : '))
    if len(nb_cpu)==0:
        nb_cpu='32'
    print('------------------------------------')
    time_cpu=str(input('How long is the simulation (hh:mm:ss - default, 48:00:00 (max)) : '))
    if len(time_cpu)==0:
        time_cpu='48:00:00'
    print('------------------------------------')
    path_gricad=str(input('Path to gricad folder (default /bettik/chauvet/CraFT_Run/):'))
    if len(path_gricad)==0:
        path_gricad='/bettik/chauvet/CraFT_Run/'


    os.mkdir('output')
    out_oar=open('output/'+ name_simu + '.oar','w');
    out_oar.write('#!/bin/bash \n')
    out_oar.write('#OAR -n '+ name_simu +'\n')
    out_oar.write('#OAR -O '+ name_simu +'.%jobid%.o\n')
    out_oar.write('#OAR -E '+ name_simu +'.%jobid%.e\n')
    out_oar.write('#OAR --project '+ gricad_proj +'\n')
    out_oar.write('#OAR -l nodes=1/core='+nb_cpu+',walltime='+time_cpu+'\n')
    out_oar.write('\n')
    out_oar.write('cd '+ path_gricad +'\n')
    out_oar.write('\n')
    out_oar.write('source /applis/site/guix-start.sh \n')
    out_oar.write('refresh_guix craft1.1.0 \n')
    out_oar.write('\n')
    out_oar.write('/bettik/PROJECTS/pr-rheolefice/Software/craftIce/bin/craft -v -n '+nb_cpu+' -f ../'+name_simu+'.in')

    com1='chmod 777 output/'+name_simu+'.oar'
    os.system(com1)
    print('####################################')
    print('######### Input file ready #########')
    print('####################################')
