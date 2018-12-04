#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 12 21:18:45 2018

@author: sacha
"""


from Grid import *
   
from time import time




# instantiate a configuration
sizeGrid=16
Nspins=sizeGrid**2
length_cycle=3000 #servira plus tard pour plotter les fonctions
n_cycles = 4500
n_warmup =10000
n_configs=1
n_temperatures=30


Beta=[]
beta=3
Means =[]
MeansSquare = []
t1=time()
for k in range(n_temperatures):
    Susceptibility =[]

    h=.5

    print(beta,k,h)
    M=[]
    Msquare=[]
    config=Grid(sizeGrid,1,beta,np.array([h,0]))
    for i in range(n_warmup): 
        metropolis_move(config)

    for i in range(n_cycles): 
        for j in range(length_cycle): 
            metropolis_move(config)
        M.append(config.magnetization[0]/Nspins)
        Msquare.append((config.magnetization[0]/Nspins)**2)
        print(i)
            
            
    print((time()-t1)/60)
    Means.append(np.mean(np.array(M)))
    MeansSquare.append(np.mean(np.array(Msquare)))
        
        
    
    Beta.append(beta)
    beta+=1
    
np.save("Results2Magnetization",Means)
np.save("ResultsSquare2Magnetization", MeansSquare)
np.save("Beta2Magnetization",Beta)
