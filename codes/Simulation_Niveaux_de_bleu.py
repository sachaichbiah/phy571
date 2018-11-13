#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 12 21:18:45 2018

@author: sacha
"""

import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.ticker as plticker
from matplotlib import colors
import time
from Grid import *

#Reglage des couleurs
Contrast_constant=0.9
Clist=[]
A=(np.linspace(1,0.5,10)-0.1)*Contrast_constant
B=(np.linspace(1,0.7,10)-0.1)*Contrast_constant
C=(np.linspace(1,0.8,10)-0.1)*Contrast_constant
for i in range(10): 
    Clist.append((A[i],B[i],C[i]))
cmap = colors.ListedColormap(['0.9']+Clist)
bounds = np.linspace(-4,4,11)
norm = colors.BoundaryNorm(bounds, cmap.N)


#Constantes de la simulation
length_cycle =100
nt = 200
Sizefig=6


# instantiate a configuration
config=Grid(20,1,5)
Angles=config.angles
U=np.cos(Angles)*2
V=np.sin(Angles)*2
fig,ax1=plt.subplots(figsize=(Sizefig, Sizefig))
ax1.set_title('XY spins')
Q = ax1.quiver(U, V, units='width',minshaft = 1, minlength = 1, color = 'k')

length_cycle=50  #servira plus tard pour plotter les fonctions
n_cycles = 10000
n_warmup =10000
for i in range(n_warmup): 
    metropolis_move(config)


def do_mc_cycle(n):
    
    for k in range(length_cycle):
        metropolis_move(config)
    
    Angles=config.angles
    U=np.cos(Angles)*1
    V=np.sin(Angles)*1
    ax1.cla()
    Q=(ax1.quiver(U,V))
    
    data = -(np.cos(Angles-np.roll(Angles,1,1))+np.cos(Angles-np.roll(Angles,-1,1))+np.cos(Angles-np.roll(Angles,1,0))+np.cos(Angles-np.roll(Angles,-1,0)))
    
    
    
    ax1.imshow(data, cmap=cmap, norm=norm)
    # draw gridlines
    ax1.set_title('XY spins')
    ax1.grid(which='major', axis='both', linestyle='-', color='w', linewidth=2)
    ax1.set_xticks(np.arange(-0.5, 20, 1));
    ax1.set_yticks(np.arange(-0.5, 20, 1));
    ax1.set_xticklabels([])
    ax1.set_yticklabels([])
    
    



    """
 #to set the grid    
    intervals = float(1)
    loc = plticker.MultipleLocator(base=intervals)
    ax1.xaxis.set_major_locator(loc)
    ax1.yaxis.set_major_locator(loc)
    ax1.grid(which='major', axis='both', linestyle='-')
    ax1.set_xticklabels([])
    ax1.set_yticklabels([])"""

    
    
    time.sleep(1) #To control the time, maybe delete it later
    
    
    return (Q)

ani = animation.FuncAnimation(fig, do_mc_cycle, interval=100, blit=False)
