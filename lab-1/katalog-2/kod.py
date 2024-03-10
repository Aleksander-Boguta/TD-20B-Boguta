import numpy as np
import matplotlib.pyplot as plt

# f =< fs/2 musi być spełniony ten warunek

phi = 0  #Przesunięcie

f =  14 #częstotliwość sygnału

fs = 8000 # częstotliwość próbkowania

Tc = 1 #czas trwania sygnału

N = Tc * fs #liczba próbek

Ts = 1/fs #Okres próbkowania

#n =   #wektor od 0 co 1 do wartości N-1

n = np.arange(N)

t = n/fs

print(np.max(n)) #sprawdzam czy faktycznie największy(w domyśle ostatni wyraz wektora) jest równy N - 1

#Funkcja 5 z tabeli 1 zadanie 1

xt = np.sin(2 * np.pi * f * t * np.cos(3 * np.pi * t) + t * phi)

# plt.plot(t,xt)
# plt.show()

#-------------------------------------------------------------------------------------------------------


#Zestaw funkcji 5 z tabeli 2 zadanie 2



yt = (2 * t * np.sin(0.5 * t * np.pi) + 1.5) * np.cos(9 * np.pi * t + np.pi * t)

zt = yt * xt + np.abs(xt + 2) * (yt**2 + 0.32)

vt = np.sqrt(np.abs(xt * zt+ 10)) * (np.abs(yt) + 1.2) * np.sin(2 * np.pi * t)


plt.plot(t,yt)
plt.show()
plt.plot(t,zt)
plt.show()
plt.plot(t,vt)
plt.show()