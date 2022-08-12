#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
@author: xizi

Plot a group of ejecta patterns
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import ticker
import cmcrameri.cm as cmc
import matplotlib.colors as cls
from mpl_toolkits.axes_grid1 import make_axes_locatable

I = 15
V = 10
degs = [20,30,45,60] # impact angle

pltlim = 15 # plot limit of the axes, smaller impactor needs a larger pltR
plt.rcParams['font.size'] = '12'
#cmap = cmc.batlowW_r
colors = ['#4576b6', '#91bfdc', '#e1f3fa', '#fce091', '#f68d5c', '#d93127']
levels = [3e-5,1e-4,3e-4,1e-3,3e-3,1e-2,3e-2]
#norm = cls.LogNorm(vmin=min(levels), vmax=max(levels))

cm = 1./2.54
ncols=len(degs)
fig, axes = plt.subplots(ncols=ncols, figsize=[21.*cm,10*cm], constrained_layout=True)
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
            labelsize=11)
    ax.grid(linestyle='--',linewidth=0.5)

text = axes[0].text(-0.45,0.5,'d = {} km'.format(I),
                    transform = axes[0].transAxes,
                    fontsize = '12',
                    fontweight='bold',
                    rotation='vertical',
                    va='center')

plt.subplots_adjust(top=None,left=None,right=None,
                    wspace=0.)


for k,deg in enumerate(degs):
    modelname = 'I{}_deg{}_V{}'.format(I, deg, V)

    Te = np.loadtxt('./'+modelname+'/Te_grid.txt')
    gridx = np.loadtxt('./'+modelname+'/gridx.txt')
    gridy = np.loadtxt('./'+modelname+'/gridy.txt')
    crater = np.loadtxt('./'+modelname+'/transient_outline.txt')
    R = ((abs(crater[:, 0].min()) + crater[:, 0].max()) / 2 + crater[:, 1].max()) / 2
    center = [(crater[:, 0].min() + crater[:, 0].max()) / 2]
    plotx, ploty = np.meshgrid(gridx, gridy)
    scale = R

    ax = axes[k]
    ax.set_xlabel('R = {}'.format(int(round(R / 1000))),fontsize=11)

    # Plot the ejecta thickness contourf
    im = ax.contourf((plotx - center) / scale, ploty / scale, Te / scale,
                     colors=colors, levels=levels)
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

# cbar=fig.colorbar(im,ax=axes[:],shrink=0.5,pad=0.2,location='bottom')
# cbar.ax.set_xticklabels(['3e-5','1e-4','3e-4','1e-3','3e-3','1e-2','3e-2'])
# cbar.ax.tick_params(labelsize='small')
# cbar.set_label('Thickness/R')

# fig.savefig('d{}_pattern_{}.pdf'.format(I,ncols),dpi=300,bbox_inches='tight')