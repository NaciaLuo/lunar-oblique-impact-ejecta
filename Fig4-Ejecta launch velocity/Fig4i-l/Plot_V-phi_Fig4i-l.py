import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import matplotlib.patheffects as path_effects

# Annotate impact velocity
def text_U(ax):
    text = ax.text(0.97,0.82,
                  'U = {}km/s'.format(V),
                  transform = ax.transAxes,
                  fontsize = '9',
                   ha='right')
    text.set_path_effects([path_effects.Stroke(linewidth = 3, foreground = 'w'),
                          path_effects.Normal()])

subfig = 'Fig4i-l'
deg = 45
I = 15
Vs = [10,15,20,30]
V_threshold = 8000.
Ves = 2380. # escape velocity

# Define velocity bin and azimuthal angle bin
gridV = np.arange(0, V_threshold, 100)  # 100-m/s bin
gridphi = np.linspace(0, 180, 91)  # 2-degree bin

# Set up canvas
plt.style.use('default')
plt.rcParams['font.size'] = '9'
multilocator = 4
cmap = 'RdYlBu_r'
cm = 1./2.54
fig, axes = plt.subplots(ncols=4, figsize=[16*cm, 3.5*cm])
for i, ax in enumerate(axes):
    if i != 0:
        ax.yaxis.set_ticklabels([])
    ax.set_xlabel(r'Azimuth, $\phi (\degree)$', fontsize=8)
    ax.set_xlim(180,0)
    ax.set_xticks([180,90,0])
    ax.xaxis.set_minor_locator(plt.MultipleLocator(45))
    ax.yaxis.set_major_locator(plt.MultipleLocator(multilocator))
    ax.tick_params(axis='both',width=0.5,length=3,labelsize=8)
axes[0].set_ylabel(r'v (km/s)',fontsize=8)

for k, V in enumerate(Vs):
    modelname = 'I{}_deg{}_V{}'.format(I, deg, V)
    print('Modelname:', modelname)

    # Load ejecta launch velocity and azimuthal angle
    ve = np.loadtxt('./' + modelname + '/v.txt')
    phi = np.loadtxt('./' + modelname + '/phi.txt')

    # Volume fraction
    vol = np.array([[0. for i in range(len(gridphi) - 1)] for j in range(len(gridV) - 1)])

    # Put ejecta volume fraction in azimuth bin (fraction: n_binned/N_total)
    for i in range(len(gridV) - 1):
        true1 = np.logical_and(ve > gridV[i], ve <= gridV[i + 1])
        for j in range(len(gridphi) - 1):
            true2 = np.logical_and(true1, np.logical_and(phi > gridphi[j], phi <= gridphi[j + 1]))
            if len(phi[true2]) == 0:
                vol[i, j] = None
            else:
                vol[i, j] += (float(len(phi[true2])) / len(ve))  # n_binned/N_total

    # Divide the volume fraction by two due to bilateral symmetry
    vol = vol / 2

    ax = axes[k]
    ax.set_ylim(0, V_threshold / 1000)

    # Plot the velocity vs. azimuthal angle distribution
    im = ax.imshow(vol, origin='lower',
                   extent=[0, 180, 0, V_threshold / 1000],
                   aspect='auto',
                   cmap=cmap, vmin=1e-4, vmax=3e-3,
                   zorder=0)

    # Annotate model information
    text_U(ax)

    # Plot a vertical line denoting the escape velocity
    ax.axhline(Ves / 1000, linestyle='--', linewidth=0.5, color='k')

plt.subplots_adjust(wspace=0.2)
fig.savefig('./{}.pdf'.format(subfig), dpi=300, bbox_inches='tight')

# Colorbar
bar, axi = plt.subplots(1, 1, figsize=(0.25*cm, 3.5*cm))
mpl.colorbar.ColorbarBase(axi, cmap=cmap,\
                               norm=mpl.colors.Normalize(0,0.3),\
                               ticks=[0,0.1,0.2,0.3])
axi.set_title('(%)')
bar.savefig('./percent_cb.pdf', dpi=300, bbox_inches='tight')