# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 20:50:35 2015

@author: JMcLarty
"""

import win32api as wapi
import win32con as wcon
from keyboardeventmaker import TryPassword
from passlist import candidates

import datetime as dt
import time

newpassword = "newpasswordhere"

def click(x,y):
    wapi.SetCursorPos((x,y))
    wapi.mouse_event(wcon.MOUSEEVENTF_LEFTDOWN, x, y, 0, 0)
    wapi.mouse_event(wcon.MOUSEEVENTF_LEFTUP, x, y, 0, 0)
        
ChangePassworddotdotdot = (812, 580)
click(*ChangePassworddotdotdot)
print "Starting fapple at {}".format(dt.datetime.now())

time.sleep(2)

ChangePassword = (999, 450)
OK = (1100, 395)
OldPassword = (961, 353)

for i, passwd in enumerate(candidates):
    click(*OldPassword)
    time.sleep(0.5)
    print "Trying password #{}/{} ({})".format(i, len(candidates), passwd)
    TryPassword(passwd, newpassword)
    click(*ChangePassword)
    time.sleep(4)
    click(*OK)
    time.sleep(2)