%% Program Praktikum PIS (OFFLINE)
% Merupakan program matlab untuk mengidentifikasikan parameter dari sebuah
% transfer function diskrit yang dihitung secara offline. Disusun oleh
% asisten praktikum PIS (Pemodelan dan Identifikasi Sistem) Tahun ajaran
% 2019/2020:
% 

%% Data Identifikasi
% Berisi data input dan output dari plant yang akan diidentifikasi.
clc; clear;

disp('Data Orde 1');
Vin1  = [2.05 3.24 4.74 4.93 5.05];
Vout1 = [2.2 9.2 6.2 6.2 60.2]; 
D1 = [Vin1' Vout1']
figure('Name','Grafik Hubungan Vin-Vout Orde 1','NumberTitle','off')
plot(Vin1,Vout1)
xlabel('Vin')
ylabel('Vout')
legend('Data')
legend('boxoff')
title('Grafik Hubungan Vin-Vout Orde 1')

% disp('Data Orde 2');
% Vin2  = [2.14 3.23 4.11 4.63 5.1];
% Vout2 = [12 22 32 42 62];
% D2 = [Vin2' Vout2']
% figure('Name','Grafik Hubungan Vin-Vout Orde 2','NumberTitle','off')
% plot(Vin2,Vout2)
% xlabel('Vin')
% ylabel('Vout')
% legend('Data')
% legend('boxoff')
% title('Grafik Hubungan Vin-Vout Orde 2')

% %% METODE LEAST SQUARE DENGAN STRUKTUR AUTO REGRESSIVE (ORDE 1)
% % Metode Auto Regresive atau (AR) Merupakan penghitungan parameter model 
% % sistem dengan persamaan dasar *y(k)=b0*x(k)+a0*y(k-1)*

