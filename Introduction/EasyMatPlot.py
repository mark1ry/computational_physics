#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  9 18:59:20 2023

@author: marc
"""

import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-5., 5., 0.02)
y = np.sin(x) * np.sin(x**2)

fig = plt.figure()
ax = fig.add_subplot(111)
ax.set_xlabel("x")
ax.set_ylabel("f(x)")
ax.set_title("f(x) vs x")
ax.plot(x, y, '-', lw=2)
ax.grid(True)
plt.show()
