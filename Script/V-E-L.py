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


Q0 = 0.1
Q1= 1000
r0 = -50

Omega1 = np.sqrt(Q0 / (2 + Q1))
Omega2 = np.sqrt(Q0 / Q1)


def coth(x):
    return np.cosh(x) / np.sinh(x)

@np.vectorize
def V(x, y):
    if (x == 0): return 100
    if (y == 0): return -100
    if (x == y): return 100
    z = np.sqrt(Q0 * (2 + Q1)) * coth(Omega1 * (x - y)) + np.sqrt(Q0 * Q1) * coth(Omega2 * y) - r0 * y
    return z

##################################################### Grafico 1: V_beta

# create figure
fig = sub.make_subplots(rows=1, cols=1, specs=[[{'type': 'surface'}]])

X = np.arange(1, 100, 1)
Y = np.arange(1, 20, 1) 
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