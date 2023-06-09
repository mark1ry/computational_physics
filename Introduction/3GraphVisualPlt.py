#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  9 18:35:56 2023

@author: marc
"""

import matplotlib.pyplot as plt
import numpy as np

string = "blue: sin^2(x), white: cos^2(x), red: sin(x)cos(x)"
x = np.arange(-5., 5., 0.1)

fig = plt.figure()
ax = fig.add_subplot(111)
ax.set_title(string)
ax.set_xlabel("x")
ax.set_ylabel("f(x)")
ax.set_facecolor("k")

ax.plot(x, np.sin(x)*np.sin(x), '-y')
ax.plot(x, np.cos(x)*np.cos(x), '-b')
ax.plot(x, np.sin(x)*np.cos(x), '-r')
