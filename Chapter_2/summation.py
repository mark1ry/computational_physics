#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 10 16:59:40 2023

@author: marc
"""

x = float(input("What value of x should the function sin(x) be evaluated at? "))
term = x
result = x
precision = float(input("What should the precision be? "))
iteration = 2
while (abs(term/result) > precision):
    term = -term*x*x/((2*iteration - 1)*(2*iteration-2))
    result += term
    iteration += 1
print("sin(x) = {:.5f}".format(result))
    