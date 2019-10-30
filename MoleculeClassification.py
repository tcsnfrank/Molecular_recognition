"""
Created on Wed Apr 18 21:17:55 2018
This script is for molecule classification based on analzing the composition and connectivity.
@author: FRANK
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import copy as cp
import json

from setting import *
from functions import *
# Read XYZ datafile into python
# infile=open('wat_800K.lammpstrj','r')
control1=0  # Control read data 
timestep=0
coord=[]    # Coordination data
bdry=[]     #Boundary conditions
crdic={}   #Store every timestep data
file=(input('Please input the trajectory file that you want to process: ') or 'wat1_800K.lammpstrj')
with open(file,'r') as flines:
    for line in flines:
        sline=line.split()
        #  Read the timestep        
        if len(sline)==2 and sline[1]=='TIMESTEP':
            if coord!=[]:
                tsdata={'coord':coord,'boundary':bdry}
                crdic[timestep]=tsdata
                
            timestep=float(next(flines))
            coord=[]
            bdry=[]
        if len(sline)==6 and sline[1]=='BOX':
            xx=next(flines)
            bdry.append([float(xx.split()[0]),float(xx.split()[1])])
            xx=next(flines)
            bdry.append([float(xx.split()[0]),float(xx.split()[1])])
            xx=next(flines)
            bdry.append([float(xx.split()[0]),float(xx.split()[1])])
                        
        if len(sline)==5 and sline[1].isdigit():
            coord.append([int(sline[0]), int(sline[1]),[float(sline[2]), float(sline[3]), float(sline[4])]])
    crdata=pd.Series(crdic)  # All data were stored here.
# Read datafile finished  

####################################################################################################  
# Calculating the connection between atoms
tsdata=[]
bdry=[]
test=0
MolNumData={}
for ts in crdata.index:
    MolNumStep=np.zeros([10,20,10])
#==============================================================================
#     if test>0:    # Just for test control
#         break
#     test+=1      
#==============================================================================
    tsdata=crdata[ts]
    crdf=pd.DataFrame(tsdata['coord'],columns=['id','type','xyz'])
    bdry=pd.DataFrame(tsdata['boundary'],columns=['low','high'])
    bdry['boxsize']=bdry.high-bdry.low
    crdf.sort_values('id',ascending=True,inplace=True)
    crdf = crdf.reset_index(drop=True)
    #  Extracting data for one timestep has finished
    ####  Connectivity calculation begins here
    cntvdat=[]
    for i in crdf.index:
        cntvdat.append([])
    crdf['connection']=cntvdat   #Add a new column for connection
    moldata=[]
    for i in crdf.index:
        moldata.append([])
    crdf['MolId']=moldata  # store MolId
    # calculate box size

    for i in crdf.index:
        for j in range(i+1,len(crdf.index)):
            Bondcut=Bcutdf.loc[AtomType[crdf.iloc[i].type]][AtomType[crdf.iloc[j].type]]
            if distance(np.array(crdf.iloc[i].xyz),np.array(crdf.iloc[j].xyz),bdry.boxsize)<Bondcut:
                crdf.iloc[i].connection.append(j)
                crdf.iloc[j].connection.append(i)
    #### Connectivity calculation finished
    #### Molecules detection begins
    Inmole=[]
    Molecule=[]
    molcnt=0
  #%%%%%
    for i in crdf.index:
        if crdf.iloc[i].MolId==[]:
            schnext=[]   # Collect connected atoms
            for ii in crdf.iloc[i].connection:
                if ii not in schnext:
                    schnext.append(ii)
            Inmole.extend(x for x in schnext if x not in Inmole)
            molcnt+=1
            crdf.at[i,'MolId']=molcnt
            tmp=[]
            while 1:
                for ii in schnext:
                    crdf.at[ii,'MolId']=molcnt
                for ii in schnext:
                    tmp.extend(x for x in crdf.iloc[ii].connection if x not in Inmole)
                Inmole.extend(tmp)
                schnext=cp.deepcopy(tmp)
                if tmp==[]:
                    if Inmole!=[]:
                        Molecule.append([list(set(Inmole)),[0,0,0]])  # Atoms and types count
                    Inmole=[]
                    break
                tmp=[]
    Molecule=pd.DataFrame(Molecule,columns=['Atoms','Types'])
    for i in Molecule.index:
        for ii in Molecule.iloc[i].Atoms:
            Molecule.at[i,'Types'][crdf.at[ii,'type']-1]+=1
        MolNumStep[Molecule.iloc[i].Types[0]][Molecule.iloc[i].Types[1]][Molecule.iloc[i].Types[2]]+=1  # Atom number 1 bgger than index
    Molecule.to_csv('Mol'+str(ts)+'.csv')
    print(Molecule)
    #print(MolNumStep)
    MolNumData[ts]=MolNumStep
    print('Analyzing of timestep: '+str(ts)+'has finished!')

        
            
    #%%%%%%%%
np.save("MolNumData", MolNumData)                   
                
