#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 10 16:36:47 2023

@author: marc
"""

under = 1
over = 1
counter = 0
while True:
    under = under/2
    over = over*2
    counter+=1
    print("{:d}, {:.5e}, {:.5e}".format(counter, under, over))