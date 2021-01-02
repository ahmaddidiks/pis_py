#!/usr/bin/env python

from data import *

# METODE LEAST SQUARE DENGAN STRUKTUR AUTO REGRESSIVE (ORDE 1)
# Metode Auto Regresive atau (AR) Merupakan penghitungan parameter model 
# sistem dengan persamaan dasar *y(k)=b0*x(k)+a0*y(k-1)*
def autoRegresiveOrde1():
    #cara berfikir dimatlab berbeda dengan dipython
    ARxk_t = Vin1.copy()
    ARxk  = np.transpose(np.matrix(Vin1)) #transpose matrix 1D
    ARyk  = np.transpose(np.matrix(Vin2))
    ARykTemp = Vout1.copy()
    ARykTemp1 = np.insert(ARykTemp, 0, 0)
    ARyk_t = np.delete(ARykTemp1, 5)
    ARyk1 = np.transpose(np.matrix(ARyk_t))
    ARpiTemp  = np.vstack((ARxk_t, ARyk_t))
    ARpi = ARpiTemp.T
   # AR    = np.linalg.inv(ARpi.T * ARpi) * ARpi.T * ARyk

    #print(ARyk1)
    #print(ARpiTemp)
    print(ARpi)


#autoRegresiveOrde1()



#percobaan1()
#print(len(ARyk))
#% ARxk  = Vin1';
#% ARyk  = Vout1'; 
#% ARyk1 = [0;ARyk(1:length(ARyk)-1)];
#% ARpi  = [ARxk ARyk1]
#% AR    = inv(ARpi'*ARpi)*ARpi'*ARyk
#% ARy(1)= AR(1)*ARxk(1)+AR(2)*0;
#% for k=2:length(ARxk);
#%     ARy(k)=AR(1)*ARxk(k)+AR(2)*ARy(k-1);    
#% end
#% DataAR = [ARxk ARy']
#% figure('Name','Hubungan Vin-Vout Metode AR Orde 1','NumberTitle','off')
#% plot(ARxk,ARy,'red',Vin1,Vout1,'blue')
#% xlabel('Vin')
#% ylabel('Vout')
#% title('Hubungan Vin-Vout Metode AR Orde 1')
#% legend('AR','Data')
#% legend('boxoff')
#% sys = tf(1,AR',1);