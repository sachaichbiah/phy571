import matplotlib.pyplot as plt
import numpy as np
import numpy.random as rnd
from collections import deque
import matplotlib.animation as animation
import matplotlib.ticker as plticker
from matplotlib import colors
import time
class Grid:
#petit commentaire    
    
    def __init__(self,L=10,J=1,beta=1) :
        angles = np.zeros((L,L))
        self.beta = beta
        self.size=L
        self.J=J
        for i in range(L) :
            for j in range(L) :
                angles[i,j] = 2*np.pi*rnd.random()
        self.angles = angles
        self.energy = 0 
        self.magnetization = 0
    
    def Energy(self) :
        E = 0 
        J =self.J
        angles =self.angles
        for i in range(L) :
            for j in range(L) :
                A = angles[i,j]
                A1= angles[(i+1)%L,j]
                A2 = angles[(i-1)%L,j]
                A3 = angles[i,(j+1)%L]
                A4 = angles[i,(j-1)%L]
                E -= J/2*(np.cos(A-A1)+np.cos(A-A2)+np.cos(A-A2)+np.cos(A-A3)+np.cos(A-A4))
        return E
     
        
    
def printGrid(config): 
    #L=config.size
    Angles=config.angles
    U=np.cos(Angles)*5
    V=np.sin(Angles)*5
    fig1, ax1 = plt.subplots()
    ax1.set_title('XY spins')
    Q = ax1.quiver(U, V, units='width',minshaft = 2)
    plt.show()     
    
    
def metropolis_move(config):
    """Modify (or not) a configuration with Metropolis algorithm"""
    
    L = config.size
    J = config.J
    Angles =config.angles
    
    beta = config.beta
    i, j = rnd.randint(L, size=(2)) # pick a random site
    tetaNew=rnd.rand()*2*np.pi
    tetaOld=Angles[i,j]
    # compute energy difference
    coef= J/2
    delta_energy =  -coef* (np.cos(tetaNew-Angles[i,(j+1)%L])-np.cos(tetaOld-Angles[i,(j+1)%L])
    + np.cos(tetaNew-Angles[i,(j-1)%L])-np.cos(tetaOld-Angles[i,(j-1)%L])
    + np.cos(tetaNew-Angles[(i+1)%L,j])-np.cos(tetaOld-Angles[(i+1)%L,j])
    + np.cos(tetaNew-Angles[(i-1)%L,j])-np.cos(tetaOld-Angles[(i-1)%L,j]))
    
    # accept modification with Metropolis probability
    # if not accepted: leave configuration unchanged
    if (rnd.random() < np.exp(-beta*delta_energy)):
        config.angles[i,j]=tetaNew
        config.energy += delta_energy
        config.magnetization += np.add(np.array([np.cos(tetaNew),np.sin(tetaNew)]),np.array([np.cos(tetaOld),np.sin(tetaOld)])*(-1))
        
        
def Monte_carlo(config, length_cycle,n_cycles = 10000, n_warmup =1000): 
    av_m, av_m2, av_e, av_e2 = 0,0,0,0
    for i in range (n_warmup): 
        metropolis_move(config)
        
        
    for i in range(n_cycles) : 
        for j in range (length_cycle) : 
            metropolis_move(config)
        
        av_m+=config.magnetization
        av_m2+=config.magnetization**2
        av_e+=config.energy
        av_e2+=config.energy**2
    
    av_m/=n_cycles
    av_m2/=n_cycles
    av_e/=n_cycles
    av_e2/=n_cycles

def ClusterMove(config):
    L = config.size
    J = config.J
    beta = config.beta
    Angles =config.angles
    theta = rnd.random()*2*np.pi #angle paramétrant le plan de symétrie, tel que alpha -> 2 theta- alpha
    i, j = rnd.randint(L, size=(2))
    Angles[i,j]*=-1
    Angles[i,j]+=2*theta
    toTreat = deque()
    toTreat.append([i,j])
    MarkPoints = np.zeros((L,L))
    MarkPoints[i,j] = 1
    #Elargissement du cluster :
    while toTreat != deque() :
        i,j = toTreat.popleft()
        neighbors = [[(i+1)%L,j],[(i-1)%L,j],[i,(j+1)%L],[i,(j-1)%L]]
        for x in neighbors :
            if MarkPoints[x[0],x[1]]!=1 :
                seuil = min(0,J*beta*(np.cos(Angles[i,j]-Angles[x[0],x[1]])-np.cos(Angles[i,j]+Angles[x[0],x[1]]-2*theta)))
                if seuil<=np.log(1-rnd.random()):
                    MarkPoints[x[0],x[1]]=1
                    toTreat.append([x[0],x[1]])
                    Angles[x[0],x[1]] = 2*theta -Angles[x[0],x[1]]




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









    """
    
A=Grid()
printGrid(A)
L=A.size
Monte_carlo(A,L)
printGrid(A)

"""

"""
L=50
Gridex = Grid(L,1,1)

Angles = Gridex.angles
U=np.cos(Angles)*5
V=np.sin(Angles)*5

fig1, ax1 = plt.subplots()
ax1.set_title('XY spins')
Q = ax1.quiver(U, V, units='width',minshaft = 2)
plt.show()      
     """
        
    
    
    