import numpy as np
import scipy.special
import matplotlib.pyplot as plt
import seaborn as sns

#generate array of x vallues
x = np.linspace(-15, 15, 400)

#compute normalized intensity
norm_I = 4 * (scipy.special.j1(x) / x)**2

# plot our computation
plt.close()
plt.plot(x, norm_I, marker='.', linestyle='none')
plt.margins(0.02)
plt.xlabel('$x$')
plt.ylabel('$I(x) / I_0$')

#processing the spike data.
data = np.loadtxt('data/retina_spikes.csv', skiprows = 2, delimiter=',')
t = data[:,0]
V = data[:,1]

#close all other plots just in complement_base
plt.close()
plt.plot(t, V)
plt.xlabel('t (ms)')
plt.ylabel('V (µV)')
plt.xlim(1395, 1400)
