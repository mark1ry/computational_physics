#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun  3 14:46:36 2023

@author: marc
"""

from vpython import *
import numpy as np

string = "blue: sin^2(x), white: cos^2(x), red: sin(x)cos(x)"
graph1 = graph(title=string, xtitle="x", ytitle="y", foreground=color.black,
               background = color.black)

y1 = gcurve(color=color.yellow)
y2 = gcurve(color=color.white)
y3 = gcurve(color=color.red)

for x in np.arange (-5, 5, 0.1):
    y1.plot( pos = (x, np.sin(x)*np.sin(x)))
    y2.plot( pos = (x, np.cos(x)*np.cos(x)))
    y3.plot( pos = (x, np.sin(x)*np.cos(x)))