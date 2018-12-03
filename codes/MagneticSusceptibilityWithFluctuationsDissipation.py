#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 12 21:18:45 2018

@author: sacha
"""

import os
os.chdir('C:\\Users\\yann\\Documents\\Polytechnique\\Physique\\phy571\\phy571\\codes')
from Grid import *
from time import time

def do_mc_cycle(n):
    
    for k in range(length_cycle):
        metropolis_move(config)
    
    Angles=config.angles
    U=np.cos(Angles)*1
    V=np.sin(Angles)*1
    ax1.cla()
    Q=(ax1.quiver(U,V))
    data = -(np.cos(Angles-np.roll(Angles,1,1))+np.cos(Angles-np.roll(Angles,-1,1))+np.cos(Angles-np.roll(Angles,1,0))+np.cos(Angles-np.roll(Angles,-1,0)))

    Circulation=np.zeros(Angles.shape)
    DataEnd=np.zeros(Angles.shape)
    size=Angles.shape[0]
    
    Number_Vortices =0
    Number_AntiVortices=0
    
    for i in range(Angles.shape[0]) :
        for j in range(Angles.shape[1]):
                if data[i,j]>-4 :#Plus on ajuste la constante haut, moins on calcule de choses
                    DR=carreDR(Angles,i,j)

                    Circulation[i,j]=Calcul_Circulation(DR)
                    if np.abs(Circulation[i,j])>5  :
                        
                        if Circulation[i,j]>0 : 
                            Number_Vortices+=1
                        else : 
                            Number_AntiVortices+=1
                        DataEnd[i,j]=Circulation[i,j]
                        DataEnd[(i+1)%size,j]=Circulation[i,j]
                        DataEnd[i,(j+1)%size]=Circulation[i,j]
                        DataEnd[(i+1)%size,(j+1)%size]=Circulation[i,j]
                        
                        
    txt = plt.text(size,4.3,'Number of Vortices : '+str(Number_Vortices))
    txt2 = plt.text(size,2.3,'Number of Anti_Vortices : '+str(Number_AntiVortices))
    txt3 = plt.text(size,0.3,'Beta : '+str(config.beta))
    txt4 = plt.text(size,6.3,'J : '+str(config.J))
    txt5 = plt.text(size,8.3,'Number of spins : '+str(size**2))

    data=DataEnd

    ax1.imshow(data, cmap=cmap, norm=norm)
    ax1.set_title('XY spins')
    ax1.grid(which='major', axis='both', linestyle='-', color='w', linewidth=.2)
    ax1.set_xticks(np.arange(-0.5, sizeGrid, 1));
    ax1.set_yticks(np.arange(-0.5, sizeGrid, 1));
    ax1.set_xticklabels([])
    ax1.set_yticklabels([])
    

 

def carreDR(Table,i,j):
    size=len(Table)
    return([Table[i,j],Table[(i+1)%size,j],Table[(i+1)%size,(j+1)%size],Table[i,(j+1)%size]])





# instantiate a configuration
sizeGrid=16
Nspins=sizeGrid**2
length_cycle=3000 #servira plus tard pour plotter les fonctions
n_cycles = 1500
n_warmup =10000
n_configs=3
n_temperatures=30
M=[]

HdeT=[]
HdeT2=[]
Beta=[]
beta=1
Results=[]
ResultsSquare=[]
t1=time()
for k in range(n_temperatures):
    Susceptibility =[]
    Means =[]
    MeansSquare = []
    h=.4
    for l in range(n_configs):
        print(beta,k,h,l)
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
            
            
        print((time()-t1)/60)
        Means.append(np.mean(np.array(M)))
        MeansSquare.append(np.mean(np.array(Msquare)))
        
        h+=.1
        
    Results.append(Means)
    ResultsSquare.append(MeansSquare)
    
        
    
    Beta.append(beta)
    beta+=.01
    
np.save("Results2",Results)
np.save("ResultsSquare2", ResultsSquare)
np.save("Beta2",Beta)

    

    
#ani.save('2osc.mp4', writer="ffmpeg")


"""
def carreUR(Table,i,j):
    size=len(Table)
    return([Table[i-1,j],Table[i,j],Table[i,(j+1)%size],Table[i-1,(j+1)%size]])

def carreUL(Table,i,j):
    return([Table[i-1,j-1],Table[i,j-1],Table[i,j],Table[i-1,j]])
def carreDL(Table,i,j):
    size=len(Table)
    return([Table[i,j-1],Table[(i+1)%size,j-1],Table[(i+1)%size,j],Table[i,j]])
    
    
Clist=[]

#Reglage des couleurs
Contrast_constant=0.9
Clist=[]

A=(np.linspace(0.6,1,10)-0.1)*Contrast_constant
B=(np.linspace(1,1,10)-0.1)*Contrast_constant
C=(np.linspace(0.6,1,10)-0.1)*Contrast_constant
for i in range(10): 
    Clist.append((A[i],B[i],C[i]))

A=(np.linspace(1,0.6,10)-0.1)*Contrast_constant
B=(np.linspace(1,0.6,10)-0.1)*Contrast_constant
C=(np.linspace(1,1,10)-0.1)*Contrast_constant
for i in range(10): 
    Clist.append((A[i],B[i],C[i]))
    

cmap = colors.ListedColormap(Clist)
bounds=np.linspace(-6,6,20)
"""