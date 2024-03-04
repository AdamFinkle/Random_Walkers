"""
Graphing functions to display simulation output.
"""

from os import system
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.patches as mpatches

def scatter_animation(data):
    """Create a scatterplot animation from an array of history grids."""
    def update_scatter(num, data):
        ax.cla()
        ax.plot(range(0, len(data[num])), data[num], 'o')
        ax.set_title("Animation of Tallies over Simulation")
        ax.set_ylabel("Cells")
        ax.set_xlabel("Walkers per Cell")
    fig, ax = plt.subplots(1, 1, constrained_layout=True)
    ax.plot(range(0, len(data[0])), data[0], 'o')
    ax.set_title("Animation of Tallies over Simulation")
    ax.set_ylabel("Cells")
    ax.set_xlabel("Walkers per Cell")
    return animation.FuncAnimation(fig, update_scatter, len(data),
                                   fargs=(data,), interval = 1)


def data_versus_model(data, model):
    """Plot a history grid and fit a Maxwell-Boltzmann curve to it."""
    fig, ax = plt.subplots(1, 1, constrained_layout=True)
    p1 = ax.plot(range(0, len(data)), data, 'o', color='r')
    p2 = ax.plot(range(0, len(model)), model, 'o', color='b')
    ax.set_title("Normalized Last Tallies versus" +
                  "\nMaxwell-Boltzmann Distribution")
    ax.set_ylabel("Cells")
    ax.set_xlabel("Walkers per Cell")
    red_patch = mpatches.Patch(color='red', label='Tallies')
    blue_patch = mpatches.Patch(color='blue', label='Distribution')
    ax.legend(handles=[red_patch, blue_patch])
    return fig
