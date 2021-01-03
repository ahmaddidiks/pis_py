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

    ARpi  = (np.vstack((ARxk_t, ARyk_t, ARyk2_t))).T
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

# METODE LEAST SQUARE DENGAN STRUKTUR MOVING AVERAGE (ORDE 1)
# Metode Moving Average atau (MA) Merupakan penghitungan parameter model 
# sistem dengan persamaan dasar *y(k)=b0*x(k)+b1*x(k-1)*
def movingAverageOrde1():

    MAxk_t = Vin1.copy()
    MAxk  = np.transpose(np.matrix(Vin1)) #transpose matrix 1D
    MAyk  = np.transpose(np.matrix(Vout1))
    
    MAxk1 = MAxk_t.copy()
    MAxk1 = np.insert(MAxk1,0,0)
    MAxk1 = np.delete(MAxk1,len(MAxk1)-1)
    MApi  = np.vstack((MAxk_t, MAxk1)).T 

    MA = np.linalg.inv(MApi.T.dot(MApi)).dot(MApi.T).dot(MAyk)
    
    a = MA[0].dot(MAxk[0]) + MA[1].dot(0)
    MAy = ([a])

    for i in range(1,len(MAxk)):
        a = MA[0].dot(MAxk[i]) + MA[1].dot(MAxk[i-1])
        MAy = np.insert(MAy,i,a)
    
    dataMA = np.vstack((MAxk.T, MAy)).T
    
    plt.plot(MAxk, MAy)
    plt.plot(Vin1, Vout1)
    plt.title('Hubungan Vin-Vout Metode MA Orde 1', fontdict=font)
    plt.xlabel('Vin', fontdict=font)
    plt.ylabel('Vout', fontdict=font)
    plt.legend(['MA','Data'])
    plt.show()

# METODE LEAST SQUARE DENGAN STRUKTUR MOVING AVERAGE (ORDE 2)
# Metode Moving Average atau (MA) Merupakan penghitungan parameter model 
# sistem dengan persamaan dasar *y(k)=b0*x(k)+b1*x(k-1)+b2*x(k-2)*
def movingAverageOrde2():
    MAxk_t = Vin2.copy()
    MAxk  = np.transpose(np.matrix(Vin2)) #transpose matrix 1D
    MAyk  = np.transpose(np.matrix(Vout2))
    
    MAxk1 = MAxk_t.copy()
    MAxk1 = np.insert(MAxk1,0,0)
    MAxk1 = np.delete(MAxk1,len(MAxk1)-1)
    
    MAxk2 = MAxk1.copy()
    MAxk2 = np.insert(MAxk2,1,0)
    MAxk2 = np.delete(MAxk2,len(MAxk2)-1)

    MApi  = (np.vstack((MAxk_t, MAxk1, MAxk2))).T
    
    MA = np.linalg.inv(MApi.T.dot(MApi)).dot(MApi.T).dot(MAyk)
    
    a = MA[0].dot(MAxk[0]) + MA[1].dot(0) + MA[2].dot(0)
    MAy = ([a])
    a = MA[0].dot(MAxk[1]) + MA[1].dot(MAy[0]) + MA[2].dot(0)
    MAy = np.insert(MAy,1,a)

    for i in range(2,len(MAxk)):
        a = MA[0].dot(MAxk[i]) + MA[1].dot(MAxk[i-1]) + MA[2].dot(MAxk[i-2])
        MAy = np.insert(MAy,i,a)
    
    dataMA = np.vstack((MAxk_t,MAy)).T #MAxk_t = MAxk.T
    
    plt.plot(MAxk, MAy)
    plt.plot(Vin2, Vout2)
    plt.title('Hubungan Vin-Vout Metode MA Orde 2', fontdict=font)
    plt.xlabel('Vin', fontdict=font)
    plt.ylabel('Vout', fontdict=font)
    plt.legend(['MA','Data'])
    plt.show()

