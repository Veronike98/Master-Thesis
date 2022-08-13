from cmath import sqrt
import numpy as np
from matplotlib import rc
import matplotlib.pyplot as plt
import scipy as sp

# Font
plt.rcParams.update({'font.size': 11})

import os
os.environ["PATH"] += os.pathsep + '/Library/TeX/texbin'
rc('font', **{'family': 'serif', 'serif': ['Computer Modern']})
rc('text', usetex=True)

# Colors
turquoise = (0, 247 / 255, 230 / 255)
goldenyellow = (1, 218 / 255, 66 / 255)
fuchsia= (1, 0, 172 / 255)

# Costanti fisiche in units SU (da NIST)

G = 6.674e-11
h = 6.626e-34
hbar = h / (2 * np.pi)
c = 2.997e8
k = 1.381e-23

# Parametri del modello
L = 10
L0 = 1
W1 = 0.1
W2 = 0.8


# Beta functions

#Minimal functions
@np.vectorize 
def f(x):
    f = np.cosh(W1 * (x - L0)) - (np.sinh(W1 * (x - L0)) / np.tanh(W1 * (L - L0)))
    return np.where(x < L0, 1, f)

def phi(x):
    phi = np.sinh(W2 * x) / np.sinh(W2 * L0)
    return np.where(x > L0, 1, phi)

def I(x, m):
    return np.where(x < L0, 1, sp.special.betainc(m, m, (L - x)/(L - L0)))

def phi(x, m):
    return np.where(x > L0, 1, sp.special.betainc(m, m, x / L0))
#################################################### Primo grafico

x = np.arange(0, L, 0.1)

# m = 14
y2 = I(x, 3)
plt.plot(x, y2, color=goldenyellow, label=r'$m = 3$', linestyle='dashed')

# m = 22
y3 = I(x, 22)
plt.plot(x, y3, color=fuchsia, label=r'$m = 22$', linestyle='dashdot')

# m = 1
y1 = I(x, 1)
plt.plot(x, y1, color=turquoise, label=r'$m = 1$')

# Label axis
plt.xlabel(r'$\lambda$')
# plt.ylabel(r'Rate $[\si{\second}^{-1}]$')
plt.ylabel(r'')

# Title
plt.title(r'$f_{\ell_0 = 1, \ell = 10}$')

# Show Legend
plt.legend()

plt.savefig('../Immagini/beta-functions.png')
plt.show()

#################################################### Secondo grafico

# f
y1 = I(x, 14) * phi(x, 14)
plt.plot(x, y1, color=goldenyellow, label=r'$f\cdot\varphi$')

# f
y2 = I(x, 14)
plt.plot(x, y2, color=turquoise, label=r'$f$', linestyle=(0, (3, 2, 1, 2)), linewidth=2.3)

# phi
y3 = phi(x, 14)
plt.plot(x, y3, color=fuchsia, label=r'$\varphi$', linestyle=(0, (3, 3, 1, 3)))

# Label axis
plt.xlabel(r'$\lambda$')
# plt.ylabel(r'Rate $[\si{\second}^{-1}]$')
plt.ylabel(r'')

# Title
plt.title(r'$f$ and $\varphi$')

# Show Legend
plt.legend()

plt.savefig('../Immagini/beta-functions-proof-bound.png')
plt.show()

# #####################################################