#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  9 20:29:48 2023

@author: marc
"""

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

print("Please be patient, I have packages to import and points to plot")

delta = 0.1

X=np.arange(-3., 3., delta)
Y=np.arange(-3., 3., delta)

X, Y = np.meshgrid(X,Y)
Z = np.sin(X) * np.cos(Y)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z)
ax.plot_wireframe(X, Y, Z, color='b', lw=0.5)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.show()
