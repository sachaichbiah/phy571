#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 12 21:18:45 2018

@author: sacha
"""
import xlsxwriter
import os
os.chdir('C:\\Users\\yann\\Documents\\Polytechnique\\Physique\\phy571\\phy571\\codes')

import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.ticker as plticker
from matplotlib import colors
import time
from Grid import *

#Constantes de la simulation
length_cycle =1
nt = 6000
Sizefig=6



# instantiate a configuration
config=Grid(128,1,0.5)
steps = []
clusters = []
SlidingList =[]
length_cycle=1  #servira plus tard pour plotter les fonctions
SlidingLength = 100
n_warmup =2000
"""for i in range(n_warmup) : 
    ClusterMove(
"""
config1=Grid(128,1,0.9)
#initiate figure
fig = plt.figure()
ax = fig.add_subplot(111)

lines =[]

ax.set_xlim(0,config1.size//2)
ax.set_ylim(0,1)



#Warmup
n_warmup =1500
Xaxis=[]
Yaxis=[]


#Write in Excel
workbook = xlsxwriter.Workbook('tailledesClusterssup1.5.xlsx')
worksheet = workbook.add_worksheet()
worksheet.write(0,0, 'Beta')
worksheet.write(0,1, 'MeanCluster')


temperatures = np.arange(1.45,10,1)

liste = []
N_iterations = 1000
for j in range(len(temperatures)) :
    mean = 0
    config=Grid(128,1,temperatures[j])
    Xaxis.append(temperatures[j])
    for i in range(n_warmup) :
        ClusterMove(config)
    
    
    for i in range(N_iterations) :
        mean+=ClusterMove(config)
    mean/=N_iterations
        
    Yaxis.append(mean)



col = 1
for j in range(len(temperatures)) :
    row = 2
    worksheet.write(j+1,0,temperatures[j])
    worksheet.write(j+1,1,Yaxis[j])
    
    
workbook.close()