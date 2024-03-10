import numpy as np
import matplotlib.pyplot as plt

# f =< fs/2 musi być spełniony ten warunek

f =  14 #częstotliwość sygnału

fs = 22050# częstotliwość próbkowania

Tc = 1 #czas trwania sygnału

N = Tc * fs #liczba próbek

Ts = 1/fs #Okres próbkowania

n = np.arange(N) #n = wektor od 0 co 1 do wartości N-1

t = n/fs
#Funkcja 5 z tabeli 4 zadanie 4
# k [1 , 2 , 3]
#H = np.array([2,20,40])
#Generowanie wektorów których wartości stosuje do obliczenia sumy
#Dla wartości zadanych 
H1 = np.arange(1, 3, 1)

H2 = np.arange(1, 21, 1)

H3 = np.arange(1, 41, 1)

#Obliczanie zadania z wykorzystaniem pętli zostało porzucone ze względu na
# to że obliczenia trwały parę minut O_O

# for x in t:
#     for h in H1:
#         b1 = np.sum((-1)**h)/(3 * h**2) * np.cos(2 * np.pi * h * t + np.sin(6 * np.pi *t))

# plt.plot(t,b1)
# plt.show()

# for x in t:
#     for h in H2:
#         b2 = np.sum((-1)**h)/(3 * h**2) * np.cos(2 * np.pi * h * t + np.sin(6 * np.pi *t))

# plt.plot(t,b2)
# plt.show()

# for x in t:
#     for h in H3:
#         b3 = np.sum((-1)**h)/(3 * h**2) * np.cos(2 * np.pi * h * t + np.sin(6 * np.pi *t))

# plt.plot(t,b3)
# plt.show()

# Obliczenia wektorowe

T, H = np.meshgrid(t, H1)

b1t = np.sum((-1)**H / (3 * H**2) * np.cos(2 * np.pi * H * T + np.sin(6 * np.pi * T)), axis=0)

plt.plot(t,b1t)
plt.show()

T, H = np.meshgrid(t, H2)

b2t = np.sum((-1)**H / (3 * H**2) * np.cos(2 * np.pi * H * T + np.sin(6 * np.pi * T)), axis=0)

plt.plot(t,b2t)
plt.show()

T, H = np.meshgrid(t, H3)

b3t = np.sum((-1)**H / (3 * H**2) * np.cos(2 * np.pi * H * T + np.sin(6 * np.pi * T)), axis=0)

plt.plot(t,b3t)
plt.show()