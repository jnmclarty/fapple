# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 20:22:17 2015

@author: JMcLarty
"""

import win32api as win
import time

mode = 'explore'

if mode == 'explore':
    for i in range(50):
        print "x={}, y={}".format(*win.GetCursorPos())
        time.sleep(1)
    
if mode == 'label':
    answers = {}
    
    while True:
        x, y = win.GetCursorPos()
        ans = raw_input("?")
        if ans == 'qqq':
            break
        answers[ans] = (x,y)
    
    for key in answers.keys():
        print key, answers[key]

# second change password (980, 353)
# ok button (987, 450)
# change password (-272, 1258)
# old password (825, 583)
    
#Change Password Button = 957, 353
