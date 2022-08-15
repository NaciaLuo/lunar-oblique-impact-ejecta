import numpy as np
import matplotlib.pyplot as plt
from cycler import cycler

subfig = 'Fig5a'
degs = [20, 60, 45, 70]
I = 30
V = 15
custom_cycler = (cycler(color=['k', 'y', 'm', 'c']))
markers = ['v', 'X', 'o', '^']

# Define azimuthal angle bin
binsize = 10
phi_bin = np.arange(0, 180+binsize, binsize)
phi_center = np.arange(binsize/2, binsize/2+180, binsize)

# Set up canvas
cm = 1./2.54
plt.style.use('default')
plt.rcParams['font.size'] = '9'
fig, ax = plt.subplots(1,1, figsize=[5*cm, 5*5/4*cm])
ax.set_xlim(180, 0)
ax.set_ylim(10, 80)
ax.set_xlabel(r'Azimuth, $\phi$ ($\degree$)')
ax.set_ylabel(r'$\alpha$ ($\degree$)')
ax.set_xticks([180,90,0])
ax.xaxis.set_minor_locator(plt.MultipleLocator(45))
ax.tick_params(axis='both', width=0.5, length=3)
ax.yaxis.set_major_locator(plt.MultipleLocator(15))
ax.set_prop_cycle(custom_cycler)

for k, deg in enumerate(degs):
    modelname = 'I{}_deg{}_V{}'.format(I, deg, V)
    print('Modelname:', modelname)

    # Load ejecta launch angle and azimuthal angle
    alpha = np.loadtxt('./' + modelname + '/alpha.txt')
    phi = np.loadtxt('./' + modelname + '/phi.txt')

    # Calculate the mean value and standard deviation in each bin
    alpha_bin = np.zeros(18)
    alpha_std = np.zeros(18)
    for i in range(18):
        alpha_sum = []
        for n, phii in enumerate(phi):
            if phi_bin[i] < phii <= phi_bin[i + 1]:
                alpha_sum.append(alpha[n])

        alpha_bin[i] = np.average(alpha_sum)
        alpha_std[i] = np.std(alpha_sum)

    ax.errorbar(phi_center, alpha_bin, yerr=alpha_std,
                ls='-',
                marker=markers[k],
                markersize=3,
                markeredgecolor='None',
                elinewidth=0.5,
                capsize=1.6,
                capthick=0.5,
                label=r'$\theta$={}$\degree$'.format(deg),
                zorder=5-k)
ax.legend(loc=4,fontsize='8',handlelength=0.5)
fig.savefig('./{}.pdf'.format(subfig), dpi=300, bbox_inches='tight')




