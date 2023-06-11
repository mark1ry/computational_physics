#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 10 11:04:00 2023

@author: marc
"""

import numpy as np

file = open("input.txt", "r")

radius = float(file.read())
perim = 2 * np.pi * radius
area = np.pi * radius**2

print("R, C, A = {:}, {:}, {:}".format(radius, perim, area))