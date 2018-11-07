import matplotlib.pyplot as plt
import matplotlib.animation as animation

from Grid import *




length_cycle =100
nt = 200

# instantiate a configuration
config=Grid()
Angles=config.angles
U=np.cos(Angles)*5
V=np.sin(Angles)*5
fig = plt.figure(figsize=(10,5))
ax1 = fig.add_subplot(121)
ax1.set_title('XY spins')
Q = ax1.quiver(U, V, units='width',minshaft = 2)

ax2 = fig.add_subplot(122, aspect=100)
line, = ax2.plot([],[])
ax2.set_xlim(0,nt)
ax2.set_ylim(-1,1)
steps = []
magnet = []

"""  
# a two-panel figure

im=ax1.imshow(config_to_image(config), interpolation='none')
ax2 = fig.add_subplot(122, aspect=100)
line, = ax2.plot([],[])
ax2.set_xlim(0,nt)
ax2.set_ylim(-1,1)

steps = []
magnet = []


"""

def do_mc_cycle(n):
    
    for k in range(length_cycle):
        metropolis_move(config)
    
    Angles=config.angles
    U=np.cos(Angles)*5
    V=np.sin(Angles)*5
    ax1.cla()
    Q=(ax1.quiver(U,V))
    
    m = config.magnetization[0]/float(config.size**2)
    if len(steps) < nt: steps.append(n)
    if len(magnet) < nt:
        magnet.append(m)
    else:
        magnet.insert(nt, m)
        magnet.pop(0)
    
    print(nt,m)
    line.set_data(steps,magnet)
    
    return (Q,line)

ani = animation.FuncAnimation(fig, do_mc_cycle, interval=100, blit=False)


