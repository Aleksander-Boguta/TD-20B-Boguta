import numpy as np
import matplotlib.pyplot as plt



N = 4
n = np.arange(N)
k = np.arange(N).reshape(-1,1) 
#pionizacja wektora k. pozwoli to uzyskać macierz X(k)
# gdzie:
#       | X(1)
# X(k)= | X(2)
#       | X(3)

x = np.array([-4,-2,1,3])



#Składowa stała : zawsze liczba całkowita 



X = x * np.exp((-2j * np.pi * n * k)/N) 


xk = np.sum(X, axis = 1) 
#Sumowanie wyrazów każdego wiersza, gdzie każdy wyraz to składowa sumy
#macierz X można rozumieć tak że numer wiersza to ten sam numer który odpowiada k
# a numer kolumny odpowiada n

print(xk)

print("------------------")

# print(X)
