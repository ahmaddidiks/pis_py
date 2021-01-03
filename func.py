#!/usr/bin/env python

#Author     : Ahmad Didik Setiyadi
#Last Edit  : 3 Jan 2021
#Alih bahasa dari MATLAB ke Python

from data import *
from scipy import signal

# METODE LEAST SQUARE DENGAN STRUKTUR AUTO REGRESSIVE (ORDE 1)
# Metode Auto Regresive atau (AR) Merupakan penghitungan parameter model 
# sistem dengan persamaan dasar *y(k)=b0*x(k)+a0*y(k-1)*
def autoRegresiveOrde1():
    ARxk  = np.transpose(np.matrix(Vin1)) #transpose matrix 1D
    ARyk  = np.transpose(np.matrix(Vout1))
    
    ARyk1 = ARyk.copy()
    ARyk1 = np.insert(ARyk1, 0, 0)
    ARyk1 = np.delete(ARyk1, len(Vout1)) #hapus element terakhir
    ARyk1  = np.transpose(np.matrix(ARyk1))

    ARpi  = np.vstack((ARxk.T, ARyk1.T)).T #tidak bisa langsung
    
    AR = np.linalg.inv(ARpi.T.dot(ARpi)).dot(ARpi.T).dot(ARyk)

    a = AR[0].dot(ARxk[0]) + AR[1].dot(0)
    ARy = ([a])

    for i in range(1,len(ARxk)):
        a = AR[0].dot(ARxk[i]) + AR[1].dot(ARy[i-1])
        ARy = np.insert(ARy,i, a)
    
    dataAR = np.vstack((ARxk.T, ARy)).T

    den = AR.A1 #merubah menjadi rank 1
    den = list(den) #list ==> menambah koma diantara elements
    sys = signal.TransferFunction(num, den, dt=1) # selalu menghasilkan tf dg s pangkat tertinggi berubah menjadi (s^n),
                                                  # sehingga hasil tersebut merupakan angka hasil bagi den[0]
                                                  # misal 1/4s^2+2s+1 menjadi 0.25/s^2+0.5s+0.25
                                                  # aku sudah mensimulasikannya hasilnya sama, secara matematis dan logika pun juga sama
                                                  # jika menemukan solusinya silahkan PR ke https://github.com/ahmaddidiks/pis_py

    print(" ARyk1 = ")
    print(ARyk1)
    print("\n ARpi = ")
    print(ARpi)
    print("\n AR = ")
    print(AR)
    print("\n ARy = ")
    print(ARy)
    print("\n dataAR = ")
    print(dataAR)
    print("\n Transfer Fungsi = ")
    print(sys)

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
    #cara berfikir dimatlab berbeda dengan dipython
    #ARx/yk matlab = ARx/yk.T python
    ARxk  = np.transpose(np.matrix(Vin2)) #transpose matrix 1D
    ARyk  = np.transpose(np.matrix(Vout2))
    
    ARyk1 = Vout2.copy()
    ARyk1 = np.insert(ARyk1, 0, 0)
    ARyk1 = np.delete(ARyk1, len(ARyk1)-1)
    ARyk1 = np.transpose(np.matrix(ARyk1)) 

    ARyk2 = Vout2.copy()
    ARyk2 = np.insert(ARyk2,0,0)
    ARyk2 = np.insert(ARyk2,1,0)
    ARyk2 = np.delete(ARyk2, len(ARyk2)-1)
    ARyk2 = np.delete(ARyk2, len(ARyk2)-1)
    ARyk2 = np.transpose(np.matrix(ARyk2))

    ARpi  = (np.vstack((ARxk.T, ARyk1.T, ARyk2.T))).T #tidak bisa langsung
    AR = np.linalg.inv(ARpi.T.dot(ARpi)).dot(ARpi.T).dot(ARyk)

    a = AR[0].dot(ARxk[0]) + AR[1].dot(0) + AR[2].dot(0)
    ARy = ([a]) #ARy[0] di python = ARy(1)

    a = AR[0].dot(ARxk[1]) + AR[1].dot(ARy[0]) + AR[2].dot(0)
    ARy = np.insert(ARy,1, a)

    for i in range(2,len(ARxk)):
        a = AR[0].dot(ARxk[i]) + AR[1].dot(ARy[i-1]) + AR[2].dot(ARy[i-2])
        ARy = np.insert(ARy,i, a)
    
    dataAR = np.vstack((ARxk.T, ARy)).T

    num = [1] 
    den = AR.A1 #merubah menjadi rank 1
    den = list(den) #list ==> menambah koma diantara elements
    sys = signal.TransferFunction(num, den, dt=1) # selalu menghasilkan tf dg s pangkat tertinggi berubah menjadi (s^n),
                                                  # sehingga hasil tersebut merupakan angka hasil bagi den[0]
                                                  # misal 0.25/4s^2+2s+1 menjadi 0.4/s^2+0.5s+0.25
                                                  # aku sudah mensimulasikannya hasilnya sama, secara matematis dan logika pun juga sama
                                                  # jika menemukan solusinya silahkan PR ke https://github.com/ahmaddidiks/pis_py
    
    print(" ARyk1 = ")
    print(ARyk1)
    print("\n ARyk2 = ")
    print(ARyk2)
    print("\n ARpi = ")
    print(ARpi)
    print("\n AR = ")
    print(AR)
    print("\n ARy = ")
    print(ARy)
    print("\n dataAR = ")
    print(dataAR)
    print("\n Transfer Fungsi = ")
    print(sys)

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
    #cara berfikir dimatlab berbeda dengan dipython
    #MAx/yk matlab = MAx/yk.T python
    MAxk  = np.transpose(np.matrix(Vin1)) #transpose matrix 1D
    MAyk  = np.transpose(np.matrix(Vout1))
    
    MAxk1 = Vin1.copy()
    MAxk1 = np.insert(MAxk1,0,0)
    MAxk1 = np.delete(MAxk1,len(MAxk1)-1)
    MAxk1 = np.transpose(np.matrix(MAxk1))

    MApi  = np.vstack((MAxk.T, MAxk1.T)).T #tidak bisa langsung
    MA = np.linalg.inv(MApi.T.dot(MApi)).dot(MApi.T).dot(MAyk)

    a = MA[0].dot(MAxk[0]) + MA[1].dot(0)
    MAy = ([a])

    for i in range(1,len(MAxk)):
        a = MA[0].dot(MAxk[i]) + MA[1].dot(MAxk[i-1])
        MAy = np.insert(MAy,i,a)
    
    dataMA = np.vstack((MAxk.T, MAy)).T

    num = [1] 
    den = MA.A1 #merubah menjadi rank 1
    den = list(den) #list ==> menambah koma diantara elements
    sys = signal.TransferFunction(num, den, dt=1) # selalu menghasilkan tf dg s pangkat tertinggi berubah menjadi (s^n),
                                                  # sehingga hasil tersebut merupakan angka hasil bagi den[0]
                                                  # misal 1/4s^2+2s+1 menjadi 0.25/s^2+0.5s+0.25
                                                  # aku sudah mensimulasikannya hasilnya sama, secara matematis dan logika pun juga sama
                                                  # jika menemukan solusinya silahkan PR ke https://github.com/ahmaddidiks/pis_py
    
    print(" MAxk1 = ")
    print(MAxk1)
    print("\n MApi = ")
    print(MApi)
    print("\n MA = ")
    print(MA)
    print("\n MAy = ")
    print(MAy)
    print("\n dataMA = ")
    print(dataMA)
    print("\n Transfer Fungsi = ")
    print(sys)

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
    #cara berfikir dimatlab berbeda dengan dipython
    #MAx/yk matlab = MAx/yk.T python
    MAxk  = np.transpose(np.matrix(Vin2)) #transpose matrix 1D
    MAyk  = np.transpose(np.matrix(Vout2))
    
    MAxk1 = Vin2.copy()
    MAxk1 = np.insert(MAxk1,0,0)
    MAxk1 = np.delete(MAxk1,len(MAxk1)-1)
    MAxk1 = np.transpose(np.matrix(MAxk1))

    MAxk2 = Vin2.copy()
    MAxk2 = np.insert(MAxk2,0,0)
    MAxk2 = np.insert(MAxk2,1,0)
    MAxk2 = np.delete(MAxk2,len(MAxk2)-1)
    MAxk2 = np.delete(MAxk2,len(MAxk2)-1)
    MAxk2 = np.transpose(np.matrix(MAxk2))

    MApi  = (np.vstack((MAxk.T, MAxk1.T, MAxk2.T))).T #tidka bisa langsung
    MA = np.linalg.inv(MApi.T.dot(MApi)).dot(MApi.T).dot(MAyk)
    
    a = MA[0].dot(MAxk[0]) + MA[1].dot(0) + MA[2].dot(0)
    MAy = ([a])
    a = MA[0].dot(MAxk[1]) + MA[1].dot(MAy[0]) + MA[2].dot(0)
    MAy = np.insert(MAy,1,a)

    for i in range(2,len(MAxk)):
        a = MA[0].dot(MAxk[i]) + MA[1].dot(MAxk[i-1]) + MA[2].dot(MAxk[i-2])
        MAy = np.insert(MAy,i,a)
    
    dataMA = np.vstack((MAxk.T,MAy)).T

    num = [1] 
    den = MA.A1 #merubah menjadi rank 1
    den = list(den) #list ==> menambah koma diantara elements
    sys = signal.TransferFunction(num, den, dt=1) # selalu menghasilkan tf dg s pangkat tertinggi berubah menjadi (s^n),
                                                  # sehingga hasil tersebut merupakan angka hasil bagi den[0]
                                                  # misal 1/4s^2+2s+1 menjadi 0.25/s^2+0.5s+0.25
                                                  # aku sudah mensimulasikannya hasilnya sama, secara matematis dan logika pun juga sama
                                                  # jika menemukan solusinya silahkan PR ke https://github.com/ahmaddidiks/pis_py
    
    print(" MAxk1 = ")
    print(MAxk1)
    print("\n MAxk2 = ")
    print(MAxk2)
    print("\n MApi = ")
    print(MApi)
    print("\n MA = ")
    print(MA)
    print("\n MAy = ")
    print(MAy)
    print("\n dataMA = ")
    print(dataMA)
    print("\n Transfer Fungsi = ")
    print(sys)

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
    #cara berfikir dimatlab berbeda dengan dipython
    #ARMAx/yk matlab = ARMAx/yk.T python
    ARMAxk  = np.transpose(np.matrix(Vin1)) #transpose matrix 1D
    ARMAyk  = np.transpose(np.matrix(Vout1))

    ARMAxk1 = Vin1.copy()
    ARMAxk1 = np.insert(ARMAxk1,0,0)
    ARMAxk1 = np.delete(ARMAxk1,len(ARMAxk1)-1)
    ARMAxk1 = np.transpose(np.matrix(ARMAxk1))
    
    ARMAyk1 = Vout1.copy()
    ARMAyk1 = np.insert(ARMAyk1,0,0)
    ARMAyk1 = np.delete(ARMAyk1,len(ARMAyk1)-1)
    ARMAyk1 = np.transpose(np.matrix(ARMAyk1))

    ARMApi = np.vstack((ARMAxk.T, ARMAxk1.T, ARMAyk1.T)).T #tidak bisa langsung
    ARMA = np.linalg.inv(ARMApi.T.dot(ARMApi)).dot(ARMApi.T).dot(ARMAyk)

    a = ARMA[0].dot(ARMAxk[0]) + ARMA[1].dot(0) +ARMA[2].dot(0)
    ARMAy = ([a])

    for i in range(1,len(ARMAxk)):
        a = ARMA[0].dot(ARMAxk[i]) + ARMA[1].dot(ARMAxk[i-1]) + ARMA[2].dot(ARMAy[i-1])
        ARMAy = np.insert(ARMAy,i,a)
    
    dataARMA = np.vstack((ARMAxk.T,ARMAy)).T

    num = [1] 
    den = ARMA.A1 #merubah menjadi rank 1
    den = list(den) #list ==> menambah koma diantara elements
    sys = signal.TransferFunction(num, den, dt=1) #selalu menghasilkan tf dg s pangkat tertinggi berubah menjadi (s^n),
                                                  # sehingga hasil tersebut merupakan angka hasil bagi den[0]
                                                  # misal 1/4s^2+2s+1 menjadi 0.25/s^2+0.5s+0.25 
                                                  # aku sudah mensimulasikannya hasilnya sama, secara matematis dan logika pun juga sama
                                                  # jika menemukan solusinya silahkan PR ke https://github.com/ahmaddidiks/pis_py

    print(" ARMAxk1 = ")
    print(ARMAxk1)
    print("\n ARMAyk1 = ")
    print(ARMAyk1)
    print("\n ARMApi = ")
    print(ARMApi)
    print("\n ARMA = ")
    print(ARMA)
    print("\n ARMAy = ")
    print(ARMAy)
    print("\n dataARMA = ")
    print(dataARMA)
    print("\n Transfer Fungsi = ")
    print(sys)

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
    #cara berfikir dimatlab berbeda dengan dipython
    #ARMAx/yk matlab = ARMAx/yk.T python
    ARMAxk  = np.transpose(np.matrix(Vin2)) #transpose matrix 1D
    ARMAyk  = np.transpose(np.matrix(Vout2))

    ARMAxk1 = Vin2.copy()
    ARMAxk1 = np.insert(ARMAxk1,0,0)
    ARMAxk1 = np.delete(ARMAxk1,len(ARMAxk1)-1)
    ARMAxk1 = np.transpose(np.matrix(ARMAxk1))

    ARMAxk2 = Vin2.copy()
    ARMAxk2 = np.insert(ARMAxk2,0,0)
    ARMAxk2 = np.insert(ARMAxk2,1,0)
    ARMAxk2 = np.delete(ARMAxk2,len(ARMAxk2)-1)
    ARMAxk2 = np.delete(ARMAxk2,len(ARMAxk2)-1)
    ARMAxk2 = np.transpose(np.matrix(ARMAxk2))

    ARMAyk1 = Vout2.copy()
    ARMAyk1 = np.insert(ARMAyk1,0,0)
    ARMAyk1 = np.delete(ARMAyk1,len(ARMAyk1)-1)
    ARMAyk1 = np.transpose(np.matrix(ARMAyk1))

    ARMAyk2 = Vout2.copy()
    ARMAyk2 = np.insert(ARMAyk2,0,0)
    ARMAyk2 = np.insert(ARMAyk2,1,0)
    ARMAyk2 = np.delete(ARMAyk2,len(ARMAyk2)-1)
    ARMAyk2 = np.delete(ARMAyk2,len(ARMAyk2)-1)
    ARMAyk2 = np.transpose(np.matrix(ARMAyk2))

    ARMApi = np.vstack((ARMAxk.T, ARMAxk1.T, ARMAxk2.T, ARMAyk1.T, ARMAyk2.T)).T #tidak bisa langsung

    ARMA = np.linalg.inv(ARMApi.T.dot(ARMApi)).dot(ARMApi.T).dot(ARMAyk)

    a = ARMA[0].dot(ARMAxk[0]) + ARMA[1].dot(0) + ARMA[2].dot(0) + ARMA[4].dot(0)
    ARMAy = ([a])
    
    a = ARMA[0].dot(ARMAxk[1]) + ARMA[1].dot(ARMAxk[0]) + ARMA[2].dot(0) + ARMA[3].dot(ARMAy[0]) + ARMA[4].dot(0)
    ARMAy = np.insert(ARMAy,1,a)

    for i in range(2,len(ARMAxk)):
        a = ARMA[0].dot(ARMAxk[i]) + ARMA[1].dot(ARMAxk[i-1]) + ARMA[2].dot(ARMAxk[i-2]) + ARMA[3].dot(ARMAy[i-1]) + ARMA[4].dot(ARMAy[i-2])
        ARMAy = np.insert(ARMAy,i,a)
    
    
    dataARMA = np.vstack((ARMAxk.T,ARMAy)).T

    num = [1] 
    den = ARMA.A1 #merubah menjadi rank 1
    den = list(den) #list ==> menambah koma diantara elements
    sys = signal.TransferFunction(num, den, dt=1) #selalu menghasilkan tf dg s pangkat tertinggi berubah menjadi (s^n),
                                                  # sehingga hasil tersebut merupakan angka hasil bagi den[0]
                                                  # misal 1/4s^2+2s+1 menjadi 0.25/s^2+0.5s+0.25 
                                                  # aku sudah mensimulasikannya hasilnya sama, secara matematis dan logika pun juga sama
                                                  # jika menemukan solusinya silahkan PR ke https://github.com/ahmaddidiks/pis_py

    print(" ARMAxk1 = ")
    print(ARMAxk1)
    print("\n ARMAyk1 = ")
    print(ARMAyk1)
    print(" ARMAxk2 = ")
    print(ARMAxk2)
    print("\n ARMAyk2 = ")
    print(ARMAyk2)
    print("\n ARMApi = ")
    print(ARMApi)
    print("\n ARMA = ")
    print(ARMA)
    print("\n ARMAy = ")
    print(ARMAy)
    print("\n dataARMA = ")
    print(dataARMA)
    print("\n Transfer Fungsi = ")
    print(sys)

    plt.plot(ARMAxk, ARMAy)
    plt.plot(Vin2, Vout2)
    plt.title('Hubungan Vin-Vout Metode ARMA Orde 2', fontdict=font)
    plt.xlabel('Vin', fontdict=font)
    plt.ylabel('Vout', fontdict=font)
    plt.legend(['ARMA', 'Data'])
    plt.show()