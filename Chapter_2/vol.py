#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 10 11:17:36 2023

@author: marc
"""

import numpy as np

radius = 10.
surface = 4 * np.pi * radius**2
volume = (4/3) * np.pi * radius**3

print("R, S, V = {:}, {:}, {:}".format(radius, surface, volume))