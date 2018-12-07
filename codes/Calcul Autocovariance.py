"""Calculs d'autocovariances"""

import numpy as np
import matplotlib.pyplot as plt
import copy
from Grid import *


def autocovariance(x,y) :
    autocov = 0.0
    L = x.size
    moy = 0
    moyquad = 0 
    for i in range(L) :
        for j in range(L) :
            autocov+=np.cos(x.angles[i,j]-y.angles[i,j])
            
    autocov/=L*L
    return autocov
    
    
def Calcul_Autocovariance(methode,size,Tmax,Niter) :
    
    
    cov = np.zeros(Tmax)
    for i in range(Niter) :
        x = Grid(size,1)
        y = Grid(size,1)
        y.angles = copy.copy(x.angles)
       
        for t in range(Tmax) :
            
            if (t%10) ==0 :
                a=autocovariance(x,y)/Niter
            cov[t]+=a 
            methode(y)
    return cov,x,y

#Cov1,x,y = Calcul_Autocovariance(metropolis_move,64,10000,1)
Cov2,x,y = Calcul_Autocovariance(ClusterMove,64,3000,5)
#plt.plot(np.arange(1000),Cov1)
plt.show()