#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  2 17:00:56 2018

@author: sacha
"""

import matplotlib.pyplot as plt
from matplotlib import pylab

# Scientific libraries
import numpy as np
from scipy.optimize import curve_fit

Beta=np.load("BetaE.npy")
Means=np.load("ResultsMeanE.npy")
MeansSquare=np.load("ResultsMeanESquare.npy")



x=Beta
y=np.multiply(Beta**2,(MeansSquare-Means**2))

plt.figure()
plt.ylabel("Heat capacity/kb")
plt.xlabel("Beta")

plt.plot(x,y,"o")

x=1/Beta
y=np.multiply(Beta**2,(MeansSquare-Means**2))

plt.figure()
plt.ylabel("Heat capacity/kb")
plt.xlabel("kb*T")

plt.plot(x,y,"o")
