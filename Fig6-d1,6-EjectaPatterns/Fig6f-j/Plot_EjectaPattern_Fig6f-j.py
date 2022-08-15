#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
@author: xizi

Plot a group of ejecta patterns
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import ticker
import matplotlib.colors as cls
from mpl_toolkits.axes_grid1 import make_axes_locatable

# Ejecta thickness contour level and colors
levels = [3e-5,1e-4,3e-4,1e-3,3e-3,1e-2]
colors = ['#4576b6', '#91bfdc', '#e1f3fa', '#fce091', '#f68d5c']

I = 6 # impactor diameter
V = 15 # impact velocity
degs = [10, 20, 30, 45, 60] # impact angle

# Set up canvas
pltlim = 25
plt.rcParams['font.size'] = '12'
cm = 1./2.54
ncols = len(degs)
fig, axes = plt.subplots(ncols = ncols, figsize = [21.*cm, 10*cm])
for i, ax in enumerate(axes):
    if i != 0:
        ax.yaxis.set_ticklabels([])
    ax.set_aspect('equal')
    ax.set_xlim(-pltlim, pltlim)
    ax.set_ylim(-pltlim, pltlim)
    ax.xaxis.set_major_locator(ticker.MaxNLocator(3))
    ax.yaxis.set_major_locator(ticker.MaxNLocator(3))
    ax.tick_params(
            axis = 'both',
            length = 3,
            top = True, right = True,
            direction = 'in',
            labelsize='10')
    ax.grid(linestyle='--',linewidth=0.5)

# Annotate the impactor diameter
text = axes[0].text(-0.45,0.5,'d = {} km'.format(I),
                    transform = axes[0].transAxes,
                    fontsize = '12',
                    fontweight='bold',
                    rotation='vertical',
                    va='center')

plt.subplots_adjust(top=None,left=None,right=None,
                    wspace=0.)

# Plot the ejecta pattern of each model case
for k,deg in enumerate(degs):
    ax = axes[k]
    modelname = 'I{}_deg{}_V{}'.format(I, deg, V)
    print(modelname)

    # Load the ejecta thickness grid
    Te = np.loadtxt('./'+modelname+'/Te_grid.txt')
    gridx = np.loadtxt('./'+modelname+'/gridx.txt')
    gridy = np.loadtxt('./'+modelname+'/gridy.txt')
    plotx, ploty = np.meshgrid(gridx, gridy)

    # Load the transient crater outline
    crater = np.loadtxt('./'+modelname+'/transient_outline.txt')

    # Calculate the crater radius
    R = ((abs(crater[:, 0].min()) + crater[:, 0].max()) / 2 + crater[:, 1].max()) / 2  # average alongrange and crossrange radius
    # Calculate the x-coordinate of the crater center
    center = [(crater[:, 0].min() + crater[:, 0].max()) / 2]

    # Set the axis and ejecta thickness normalization scale to the crater radius
    scale = R
    ax.set_xlabel('R = {}'.format(int(round(R / 1000))),fontsize=11)

    # Plot the ejecta thickness filled contours
    ax.contourf((plotx - center) / scale, ploty / scale, Te / scale,
                     colors=colors, levels=levels)
    # Mirror in the y direction
    ax.contourf((plotx - center) / scale, -ploty / scale, Te / scale,
                colors=colors, levels=levels)

    # Plot transient crater outline
    ax.plot((crater[:, 0] - center) / scale, crater[:, 1] / scale,
            lw=1., c='k')
    ax.plot((crater[:, 0] - center) / scale, -crater[:, 1] / scale,
            lw=1., c='k')

    ax.set_title(r'{}$\degree$'.format(deg),
                 fontsize='12',
                 fontweight='bold')

fig.savefig('./d{}_pattern_{}.pdf'.format(I, ncols), dpi=300, bbox_inches='tight')

# Colorbar
fig2, ax2 = plt.subplots(figsize=(12*cm, 1*cm))
fig2.subplots_adjust(bottom=0.5)
ax2.tick_params(axis = 'x',
                direction = 'in', length = 3,
                top = True, labelbottom = True,labeltop = False,
                labelsize='11')
ax2.set_yticks([])
ax2.set_xlim(0, len(colors))
for i in range(len(colors)):
   ax2.axvspan(i, i+1,
               color=colors[i])

ax2.set_xticks(range(len(colors)+1))
ax2.set_xticklabels(levels)
ax2.set_title('Thickness/R', pad=10, fontsize='12')
fig2.savefig('./Te_cb.pdf', bbox_inches='tight', dpi=300)
