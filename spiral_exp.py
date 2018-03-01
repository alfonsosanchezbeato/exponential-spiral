#!/usr/bin/env python3
import math
import numpy as np
import cmath


# Calculates the values of w**z, w,z in C, up to num_sol
def calc_exponential_values(w, z, num_sol):
    c = cmath.exp(z*cmath.log(w))
    lr = []
    li = []
    for n in range(-num_sol//2, num_sol//2):
        r = c*cmath.exp(z*2*math.pi*1j*n)
        lr.append(r.real)
        li.append(r.imag)

    return lr, li


# Calculates values for a spiral that passes over the w**z solutions
def calc_exponential_spiral(w, z, shift, step, minv, maxv):
    c = cmath.exp(z*cmath.log(w))
    lr = []
    li = []
    for n in np.arange(minv, maxv, step):
        r = c*cmath.exp((z + shift)*2*math.pi*1j*n)
        lr.append(r.real)
        li.append(r.imag)

    return lr, li


# Add points to subplot (input is axes object)
def add_points_to_subplot(ax, r, i, style):
    ax.plot(r, i, style)
    ax.set_aspect('equal')
    ax.grid(True, which='both')
    ax.set_aspect('equal')

    # set the x-spine, attach ticks to it
    ax.spines['left'].set_position('zero')
    ax.yaxis.tick_left()

    # turn off the right spine/ticks
    ax.spines['right'].set_color('none')

    # set the y-spine
    ax.spines['bottom'].set_position('zero')
    ax.xaxis.tick_bottom()

    # turn off the top spine/ticks
    ax.spines['top'].set_color('none')
