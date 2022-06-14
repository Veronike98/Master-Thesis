from cmath import sqrt
import numpy as np
# from matplotlib import cm
import matplotlib.pyplot as plt

# Costanti fisiche in units SU (da NIST)

G = 6.674e-11
h = 6.626e-34
hbar = h / (2 * np.pi)
c = 2.997e8
k = 1.381e-23

# Parametri del modello
xi = 1 / 6
alpha = 4 * np.pi * np.sqrt(np.pi) / 3 * xi
gamma = 32 * np.pi**6 / 405 * xi**3
r = 2.7e-7 / (2.7e-7)
b = 1e-5

const1 =  b * (8 * np.pi)**3 * G / hbar**2 * k**3 / c**5
const2 = k**4 * G**(3 / 2) / (hbar**(5 / 2) * c**(15 / 2))

A_1 = 2 * np.pi * sqrt(np.pi) / 3 * xi * G * k**2 / (2)
B_1 = (8 * np.pi)**4 / 3 * r * (2.7e-4) * G * k**4 / (c**4 * hbar**3)
B_2 = G**(3 / 2) / (hbar**(5 / 2) * c**(15 / 2)) * k**4 * np.sqrt(64 / 1215 * np.pi**6 * xi**3)

def rate(x):
    y = const1 * x**3
    return y

def bound_min(x):
    y = 20 * np.sqrt(alpha * r) * const1 * x**3 + np.sqrt(2 / 3 * gamma) * const2 * x**4
    return y 

def bound_const(x, l_0):
    y = A_1 / l_0 * x**2 + (B_1 * l_0 + B_2) * x**4
    return y

print('T per 4-pow:')
print(20 * np.sqrt(alpha * r) * const1 / (np.sqrt(2 / 3 * gamma) * const2))
#################################################### Primo grafico: rate e bound in scala lineare

# Rate
x = np.arange(0, 1e2, 0.1)
y = rate(x)
plt.plot(x, y, color='cyan', label=r'Evaporation rate')

# Bound
y2 = bound_min(x)
plt.plot(x, y2, color='orange', label=r'Upper Bound')

# Bound classico
y0 = [0.] * len(x)
plt.plot(x, y0, color='red', linestyle='dashed')

# Label axis
# plt.xlabel(r'Temperature $[\si{\kelvin}]$')
plt.xlabel(r'Temperature')
# plt.ylabel(r'Rate $[\si{\second}^{-1}]$')
plt.ylabel(r'Rate')

# Title
plt.title(r'Comparison of evaporation rates')

# Show Legend
plt.legend()

# plt.savefig('../Immagini/p')
plt.show()

# ##################################################### Grafico 2: Bound minimale in log scale

# Rate
x = np.arange(10, 1e45, 1e40)
y = rate(x)
plt.plot(x, y, color='cyan', label=r'Evaporation rate')

# Bound
y2 = bound_min(x)
plt.plot(x, y2, color='orange', label=r'Upper Bound')

# Scala 
plt.yscale('log')
plt.xscale('log')

# Limiti del grafico
# plt.ylim(1e-64, 1e-43)
plt.xlim(10,1e45) 

# Label axis
# plt.xlabel(r'Temperature $[\si{\kelvin}]$')
plt.xlabel(r'Temperature')
# plt.ylabel(r'Rate $[\si{\second}^{-1}]$')
plt.ylabel(r'Rate')

# Title
plt.title(r'Comparison of evaporation rates')

# Show Legend
plt.legend()

# plt.savefig('../Immagini/p')
plt.show()


# ##################################################### Grafico 3: Bound con l_0 fisso

print('l-critical:')
print(A_1 * B_2 / (const1**2 / 4 - A_1 * B_1))

# Rate
L_0 = [1e-28, 1e-27, 1e-26]
x = np.arange(0, 1e-35, 1e-39)
y = rate(x)
plt.plot(x, y, color='cyan', label=r'Evaporation rate')

# Bound
for l in L_0:
    y2 = bound_const(x, l)
    plt.plot(x, y2, label=r'Upper Bound for $l_0 =$' + str(l))

# Bound classico
y0 = [0.] * len(x)
plt.plot(x, y0, color='red', linestyle='dashed')

# Label axis
# plt.xlabel(r'Temperature $[\si{\kelvin}]$')
plt.xlabel(r'Temperature')
# plt.ylabel(r'Rate $[\si{\second}^{-1}]$')
plt.ylabel(r'Rate')

# Title
plt.title(r'Comparison of evaporation rates')

# Show Legend
plt.legend()

# plt.savefig('../Immagini/p')
plt.show()