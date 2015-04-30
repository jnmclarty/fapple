# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 20:42:07 2015

@author: JMcLarty
"""


pos1 = ['p']
pos1 = pos1 + ['a']

pos2 = ['s']

pos3 = ['s']

pos4 = ['w','o','r','d']

source = [pos1, pos2, pos3, pos4]


from itertools import product
candidates = product(*source)
candidates = ["".join(c) for c in candidates]

print "Trying {} passwords".format(len(candidates))