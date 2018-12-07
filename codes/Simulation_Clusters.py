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
Contrast_constant=1
Clist=[]
A=(np.linspace(1,0.2,10))*Contrast_constant
B=(np.linspace(0.2,0.2,10))*Contrast_constant
C=(np.linspace(0.2,1,10))*Contrast_constant
for i in range(10): 
    Clist.append((A[i],B[i],C[i]))
cmap = colors.ListedColormap(np.concatenate((Clist,np.flip(Clist,0)),axis=0))
bounds = np.linspace(0,2*np.pi,20)
norm = colors.BoundaryNorm(bounds, cmap.N)


#Constantes de la simulation
length_cycle =1
nt = 200
Sizefig=6


# instantiate a configuration
config=Grid(128,1,1.7)
Angles=config.angles
U=np.cos(Angles)*2
V=np.sin(Angles)*2
fig=plt.figure(figsize=(Sizefig, Sizefig))

ax1=fig.add_subplot(121, aspect=100)
ax1.set_title('XY spins')
ax2 = fig.add_subplot(122, aspect=100)
line, = ax2.plot([],[])
ax2.set_xlim(0,nt)
ax2.set_ylim(-1,1)
steps = []
clusters = []
length_cycle=1  #servira plus tard pour plotter les fonctions
n_cycles = 10000
n_warmup =500
for i in range(n_warmup): 
    ClusterMove(config)


def do_mc_cycle(n):
    
    for k in range(length_cycle):
        metropolis_move(config)
    
    Angles=config.angles
    U=np.cos(Angles)*1
    V=np.sin(Angles)*1
    ax1.cla()    
    data = Angles%(2*np.pi)    
    
    
    ax1.imshow(data, cmap=cmap, norm=norm)
    # draw gridlines
    ax1.set_title('XY spins')
    ax1.grid(which='major', axis='both', linestyle='-', color='w', linewidth=0)
    ax1.set_xticks(np.arange(-0.5, 20, 1));
    ax1.set_yticks(np.arange(-0.5, 20, 1));
    ax1.set_xticklabels([])
    ax1.set_yticklabels([])
    
    if n%20==0 : 
        config.beta+=-0.005
        for k in range(100): 
            metropolis_move(config)
        print(config.beta)
    
def do_cm_cycle(n):
    
    for k in range(length_cycle):
        taille = np.sqrt(ClusterMove(config))/float(config.size)
    
    Angles=config.angles
    U=np.cos(Angles)*1
    V=np.sin(Angles)*1
    ax1.cla()    
    data = Angles%(2*np.pi)    
    
    
    ax1.imshow(data, cmap=cmap, norm=norm)
    # draw gridlines
    ax1.set_title('XY spins')
    ax1.grid(which='major', axis='both', linestyle='-', color='w', linewidth=0)
    ax1.set_xticks(np.arange(-0.5, 20, 1));
    ax1.set_yticks(np.arange(-0.5, 20, 1));
    ax1.set_xticklabels([])
    ax1.set_yticklabels([])
    

    

    
    if len(steps) < nt: steps.append(n)
    if len(clusters) < nt:
        clusters.append(taille)
        
    if len(clusters) >= nt:
        clusters.append(taille)
        clusters.pop(0)
    line.set_data(steps,clusters)
    """
    if n%20==0 : 
        config.beta+=-0.005
        for k in range(100): 
            metropolis_move(config)
        print(config.beta)    """

    return(line)

    """
 #to set the grid    
    intervals = float(1)
    loc = plticker.MultipleLocator(base=intervals)
    ax1.xaxis.set_major_locator(loc)
    ax1.yaxis.set_major_locator(loc)
    ax1.grid(which='major', axis='both', linestyle='-')
    ax1.set_xticklabels([])
    ax1.set_yticklabels([])"""


    
    #time.sleep(0.1) #To control the time, maybe delete it later
    
    
    
ani = animation.FuncAnimation(fig, do_cm_cycle, interval=1, blit=False)