# METODE LEAST SQUARE DENGAN STRUKTUR AUTO REGRESSIVE MOVING AVERAGE (ORDE 1)
# Metode Auto Regresive Moving Average (ARMA) Merupakan penghitungan 
# parameter model sistem dengan persamaan dasar 
# *y(k)=b0*x(k)+b1*x(k-1)+a0*y(k-1)*   
def ARMAOrde1():
    #ARMAx/yk di matlab = ARMAx/yk.T di python
    ARMAxk  = np.transpose(np.matrix(Vin1)) #transpose matrix 1D
    ARMAyk  = np.transpose(np.matrix(Vout1))

    ARMAxk1 = Vin1.copy()
    ARMAxk1 = np.insert(ARMAxk1,0,0)
    ARMAxk1 = np.delete(ARMAxk1,len(ARMAxk1)-1)

    ARMAyk1 = Vout1.copy()
    ARMAyk1 = np.insert(ARMAyk1,0,0)
    ARMAyk1 = np.delete(ARMAyk1,len(ARMAyk1)-1)

    ARMApi = np.vstack((ARMAxk.T, ARMAxk1, ARMAyk1)).T

    ARMA = np.linalg.inv(ARMApi.T.dot(ARMApi)).dot(ARMApi.T).dot(ARMAyk)

    a = ARMA[0].dot(ARMAxk[0]) + ARMA[1].dot(0) +ARMA[2].dot(0)
    ARMAy = ([a])

    for i in range(1,len(ARMAxk)):
        a = ARMA[0].dot(ARMAxk[i]) + ARMA[1].dot(ARMAxk[i-1]) + ARMA[2].dot(ARMAy[i-1])
        ARMAy = np.insert(ARMAy,i,a)
    
    dataARMA = np.vstack((ARMAxk.T,ARMAy)).T

   
    plt.plot(ARMAxk, ARMAy)
    plt.plot(Vin1, Vout1)
    plt.title('Hubungan Vin-Vout Metode ARMA Orde 1', fontdict=font)
    plt.xlabel('Vin', fontdict=font)
    plt.ylabel('Vout', fontdict=font)
    plt.legend(['ARMA','Data'])
    plt.show()

# METODE LEAST SQUARE DENGAN STRUKTUR AUTO REGRESSIVE MOVING AVERAGE (ORDE 2)
# Metode Auto Regresive Moving Average (ARMA) Merupakan penghitungan 
# parameter model sistem dengan persamaan dasar 
# *y(k)=b0*x(k)+b1*x(k-1)+b2*x(k-2)+a0*y(k-1)+a1*y(k-2)*
def ARMAOrde2():
    #ARMAx/yk di matlab = ARMAx/yk.T di python
    ARMAxk  = np.transpose(np.matrix(Vin2)) #transpose matrix 1D
    ARMAyk  = np.transpose(np.matrix(Vout2))

    ARMAxk1 = Vin2.copy()
    ARMAxk1 = np.insert(ARMAxk1,0,0)
    ARMAxk1 = np.delete(ARMAxk1,len(ARMAxk1)-1)

    ARMAxk2 = ARMAxk1.copy()
    ARMAxk2 = np.insert(ARMAxk2,1,0)
    ARMAxk2 = np.delete(ARMAxk2,len(ARMAxk2)-1)

    ARMAyk1 = Vout2.copy()
    ARMAyk1 = np.insert(ARMAyk1,0,0)
    ARMAyk1 = np.delete(ARMAyk1,len(ARMAyk1)-1)

    ARMAyk2 = ARMAyk1.copy()
    ARMAyk2 = np.insert(ARMAyk2,1,0)
    ARMAyk2 = np.delete(ARMAyk2,len(ARMAyk2)-1)

    ARMApi = np.vstack((ARMAxk.T, ARMAxk1, ARMAxk2, ARMAyk1, ARMAyk2)).T

    ARMA = np.linalg.inv(ARMApi.T.dot(ARMApi)).dot(ARMApi.T).dot(ARMAyk)

    a = ARMA[0].dot(ARMAxk[0]) + ARMA[1].dot(0) + ARMA[2].dot(0) + ARMA[4].dot(0)
    ARMAy = ([a])
    
    a = ARMA[0].dot(ARMAxk[1]) + ARMA[1].dot(ARMAxk[0]) + ARMA[2].dot(0) + ARMA[3].dot(ARMAy[0]) + ARMA[4].dot(0)
    ARMAy = np.insert(ARMAy,1,a)

    for i in range(2,len(ARMAxk)):
        a = ARMA[0].dot(ARMAxk[i]) + ARMA[1].dot(ARMAxk[i-1]) + ARMA[2].dot(ARMAxk[i-2]) + ARMA[3].dot(ARMAy[i-1]) + ARMA[4].dot(ARMAy[i-2])
        ARMAy = np.insert(ARMAy,i,a)
    
    
    dataARMA = np.vstack((ARMAxk.T,ARMAy)).T

   
    plt.plot(ARMAxk, ARMAy)
    plt.plot(Vin2, Vout2)
    plt.title('Hubungan Vin-Vout Metode ARMA Orde 2', fontdict=font)
    plt.xlabel('Vin', fontdict=font)
    plt.ylabel('Vout', fontdict=font)
    plt.legend(['ARMA', 'Data'])
    plt.show()
