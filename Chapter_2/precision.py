#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 10 16:51:48 2023

@author: marc
"""

N=150
epsilon = complex(1.0)
counter = 0
for i in range(N):
    epsilon = epsilon/2
    value = complex(1.0) + epsilon
    counter += 1
    print("{:}, {:}, {:}".format(counter, epsilon, value))