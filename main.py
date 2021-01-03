#!/usr/bin/env python

#Author     : Ahmad Didik Setiyadi
#Last Edit  : 3 Jan 2021
#Alih bahasa dari MATLAB ke Python

from func import *

def percobaan1():
    dataOrde1()
    autoRegresiveOrde1()
    
def percobaan2():
    dataOrde2()
    autoRegresiveOrde2()

def percobaan3():
    dataOrde1()
    movingAverageOrde1()

def percobaan4():
    dataOrde2()
    movingAverageOrde2()

def percobaan5():
    dataOrde1()
    ARMAOrde1()

def percobaan6():
    dataOrde2()
    ARMAOrde2()

if __name__ == '__main__' :
    percobaan6()