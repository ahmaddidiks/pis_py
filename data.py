#!/usr/bin/env python

# Program Praktikum PIS (OFFLINE)
# Merupakan program python untuk mengidentifikasikan parameter dari sebuah
# transfer function diskrit yang dihitung secara offline. Disusun oleh
# asisten praktikum PIS (Pemodelan dan Identifikasi Sistem) Tahun ajaran 2019/2020:
 
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np

font = {'family': 'Times New Roman',
        'color':  'black',
        'weight': 'normal',
        'size': 14,
        }

def dataOrde1():
    print("Data Orde 1")
    global Vin1, Vout1, D1
    Vin1 = np.array([2.05, 3.24, 4.74, 4.93, 5.05])
    Vout1 = np.array([2.2, 9.2, 6.2, 6.2, 60.2]) 
    #D1 = np.concatenate((Vin1.T, Vout1))
    
    plt.plot(Vin1,Vout1)
    plt.title('Grafik Hubungan Vin-Vout Orde 1', fontdict=font)
    plt.xlabel('Vin', fontdict=font)
    plt.ylabel('Vout', fontdict=font)
    plt.legend(['Data'])
    plt.show()

def dataOrde2():
    print("Data Orde 2")
    global Vin2, Vout2, D2
    Vin2  = np.array ([2.14, 3.23, 4.11, 4.63, 5.1])
    Vout2 = ([12, 22, 32, 42, 62])
    #D2 = np.concatenate ((Vin2.T Vout2.T))

    plt.plot(Vin2,Vout2)
    plt.title('Grafik Hubungan Vin-Vout Orde 2', fontdict=font)
    plt.xlabel('Vin', fontdict=font)
    plt.ylabel('Vout', fontdict=font)
    plt.legend(['Data'])
    plt.show()

if __name__ == '__main__' :
    dataOrde1()
    dataOrde2()
