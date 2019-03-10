import scipy
from scipy.fftpack import fft
import numpy as np
import matplotlib.pyplot as plt


# seems that increasing N will not affact the spectrum, 
# which means the magnitude of each frequency component is really power, not energy
N=60000

T = 1.0/800.0
x = np.linspace(0.0, N*T, N)
y = np.sin(50.0 * 2.0 * np.pi * x) + 0.5 * np.sin(100.0 * 2.0 * np.pi *x)
yf = fft(y)
xf = np.linspace(0.0, 1.0/(2.0*T), N/2)

plt.plot(xf, 2.0/N * np.abs(yf[0:N/2]))
plt.grid()
plt.show()
