from Grid import *
   
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


CC=0.9
Clist=[(0.6*CC,1*CC,0.6*CC),(1*CC,1*CC,1*CC),(0.6*CC,0.6*CC,1*CC)]
cmap = colors.ListedColormap(Clist)
bounds=[-6,-1,1,6]
norm = colors.BoundaryNorm(bounds, cmap.N)

#Constantes de la simulation
length_cycle =100
Sizefig=6
sizeGrid=20
n_warmup =10000

# instantiate a configuration
config=Grid(sizeGrid,1,1.5,np.array([0,0]))
Angles=config.angles
U=np.cos(Angles)*2
V=np.sin(Angles)*2
fig,ax1=plt.subplots(figsize=(Sizefig+4, Sizefig))
ax1.set_title('XY spins')
Q = ax1.quiver(U, V, units='width',minshaft = 1, minlength = 1, color = 'k')

for i in range(n_warmup): 
    metropolis_move(config)

ani = animation.FuncAnimation(fig, do_mc_cycle,np.arange(1, 100000), interval=1, blit=False)
