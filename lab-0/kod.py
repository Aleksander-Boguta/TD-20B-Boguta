import numpy as np
import matplotlib.pyplot as plt

X = np.arange(-100,100,0.5)
plt.style.use('Solarize_Light2')
plt.title('Funkcja kwadratowa')
plt.plot(X,X*X)

plt.show()
