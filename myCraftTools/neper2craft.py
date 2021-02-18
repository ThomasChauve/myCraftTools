#!/usr/bin/env python
from paraview.simple import *
import sys
import os

for arg in sys.argv:
    print(arg)

r = LegacyVTKReader( FileNames=[arg] )
SaveData(arg, proxy=r, FileType='Ascii')
com1="sed -i 's/CELL_DATA/POINT_DATA/' "+arg
os.system(com1)
com2="sed -i 's/SCALARS MaterialId short/SCALARS scalars float/' "+arg
os.system(com2)

fp = open(arg)
for i, line in enumerate(fp):
    if i == 4:
        break
fp.close()

split_line=line.split()
for i in [1,2,3]:
    split_line[i]=str(int(float(split_line[i])-1))

  
replace_line=split_line[0]+' '+split_line[1]+' '+split_line[2]+' '+split_line[3]
com3="sed -i 's/"+line[0:-1]+"/"+replace_line+"/' "+arg
os.system(com3)
