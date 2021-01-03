#!/usr/bin/env python

#import matplotlib.pyplot as plt
import numpy as np

def dataOrde2():
    pi = np.matrix('2.14 0 0 0 0; 3.23 2.14 0 12.00 0;4.11 3.23 2.14 22.30 12.00;4.63 4.11 3.23 32.0 22.0;5.10 4.63 4.11 42.0 32.0')
    y= np.matrix('12;22;32;42;62')
    tetha = np.linalg.inv(pi.T * pi) * pi.T * y
    print("Data Orde 2")
    print(tetha)

if __name__ == '__main__' :
    dataOrde2()
    
