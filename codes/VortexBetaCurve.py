from Grid import *

def carreDR(Table,i,j):
    size=len(Table)
    return([Table[i,j],Table[(i+1)%size,j],Table[(i+1)%size,(j+1)%size],Table[i,(j+1)%size]])

#Constantes de la simulation
length_cycle =1000
sizeGrid=40
J=1
Beta=0.00
n_warmup=1000
n_cycles=12000

# instantiate a configuration
config=Grid(sizeGrid,J,Beta)

def monte_Carlo(n_cycles,n_warmup,config):
    
    for i in range(n_warmup): 
        metropolis_move(config)
    Vortices=[]
    DATA=[]
    for l in range(n_cycles): 
        for k in range(length_cycle):
            metropolis_move(config)
    
        Angles=config.angles
        Circulation=np.zeros(Angles.shape)
        data = -(np.cos(Angles-np.roll(Angles,1,1))+np.cos(Angles-np.roll(Angles,-1,1))+np.cos(Angles-np.roll(Angles,1,0))+np.cos(Angles-np.roll(Angles,-1,0)))
    
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

        Vortices.append(Number_Vortices)
        if l%20==0 : 
            print(l/20,config.beta)
            config.beta=max(0,config.beta+0.01)
            DATA.append([config.beta,np.mean(np.array(Vortices))])
            Vortices=[]
            
    return(DATA)

A=monte_Carlo(n_cycles,n_warmup,config)

#A=np.load("Data/VortexFunctionBeta.npy")


A=np.array(A)
plt.plot(A[:,0],A[:,1])

    
    
