import matplotlib.pyplot as plt
import numpy as np
import numpy.random as rnd

class Grid:
#petit commentaire    
    
    def __init__(self,L,J,beta) :
        angles = np.zeros((L,L))
        self.size=L
        self.J=J
        for i in range(L) :
            for j in range(L) :
                angles[i,j] = 2*np.pi*rnd.random()
        self.angles = angles
    
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
        



L=50
Gridex = Grid(L,1,1)

Angles = Gridex.angles
U=np.cos(Angles)*5
V=np.sin(Angles)*5

fig1, ax1 = plt.subplots()
ax1.set_title('XY spins')
Q = ax1.quiver(U, V, units='width',minshaft = 2)
plt.show()
        
        
        
        