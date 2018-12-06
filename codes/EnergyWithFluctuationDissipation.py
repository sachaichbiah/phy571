#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 12 21:18:45 2018

@author: sacha
"""


from Grid import *

# instantiate a configuration
sizeGrid=16
Nspins=sizeGrid**2
beta=.1

#Parameters of the simulation
n_cycles=2000
length_cycle=10
n_warmup =1000
n_temperatures=30

Beta=[]
Means =[]
MeansSquare = []

for k in range(n_temperatures):
    Susceptibility =[]
    config=Grid(sizeGrid,1,beta)
    
    for p in range(n_warmup): 
        ClusterMove(config)
        
    E=[]
    Esquare=[]

    for i in range(n_cycles): 
            
        for j in range(length_cycle): 
            ClusterMove(config)
                
        E.append(Calcul_Energy(config)/Nspins)
        Esquare.append((Calcul_Energy(config)/Nspins)**2)
            

    Means.append(np.mean(np.array(E)))
    MeansSquare.append(np.mean(np.array(Esquare)))
    
    Beta.append(beta)
    beta+=.1
    
np.save("ResultsMeanE",Means)
np.save("ResultsMeanESquare, MeansSquare)
np.save("BetaE",Beta)

    

    
