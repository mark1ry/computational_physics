#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun  3 14:25:17 2023

@author: marc
"""
from vpython import *
import numpy as np



graph1 = graph(width=600, height=450, title='Visual 2D Plot',\
                  xtitle='x', ytitle='f(x)', foreground=color.black,\
                  background = color.black)
Plot1 = gcurve(color = color.white, )
for x in np.arange(0., 8.1, 0.1):
    Plot1.plot( pos = (x, 5.*cos(2.*x)*exp(-0.4*x)) )

graph2 = graph(width=600, height=450, title='Visual 2D Plot',\
                  xtitle='x', ytitle='f(x)', foreground=color.black,\
                  background = color.white)

Plot2 = gdots(color = color.black)

for x in np.arange(-5., +5., 0.1):
    Plot2.plot(pos = (x, cos(x)))