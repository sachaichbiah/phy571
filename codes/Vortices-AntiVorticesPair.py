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

def Calcul_Circulation(Table): 
    Circulation=0
    count=0
    for i in range(len(Table)):
        if Table[i]>np.pi : 
            Table[i]-=2*np.pi
    for n in range(len(Table)):
        
        alpha=Table[(n+1)%len(Table)]-Table[n]
        
        if alpha>np.pi:
            
            alpha=-2*np.pi+alpha
        if alpha <-np.pi : 
            alpha+=2*np.pi
        
        
        Circulation+=(alpha)

    return(Circulation)       


Clist=[]
#Reglage des couleurs
A=np.linspace(0.7,1,11)
B=A.copy()
B=np.flip(B,0)
for i in range(len(B)): 
    Clist.append(str(B[i]))
for i in range(len(A)): 
    Clist.append(str(A[i]))
cmap = colors.ListedColormap(Clist)
bounds=np.linspace(6,-6,22)


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
#bounds =np.array([-4,-3.2,-2.4,-1.6,-0.8,0,0.8,1.6,2.4,3.2,4])+4
norm = colors.BoundaryNorm(bounds, cmap.N)


#Constantes de la simulation
length_cycle =100
nt = 200
Sizefig=6
sizeGrid=40


# instantiate a configuration
config=Grid(sizeGrid,1,40)
Angles=config.angles
U=np.cos(Angles)*2
V=np.sin(Angles)*2
fig,ax1=plt.subplots(figsize=(Sizefig, Sizefig))
ax1.set_title('XY spins')
Q = ax1.quiver(U, V, units='width',minshaft = 1, minlength = 1, color = 'k')

length_cycle=5000  #servira plus tard pour plotter les fonctions
n_cycles = 10000
n_warmup =100000
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
    #Pour Data: Valeur haute: C est fonce, valeur basse, c est clair. D ou le signe -au debut
    #data = -(np.cos(Angles-np.roll(Angles,1,1))+np.cos(Angles-np.roll(Angles,-1,1))+np.cos(Angles-np.roll(Angles,1,0))+np.cos(Angles-np.roll(Angles,-1,0)))
    data = -(np.cos(Angles-np.roll(Angles,1,1))+np.cos(Angles-np.roll(Angles,-1,1))+np.cos(Angles-np.roll(Angles,1,0))+np.cos(Angles-np.roll(Angles,-1,0)))

    Circulation=np.zeros(Angles.shape)
    DataEnd=np.zeros(Angles.shape)
    size=Angles.shape[0]
    
    Number_Vortices =0
    Number_AntiVortices=0
    
    for i in range(Angles.shape[0]) :
        for j in range(Angles.shape[1]):
            if True : #Visited[i,j]==0:
                #-1 : Constante a changer, valeur variant de 0 a -4  
                if data[i,j]>-6:
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
    #data=(Circulation)
    data=DataEnd
    print(np.amin(data))
    print(np.amax(data))
    

    #print(CenterVortices)
    #print(CenterVortices)

    ax1.imshow(data, cmap=cmap, norm=norm)
    # draw gridlines
    ax1.set_title('XY spins')
    ax1.grid(which='major', axis='both', linestyle='-', color='w', linewidth=2)
    ax1.set_xticks(np.arange(-0.5, sizeGrid, 1));
    ax1.set_yticks(np.arange(-0.5, sizeGrid, 1));
    ax1.set_xticklabels([])
    ax1.set_yticklabels([])
    

 
def carreUR(Table,i,j):
    size=len(Table)
    return([Table[i-1,j],Table[i,j],Table[i,(j+1)%size],Table[i-1,(j+1)%size]])

def carreUL(Table,i,j):
    return([Table[i-1,j-1],Table[i,j-1],Table[i,j],Table[i-1,j]])

def carreDR(Table,i,j):
    size=len(Table)
    return([Table[i,j],Table[(i+1)%size,j],Table[(i+1)%size,(j+1)%size],Table[i,(j+1)%size]])


def carreDL(Table,i,j):
    size=len(Table)
    return([Table[i,j-1],Table[(i+1)%size,j-1],Table[(i+1)%size,j],Table[i,j]])
    


ani = animation.FuncAnimation(fig, do_mc_cycle, interval=1, blit=False)
