#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 24 10:08:55 2018
This is for plotting and data collecting.
@author: Jie Zhang
"""

import numpy as np
import matplotlib.pyplot as plt
MolNumData=np.load('MolNumData.npy').item()
k=str(input('Please input the Chemical Formula of the molecule that you want to count: \
            For example: 1 2 3 for B1H2N3:')).split()
TimeStep=[]
Number=[]
for i in MolNumData.keys():
    TimeStep.append(int(i))
    Number.append(MolNumData[i][int(k[0])][int(k[1])][int(k[2])])
plt.figure(figsize=(10,9))
SMALL_SIZE = 24
MEDIUM_SIZE = 24
BIGGER_SIZE = 28
title_font = {'fontname':'Arial', 'size':'26', 'color':'black', 'weight':'normal',
              'verticalalignment':'bottom'} # Bottom vertical alignment for more space
axis_font = {'fontname':'Arial', 'size':'28'}

plt.rc('font', size=SMALL_SIZE)          # controls default text sizes
plt.rc('axes', titlesize=SMALL_SIZE)     # fontsize of the axes title
plt.rc('axes', labelsize=MEDIUM_SIZE)    # fontsize of the x and y labels
plt.rc('xtick', labelsize=SMALL_SIZE)    # fontsize of the tick labels
plt.rc('ytick', labelsize=SMALL_SIZE)    # fontsize of the tick labels
plt.rc('legend', fontsize=SMALL_SIZE)    # legend fontsize
plt.rc('figure', titlesize=BIGGER_SIZE)  # fontsize of the figure title
plt.xlabel(r"Timestep (step)")
plt.ylabel("Number of molecules (1)")
plt.title("Timestep - Molecule NO.",fontweight="bold")
plt.legend(loc='best',numpoints=1)
line1,=plt.plot(TimeStep,Number,'ok',label="Number of molecules N%dH%dB%d"%(int(k[0]),int(k[1]),int(k[2])))
first_legend = plt.legend(handles=[line1])

plt.savefig('Timestep - Molecule NO.png')
plt.show()
