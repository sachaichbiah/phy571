#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 12 21:18:45 2018

@author: sacha
"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.ticker as plticker
from matplotlib import colors
import time
from Grid import *
# instantiate a configuration
SamplePerGrid=10
NumberOfGrids=1
LengthCycle=100
config1_3=Grid(64,1,1.3)
config1_2=Grid(64,1,1.2)
config1_1=Grid(64,1,1.1)
config1=Grid(64,1,1)
liste = [config1,config1_1,config1_2,config1_3]
#initiate figure
fig = plt.figure()
ax = fig.add_subplot(111)

lines =[]

ax.set_xlim(0,config1.size//2)
ax.set_ylim(0,1)



#Warmup
n_warmup =100
Xaxis=[]
Yaxis=[]
for j in range(len(liste)) :
    line, = ax.plot([], [])
    lines.append(line)
    
    for i in range(n_warmup): 
        ClusterMove(liste[j])
    Xaxis.append(np.arange(liste[j].size//2))
    Yaxis.append(Calcul_Correlation(liste[j],SamplePerGrid,NumberOfGrids ,LengthCycle))
    
def animate(i):
    global Yaxis
    for j in range(len(liste)):
        Yaxis[j] += Calcul_Correlation(liste[j],SamplePerGrid,NumberOfGrids,LengthCycle)/(i+1)-Yaxis[j]/(i+1)
   
        lines[j].set_data(Xaxis[j], Yaxis[j])
    return (lines)
    
anim = animation.FuncAnimation(fig, animate, interval=1, blit=False)
