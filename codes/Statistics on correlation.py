#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 12 21:18:45 2018

@author: sacha
"""
import xlsxwriter
import os
os.chdir('C:\\Users\\yann\\Documents\\Polytechnique\\Physique\\phy571\\phy571\\codes')
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.ticker as plticker
from matplotlib import colors
import time
from Grid import *
# instantiate a configuration
SamplePerGrid=20
NumberOfGrids=1
LengthCycle=5

config1=Grid(64,1,0.9)
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


#anim = animation.FuncAnimation(fig, animate, interval=1, blit=False)
#Write in Excel
workbook = xlsxwriter.Workbook('Correlations64basseT1.xlsx')
worksheet = workbook.add_worksheet()
worksheet.write(0,0, 'Beta')


temperatures = np.arange(3,35,5)
#temperatures=np.concatenate((temperatures,np.arange(0.5,1,0.1),np.arange(1.2,1.7,0.1),np.arange(1.7,6,0.5)))
#temperatures.sort()
#temperatures = temperatures[13:20]
liste = []
N_iterations = 100
for j in range(len(temperatures)) :
    line, = ax.plot([], [])
    lines.append(line)
    config=Grid(64,1,temperatures[j])
    for i in range(n_warmup) :
        ClusterMove(config)
    liste.append(config)
    Xaxis.append(np.arange(liste[j].size//2))

    Yaxis.append(Calcul_Correlation(liste[j],SamplePerGrid,NumberOfGrids ,LengthCycle))
for i in range(N_iterations) :
    for j in range(len(liste)) :

        Yaxis[j]+= Calcul_Correlation(liste[j],SamplePerGrid,NumberOfGrids,LengthCycle)/(i+1)-Yaxis[j]/(i+1)


col = 1
for j in range(len(temperatures)) :
    row = 2
    worksheet.write(0,j+1,temperatures[j])
    for i in Yaxis[j] :
        worksheet.write(row,j+1,i)
        row+=1
for j in range(len(liste)) :
    lines[j].set_data(Xaxis[j], Yaxis[j])
    
plt.show()

workbook.close()


    

#direct calcul:
