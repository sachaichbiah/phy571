#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 12 21:18:45 2018

@author: sacha
"""

import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.ticker as plticker
import time
from Grid import *




length_cycle =100
nt = 200
Sizefig=6

# instantiate a configuration
config=Grid(20,1,1)
Angles=config.angles
U=np.cos(Angles)*2
V=np.sin(Angles)*2
fig,ax1=plt.subplots(figsize=(Sizefig, Sizefig))


#fig = plt.figure(figsize=(10,5))
#ax1 = fig.add_subplot()
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
    U=np.cos(Angles)*2
    V=np.sin(Angles)*2
    ax1.cla()
    Q=(ax1.quiver(U,V))
    
    
    #to set the grid    
    intervals = float(1)
    loc = plticker.MultipleLocator(base=intervals)
    ax1.xaxis.set_major_locator(loc)
    ax1.yaxis.set_major_locator(loc)
    ax1.grid(which='major', axis='both', linestyle='-')
    ax1.set_xticklabels([])
    ax1.set_yticklabels([])
    
    
    time.sleep(.1) #To control the time, maybe delete it later
    
    
    return (Q)

ani = animation.FuncAnimation(fig, do_mc_cycle, interval=100, blit=False)


