from math import factorial
import numpy as np
from matplotlib import cm
import matplotlib.pyplot as plt
import scipy.special as sp
from scipy.optimize import fsolve

import plotly.graph_objects as go
import plotly.subplots as sub
from typing import Tuple, Iterable

# from mpl_toolkits import mplot3d

m = 1
Q0 = 40
Q1= 10
r0 = -0.1

A = 1 / 2 - factorial(2 * m)**4 / (4 * factorial(4 * m) * factorial(m)**4)
B = factorial(2 * m - 2)**2 * factorial(2 * m - 1)**2 / (factorial(4* m - 3) * factorial(m - 1))
C = factorial(2 * m - 2) * factorial(2 * m - 1) / (factorial(m - 1)**2)

@np.vectorize
def V(x, y):
    if (x == 0): return 100
    if (y == 0): return -100
    if (x == y): return 100
    z = (A - 1) * r0 * y + Q1 * C / (y**(2 * m - 1)) + Q0 * A * x + 2 * B / (x - y) + Q1 * C / ((x - y)**(2 * m - 1))
    return z

##################################################### Grafico 1: V_beta

# create figure
fig = sub.make_subplots(rows=1, cols=1, specs=[[{'type': 'surface'}]])

X = np.arange(0.1, 10, 0.1)
Y = np.arange(0.1, 10, 0.1) 
X, Y = np.meshgrid(X, Y)
Z = V(X, Y)

surface = go.Surface(x = X, y = Y, z = Z, colorscale = "YlOrRd")
fig.add_trace(surface, row=1, col=1)


# Label axes
fig.update_layout(scene = dict(
                    xaxis_title='l',
                    yaxis_title='l_0',
                    zaxis_title='V'))
fig.show()