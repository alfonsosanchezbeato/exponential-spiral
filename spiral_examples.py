#!/usr/bin/env python3
import spiral_exp as se
import matplotlib.pyplot as plt


def plot_exp_values(w, z, num, fname):
    fig, ax = plt.subplots()

    (r, i) = se.calc_exponential_values(w, z, num)
    se.add_points_to_subplot(ax, r, i, 'bo')

    plt.savefig(fname + '.svg')
    plt.show()


def plot_spirals(w, z, num_sol, shift, step, minv, maxv, fname):
    fig, ax = plt.subplots()

    for sh in shift:
        (r, i) = se.calc_exponential_spiral(w, z, sh, step, minv, maxv)
        se.add_points_to_subplot(ax, r, i, '--')

    (r, i) = se.calc_exponential_values(w, z, num_sol)
    se.add_points_to_subplot(ax, r, i, 'bo')

    plt.savefig(fname + '.svg')
    plt.show()


plot_spirals(2, 0.4 - 0.1j, 6, [-3, -4], 0.01, -3.3, 2.1, 'xx')


plot_exp_values(2., 0.2, 5, 'pentagon')
plot_spirals(2, 0.4 - 0.1j, 6, [0], 0.01, -3.3, 2.1, 'spiral0')
plot_spirals(2, 0.4 - 0.1j, 6, [0, -1], 0.01, -3.3, 2.1, 'spiral1')
plot_spirals(2, 0.4 - 0.1j, 6, [0, 1], 0.01, -3.3, 2.1, 'spiral2')
plot_spirals(2, 0.4 - 0.1j, 6, [0, -1, 1], 0.01, -3.3, 2.1, 'spiral3')
plot_spirals(2, 0.4 - 0.1j, 6, [-1, -2], 0.01, -3.3, 2.1, 'spiral4')
plot_spirals(10, 0.1j, 6, [0, -1, 1], 0.01, -3.3, 2.1, 'line0')
plot_spirals(1j, 0.1j, 6, [0, -1, 1], 0.01, -3.3, 2.1, 'line1')
