import matplotlib.pyplot as plt
import numpy as np
import numpy.random as rnd

class Grid:
    
    def __init__(self,L,J,beta) :
        angles = np.zeros((L,L))
        self.size=L
        self.J=J
        for i in range(L) :
            for j in range(L) :
                angles[i,j] = 2*np.pi*rnd.random()
        self.angles = angles
    

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
    if rnd.random() < np.exp(-beta*delta_energy):
        config.angles[i,j]=tetaNew
        config.energy += delta_energy
        config.magnetization += np.add(np.array([np.cos(tetaNew),np.sin(tetaNew)]),np.array([np.cos(tetaOld),np.sin(tetaOld)])*(-1)
     
        

def Monte_carlo(config,)
        
        
        
        
        
        
        