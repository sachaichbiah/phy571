#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 28 08:24:57 2018

@author: sacha
"""
import matplotlib.pyplot as plt
from matplotlib import pylab
import numpy as np
from scipy.optimize import curve_fit

Beta=np.load("Beta2Magnetization.npy")
Means=np.load("Results2Magnetization.npy")
MeansSquare=np.load("ResultsSquare2Magnetization.npy")



x=Beta
y=np.multiply(Beta,(MeansSquare-Means**2))

plt.figure()
plt.ylabel("Magnetic susceptibility")
plt.xlabel("Beta")

plt.plot(x,y,"o")

x=1/Beta
y=np.multiply(Beta,(MeansSquare-Means**2))

plt.figure()
plt.ylabel("Magnetic susceptibility")
plt.xlabel("kb*T")

plt.plot(x,y,"o")


    

