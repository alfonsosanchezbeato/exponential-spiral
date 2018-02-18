#!/usr/bin/env python3
import math
import numpy as np
import cmath
import matplotlib.pyplot as plt


# Plots the values of w**z, w,z in C, up to num_sol
def plot_exponential_values(w, z, num_sol):
    c = cmath.exp(z*cmath.log(w))
    lr = []
    li = []
    for n in range(-num_sol//2, num_sol//2):
        r = c*cmath.exp(z*2*math.pi*1j*n)
        lr.append(r.real)
        li.append(r.imag)
        print(cmath.polar(r))

    #plt.plot(lr, li, '--bo')
    plt.plot(lr, li, 'bo')


def plot_spiral(w, z, step, minv, maxv):
    c = cmath.exp(z*cmath.log(w))
    lr = []
    li = []
    for n in np.arange(minv, maxv, step):
        r = c*cmath.exp(z*2*math.pi*1j*n)
        lr.append(r.real)
        li.append(r.imag)
        print(cmath.polar(r))

    plt.plot(lr, li, '--')

def plot_spiral_left(w, z, step, minv, maxv):
    c = cmath.exp(z*cmath.log(w))
    lr = []
    li = []
    for n in np.arange(minv, maxv, step):
        r = c*cmath.exp((1 - z)*2*math.pi*1j*n)
        lr.append(r.real)
        li.append(r.imag)
        print(cmath.polar(r))

    plt.plot(lr, li, '--')

# plot_spiral(2, 0.0223 - 0.001j, 0.1)
# plot_exponential_values(2, 0.0223 - 0.001j, 500)
w = 2
z = 0.4 - 0.01j
plot_spiral(w, z, 0.01, -3, 2)
plot_spiral_left(w, z, 0.01, -2, 3)
plot_exponential_values(w, z, 5)
plt.show()
