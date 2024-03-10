import numpy as np
import matplotlib.pyplot as plt

# f =< fs/2 musi być spełniony ten warunek

f =  14 #częstotliwość sygnału

fs = 8000 # częstotliwość próbkowania

Tc = 0.5 #czas trwania sygnału

N = Tc * fs #liczba próbek

Ts = 1/fs #Okres próbkowania

#n =   #wektor od 0 co 1 do wartości N-1

n = np.arange(N)

t = n/fs

ut = t * np.sqrt(-t + 0.7) * np.sin(22 * np.pi * t * np.cos(t**2))

plt.plot(t,ut)
plt.show()
