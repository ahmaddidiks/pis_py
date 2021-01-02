#!/usr/bin/env python

from data import *
from scipy import signal

# METODE LEAST SQUARE DENGAN STRUKTUR AUTO REGRESSIVE (ORDE 1)
# Metode Auto Regresive atau (AR) Merupakan penghitungan parameter model 
# sistem dengan persamaan dasar *y(k)=b0*x(k)+a0*y(k-1)*
def autoRegresiveOrde1():
    #cara berfikir dimatlab berbeda dengan dipython
    ARxk_t = Vin1.copy()
    ARxk  = np.transpose(np.matrix(Vin1)) #transpose matrix 1D
    ARyk  = np.transpose(np.matrix(Vout1))
    ARykTemp = Vout1.copy()
    ARykTemp = np.insert(ARykTemp, 0, 0)
    ARyk_t = np.delete(ARykTemp, 5)
    ARyk1 = np.transpose(np.matrix(ARyk_t))
    ARpiTemp  = np.vstack((ARxk_t, ARyk_t))
    ARpi = ARpiTemp.T
    AR = np.linalg.inv(ARpi.T.dot(ARpi)).dot(ARpi.T).dot(ARyk)

    a = AR[0].dot(ARxk[0]) + AR[1].dot(0)
    ARy = ([a])

    for i in range(1,len(ARxk)):
        a = AR[0].dot(ARxk[i]) + AR[1].dot(ARy[i-1])
        ARy = np.insert(ARy,i, a)
    
    dataAR = np.vstack((ARxk_t, ARy)).T

    plt.plot(ARxk, ARy)
    plt.plot(Vin1, Vout1)
    plt.title('Hubungan Vin-Vout Metode AR Orde 1', fontdict=font)
    plt.xlabel('Vin', fontdict=font)
    plt.ylabel('Vout', fontdict=font)
    plt.legend(['AR','Data'])
    plt.show()


# METODE LEAST SQUARE DENGAN STRUKTUR AUTO REGRESSIVE (ORDE 2)
# Metode Auto Regresive atau (AR) Merupakan penghitungan parameter model 
# sistem dengan persamaan dasar *y(k)=b0*x(k)+a0*y(k-1)+a1*y(k-2)*
def autoRegresiveOrde2():
    ARxk_t = Vin2.copy()
    ARxk  = np.transpose(np.matrix(Vin2)) #transpose matrix 1D
    ARyk  = np.transpose(np.matrix(Vout2))
    ARykTemp = Vout2.copy()
    ARykTemp = np.insert(ARykTemp, 0, 0)
    ARyk_t = np.delete(ARykTemp, 5)
    ARyk1 = np.transpose(np.matrix(ARyk_t))

    ARyk2_t = ARyk_t.copy()
    ARyk2_t = np.insert(ARyk2_t,0,0)
    ARyk2_t = np.delete(ARyk2_t, 5)
    ARyk2 = np.transpose(np.matrix(ARyk2_t))

    ARpiTemp  = np.vstack((ARxk_t, ARyk_t, ARyk2_t))
    ARpi = ARpiTemp.T
    AR = np.linalg.inv(ARpi.T.dot(ARpi)).dot(ARpi.T).dot(ARyk)

    a = AR[0].dot(ARxk[0]) + AR[1].dot(0) + AR[2].dot(0)
    ARy = ([a]) #ARy[0] di python = ARy(1)
    print(AR)
    print(ARxk)
    a = AR[0].dot(ARxk[1]) + AR[1].dot(ARy[0]) + AR[2].dot(0)
    ARy = np.insert(ARy,1, a)

    for i in range(2,len(ARxk)):
        a = AR[0].dot(ARxk[i]) + AR[1].dot(ARy[i-1]) + AR[2].dot(ARy[i-2])
        ARy = np.insert(ARy,i, a)
    
    dataAR = np.vstack((ARxk_t, ARy)).T
    
    plt.plot(ARxk, ARy)
    plt.plot(Vin2, Vout2)
    plt.title('Hubungan Vin-Vout Metode AR Orde 2', fontdict=font)
    plt.xlabel('Vin', fontdict=font)
    plt.ylabel('Vout', fontdict=font)
    plt.legend(['AR','Data'])
    plt.show()