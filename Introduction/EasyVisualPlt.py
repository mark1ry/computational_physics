#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  9 18:35:56 2023

@author: marc
"""

import matplotlib.pyplot as plt 
import numpy as np

fig1 = plt.figure(figsize=[6, 4.5])
ax1 = fig1.add_subplot(111)
x = np.arange(0., 8.1, 0.1)
y = 5.*np.cos(2.*x)*np.exp(-0.4*x)

ax1.plot(x, y, '-w')
ax1.set_xlabel("x")
ax1.set_ylabel("f(x)")
ax1.set_title("Visual 2D Plot")
ax1.set_facecolor("black")

fig2 = plt.figure(figsize=[6, 4.5])
ax2 = fig2.add_subplot(111)
x = np.arange(-5., 5., 0.1)
y = np.cos(x)

ax2.plot(x, y, '.k')
ax1.set_xlabel("x")
ax1.set_ylabel("f(x)")
ax1.set_title("Visual 2D Plot")