% ARxk  = Vin1';
% ARyk  = Vout1'; 
% ARyk1 = [0;ARyk(1:length(ARyk)-1)];
% ARpi  = [ARxk ARyk1]
% AR    = inv(ARpi'*ARpi)*ARpi'*ARyk
% ARy(1)= AR(1)*ARxk(1)+AR(2)*0;
% for k=2:length(ARxk);
%     ARy(k)=AR(1)*ARxk(k)+AR(2)*ARy(k-1);    
% end
% DataAR = [ARxk ARy']
% figure('Name','Hubungan Vin-Vout Metode AR Orde 1','NumberTitle','off')
% plot(ARxk,ARy,'red',Vin1,Vout1,'blue')
% xlabel('Vin')
% ylabel('Vout')
% title('Hubungan Vin-Vout Metode AR Orde 1')
% legend('AR','Data')
% legend('boxoff')
% sys = tf(1,AR',1);
 
% %% METODE LEAST SQUARE DENGAN STRUKTUR AUTO REGRESSIVE (ORDE 2)
% % Metode Auto Regresive atau (AR) Merupakan penghitungan parameter model 
% % sistem dengan persamaan dasar *y(k)=b0*x(k)+a0*y(k-1)+a1*y(k-2)*

% ARxk  = Vin2';
% ARyk  = Vout2'; 
% ARyk1 = [0;ARyk(1:length(ARyk)-1)];
% ARyk2 = [0;0;ARyk(1:length(ARyk)-2)];
% ARpi  = [ARxk ARyk1 ARyk2]
% AR    = inv(ARpi'*ARpi)*ARpi'*ARyk
% 
% ARy(1)=AR(1)*ARxk(1)+AR(2)*0+AR(3)*0;
% ARy(2)=AR(1)*ARxk(2)+AR(2)*ARy(1)+AR(3)*0;
% for k=3:length(ARxk);
%     ARy(k)=AR(1)*ARxk(k)+AR(2)*ARy(k-1)+AR(3)*ARy(k-2);    
% end
% DataAR = [ARxk ARy']
% figure('Name','Hubungan Vin-Vout Metode AR Orde 2','NumberTitle','off')
% plot(ARxk,ARy,'red',Vin2,Vout2,'blue')
% xlabel('Vin')
% ylabel('Vout')
% title('Hubungan Vin-Vout Metode AR Orde 2')
% legend('AR','Data')
% legend('boxoff')
% sys = tf(1,AR',1);

% %% METODE LEAST SQUARE DENGAN STRUKTUR MOVING AVERAGE (ORDE 1)
% % Metode Moving Average atau (MA) Merupakan penghitungan parameter model 
% % sistem dengan persamaan dasar *y(k)=b0*x(k)+b1*x(k-1)*

% MAxk  = Vin1';
% MAyk  = Vout1'; 
% MAxk1 = [0;MAxk(1:length(MAxk)-1)];
% MApi  = [MAxk MAxk1]
% MA    = inv(MApi'*MApi)*MApi'*MAyk
% 
% MAy(1)=MA(1)*MAxk(1)+MA(2)*0;
% for k=2:length(MAxk);
%     MAy(k)=MA(1)*MAxk(k)+MA(2)*MAxk(k-1);    
% end
% DataMA = [MAxk MAy']
% figure('Name','Hubungan Vin-Vout Metode MA Orde 1','NumberTitle','off')
% plot(MAxk,MAy,'green',Vin1,Vout1,'blue')
% xlabel('Vin')
% ylabel('Vout')
% title('Hubungan Vin-Vout Metode MA Orde 1')
% legend('MA','Data')
% legend('boxoff')
% sys = tf(1,MA',1);

% %% METODE LEAST SQUARE DENGAN STRUKTUR MOVING AVERAGE (ORDE 2)
% % Metode Moving Average atau (MA) Merupakan penghitungan parameter model 
% % sistem dengan persamaan dasar *y(k)=b0*x(k)+b1*x(k-1)+b2*x(k-2)*
% 
% MAxk  = Vin2';
% MAyk  = Vout2'; 
% MAxk1 = [0;MAxk(1:length(MAxk)-1)];
% MAxk2 = [0;0;MAxk(1:length(MAxk)-2)];
% MApi  = [MAxk MAxk1 MAxk2]
% MA    = inv(MApi'*MApi)*MApi'*MAyk
% 
% MAy(1)=MA(1)*MAxk(1)+MA(2)*0+MA(3)*0;
% MAy(2)=MA(1)*MAxk(2)+MA(2)*MAy(1)+MA(3)*0;
% for k=3:length(MAxk);
%     MAy(k)=MA(1)*MAxk(k)+MA(2)*MAxk(k-1)+MA(3)*MAxk(k-2);    
% end
% DataMA = [MAxk MAy']
% figure('Name','Hubungan Vin-Vout Metode MA Orde 2','NumberTitle','off')
% plot(MAxk,MAy,'green',Vin2,Vout2,'blue')
% xlabel('Vin')
% ylabel('Vout')
% title('Hubungan Vin-Vout Metode MA Orde 2')
% legend('MA','Data')
% legend('boxoff')
% sys = tf(1,MA',1);

%% METODE LEAST SQUARE DENGAN STRUKTUR AUTO REGRESSIVE MOVING AVERAGE (ORDE 1)
% Metode Auto Regresive Moving Average (ARMA) Merupakan penghitungan 
% parameter model sistem dengan persamaan dasar 
% *y(k)=b0*x(k)+b1*x(k-1)+a0*y(k-1)*

ARMAxk  = Vin1';
ARMAyk  = Vout1'; 
ARMAxk1 = [0;ARMAxk(1:length(ARMAxk)-1)];
ARMAyk1 = [0;ARMAyk(1:length(ARMAyk)-1)];
ARMApi  = [ARMAxk ARMAxk1 ARMAyk1]
ARMA    = inv(ARMApi'*ARMApi)*ARMApi'*ARMAyk

ARMAy(1)=ARMA(1)*ARMAxk(1)+ARMA(2)*0+ARMA(3)*0;
for k=2:length(ARMAxk);
    ARMAy(k)=ARMA(1)*ARMAxk(k)+ARMA(2)*ARMAxk(k-1)+ARMA(3)*ARMAy(k-1);    
end
DataARMA = [ARMAxk ARMAy']
figure('Name','Hubungan Vin-Vout Metode ARMA Orde 1','NumberTitle','off')
plot(ARMAxk,ARMAy,'black',Vin1,Vout1,'blue')
xlabel('Vin')
ylabel('Vout')
title('Hubungan Vin-Vout Metode ARMA Orde 1')
legend('ARMA','Data')
legend('boxoff')
sys = tf(1,ARMA',1);
% 
%% METODE LEAST SQUARE DENGAN STRUKTUR AUTO REGRESSIVE MOVING AVERAGE (ORDE 2)
% Metode Auto Regresive Moving Average (ARMA) Merupakan penghitungan 
% parameter model sistem dengan persamaan dasar 
% *y(k)=b0*x(k)+b1*x(k-1)+b2*x(k-2)+a0*y(k-1)+a1*y(k-2)*

% ARMAxk  = Vin2';
% ARMAyk  = Vout2'; 
% ARMAxk1 = [0;ARMAxk(1:length(ARMAxk)-1)];
% ARMAxk2 = [0;0;ARMAxk(1:length(ARMAxk)-2)];
% ARMAyk1 = [0;ARMAyk(1:length(ARMAyk)-1)];
% ARMAyk2 = [0;0;ARMAyk(1:length(ARMAyk)-2)];
% ARMApi  = [ARMAxk ARMAxk1 ARMAxk2 ARMAyk1 ARMAyk2]
% ARMA    = inv(ARMApi'*ARMApi)*ARMApi'*ARMAyk
% 
% ARMAy(1)=ARMA(1)*ARMAxk(1)+ARMA(2)*0+ARMA(3)*0+ARMA(4)*0+ARMA(5)*0;
% ARMAy(2)=ARMA(1)*ARMAxk(2)+ARMA(2)*ARMAxk(1)+ARMA(3)*0+ARMA(4)*ARMAy(1)+...
%     ARMA(5)*0;
% for k=3:length(ARMAxk);
%     ARMAy(k)=ARMA(1)*ARMAxk(k)+ARMA(2)*ARMAxk(k-1)+ARMA(3)*ARMAxk(k-2)+...
%         ARMA(4)*ARMAy(k-1)+ARMA(5)*ARMAy(k-2);    
% end
% DataARMA = [ARMAxk ARMAy']
% figure('Name','Hubungan Vin-Vout Metode ARMA Orde 2','NumberTitle','off')
% plot(ARMAxk,ARMAy,'black',Vin2,Vout2,'blue')
% xlabel('Vin')
% ylabel('Vout')
% title('Hubungan Vin-Vout Metode ARMA Orde 2')
% legend('ARMA','Data')
% legend('boxoff')
% sys = tf(1,ARMA',1);