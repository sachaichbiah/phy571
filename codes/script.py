#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  6 14:26:15 2018

@author: sacha
"""

#this is the script 
import numpy as np
import matplotlib.pyplot as plt

L=10
X, Y = np.meshgrid(np.linspace(0,39,L), np.linspace(0, 39, L))

Angles = np.random.rand(L,L)
U=np.cos(Angles)*5
V=np.sin(Angles)*5

fig1, ax1 = plt.subplots()
ax1.set_title('Arrows scale with plot width, not view')
Q = ax1.quiver(X, Y, U, V, units='x')
qk = ax1.quiverkey(Q, 0.9, 0.9, 2, r'$2 \frac{m}{s}$', labelpos='E',
                   coordinates='figure')

