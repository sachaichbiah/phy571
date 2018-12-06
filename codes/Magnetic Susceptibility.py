import xlsxwriter
import os
os.chdir('C:\\Users\\yann\\Documents\\Polytechnique\\Physique\\phy571\\phy571\\codes')

import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.ticker as plticker
from matplotlib import colors
import time
from Grid import *





# instantiate a configuration
config=Grid(64,1,0.5)
steps = []
clusters = []

n_warmup =2000
"""for i in range(n_warmup) : 
    ClusterMove(
"""
config1=Grid(64,1,0.9)
#initiate figure
fig = plt.figure()
ax = fig.add_subplot(111)

lines =[]

ax.set_xlim(0,config1.size//2)
ax.set_ylim(0,1)




n_warmup =1500
N_iterations = 1000
length_cycle=10
Xaxis=[]
ClusterSize=[]
Susceptibility = []



#Write in Excel
workbook = xlsxwriter.Workbook('Susceptibility64,sur1.3,directionX.xlsx')
worksheet = workbook.add_worksheet()
worksheet.write(0,0, 'Beta')
worksheet.write(0,1, 'MeanCluster')
worksheet.write(0,2, 'Susceptibility')


temperatures = np.arange(1.3,1.9,0.05)

liste = []
for j in range(len(temperatures)) :
    mean = 0
    config=Grid(64,1,temperatures[j])
    squaredMagn = []
    Xaxis.append(temperatures[j])
    for i in range(n_warmup) :
        ClusterMove(config)
    
    
    
    for i in range(N_iterations) :
        
        mean+=ClusterMove(config)
        if i%length_cycle==0 :
            squaredMagn.append(Calcul_Magnetisation(config)[0])#projection selon une direction
    mean/=N_iterations
    Susceptibility.append(np.var(squaredMagn))
    ClusterSize.append(mean)



col = 1
for j in range(len(temperatures)) :
    row = 2
    worksheet.write(j+1,0,temperatures[j])
    worksheet.write(j+1,1,ClusterSize[j])
    worksheet.write(j+1,2,Susceptibility[j])
    
    
workbook.close()