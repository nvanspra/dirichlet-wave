#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  4 00:05:51 2021

@author: vanspran
"""

import numpy as np

import matplotlib as mpl
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

from scipy import linalg

dt = 0.01

Ew = np.fromfile('Ew.dat', float, sep=";")
N = np.size(Ew)
T = (N-1)*dt
t = np.linspace(0, T, N)

fig = plt.figure()
plt.plot(t, Ew)
plt.xlabel(r'Time $t$', fontsize=20)
plt.ylabel(r"Energy $\mathcal{E}(u(t), u'(t))$",fontsize=20)
plt.grid(True)