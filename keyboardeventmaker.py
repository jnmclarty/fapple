# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 21:16:10 2015

@author: JMcLarty
"""

import ctypes
import time

SendInput = ctypes.windll.user32.SendInput

VKs = {'\t' : (0x09,),
'0' : (0x30,),
'1' : (0x31,),
'2' : (0x32,),
'3' : (0x33,),
'4' : (0x34,),
'5' : (0x35,),
'6' : (0x36,),
'7' : (0x37,),
'8' : (0x38,),
'9' : (0x39,),
'A' : (0x41,'upper'),
'B' : (0x42,'upper'),
'C' : (0x43,'upper'),
'D' : (0x44,'upper'),
'E' : (0x45,'upper'),
'F' : (0x46,'upper'),
'G' : (0x47,'upper'),
'H' : (0x48,'upper'),
'I' : (0x49,'upper'),
'J' : (0x4A,'upper'),
'K' : (0x4B,'upper'),
'L' : (0x4C,'upper'),
'M' : (0x4D,'upper'),
'N' : (0x4E,'upper'),
'O' : (0x4F,'upper'),
'P' : (0x50,'upper'),
'Q' : (0x51,'upper'),
'R' : (0x52,'upper'),
'S' : (0x53,'upper'),
'T' : (0x54,'upper'),
'U' : (0x55,'upper'),
'V' : (0x56,'upper'),
'W' : (0x57,'upper'),
'X' : (0x58,'upper'),
'Y' : (0x59,'upper'),
'Z' : (0x5A,'upper'),
'.' : (0xBE,),
'a' : (0x41,'lower'),
'b' : (0x42,'lower'),
'c' : (0x43,'lower'),
'd' : (0x44,'lower'),
'e' : (0x45,'lower'),
'f' : (0x46,'lower'),
'g' : (0x47,'lower'),
'h' : (0x48,'lower'),
'i' : (0x49,'lower'),
'j' : (0x4A,'lower'),
'k' : (0x4B,'lower'),
'l' : (0x4C,'lower'),
'm' : (0x4D,'lower'),
'n' : (0x4E,'lower'),
'o' : (0x4F,'lower'),
'p' : (0x50,'lower'),
'q' : (0x51,'lower'),
'r' : (0x52,'lower'),
's' : (0x53,'lower'),
't' : (0x54,'lower'),
'u' : (0x55,'lower'),
'v' : (0x56,'lower'),
'w' : (0x57,'lower'),
'x' : (0x58,'lower'),
'y' : (0x59,'lower'),
'z' : (0x5A,'lower')}


# C struct redefinitions 
PUL = ctypes.POINTER(ctypes.c_ulong)
class KeyBdInput(ctypes.Structure):
    _fields_ = [("wVk", ctypes.c_ushort),
                ("wScan", ctypes.c_ushort),
                ("dwFlags", ctypes.c_ulong),
                ("time", ctypes.c_ulong),
                ("dwExtraInfo", PUL)]

class HardwareInput(ctypes.Structure):
    _fields_ = [("uMsg", ctypes.c_ulong),
                ("wParamL", ctypes.c_short),
                ("wParamH", ctypes.c_ushort)]

class MouseInput(ctypes.Structure):
    _fields_ = [("dx", ctypes.c_long),
                ("dy", ctypes.c_long),
                ("mouseData", ctypes.c_ulong),
                ("dwFlags", ctypes.c_ulong),
                ("time",ctypes.c_ulong),
                ("dwExtraInfo", PUL)]

class Input_I(ctypes.Union):
    _fields_ = [("ki", KeyBdInput),
                 ("mi", MouseInput),
                 ("hi", HardwareInput)]

class Input(ctypes.Structure):
    _fields_ = [("type", ctypes.c_ulong),
                ("ii", Input_I)]

# Actuals Functions

def PressKey(hexKeyCode):

    extra = ctypes.c_ulong(0)
    ii_ = Input_I()
    ii_.ki = KeyBdInput( hexKeyCode, 0x48, 0, 0, ctypes.pointer(extra) )
    x = Input( ctypes.c_ulong(1), ii_ )
    SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))

def ReleaseKey(hexKeyCode):

    extra = ctypes.c_ulong(0)
    ii_ = Input_I()
    ii_.ki = KeyBdInput( hexKeyCode, 0x48, 0x0002, 0, ctypes.pointer(extra) )
    x = Input( ctypes.c_ulong(1), ii_ )
    SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))

def TypeKey(kexKeyCode):
    PressKey(kexKeyCode)
    time.sleep(0.01)
    ReleaseKey(kexKeyCode)
    time.sleep(0.01)
def PressCharacter(c):
    if c in VKs:
        k = VKs[c]
    else:
        raise Exception("{} not in Virtual Keyboard Dictionary".format(c))
    
    if len(k) == 1:
        TypeKey(k[0])
    else: #len is 2
        shift = False
        if k[1] == 'upper':
            shift=True
        
        if shift:
            PressKey(0xA1)
            
        TypeKey(k[0])

        if shift:
            ReleaseKey(0xA1)        
            

def PressString(s):
    for c in s:
        PressCharacter(c)
    time.sleep(0.1)

def TryPassword(passwd, newpwd):
    PressString(passwd)
    for i in range(2):
        PressCharacter("\t")
        PressString(newpwd)
    
def AltTab():
    '''
    Press Alt+Tab and hold Alt key for 2 seconds in order to see the overlay
    '''

    PressKey(0x012) #Alt
    PressKey(0x09) #Tab
    ReleaseKey(0x09) #~Tab

    time.sleep(2)       
    ReleaseKey(0x012) #~Alt


if __name__ =="__main__":

    for i in range(10):
        PressString('Aa0.\t1')
        time.sleep(1)
        
    #AltTab()