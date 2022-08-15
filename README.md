# lunar-oblique-impact-ejecta
This repository includes sample input files for iSALE-3D and the simulations results of ejecta launch velocities, launch angles, and ejecta deposit patterns for the paper "Ejecta pattern of oblique impacts on the Moon from numerical simulations". Please note the iSALE-3D code is distributed on a case-by-case basis in the impact community, restricted to non-commercial use. 

Folders Fig4-8 contain source data and python scripts for producing the figures in the paper. 

Folders that contain the source data specific to a model case use the name convention I<impactor diameter>_deg<impact angle>_V<impact velocity>, where the units are km, degree, and km/s.

Folder "Fig4-Ejecta launch velocity" constains simulation results of the ejecta launch velocity distribution with respect to azimuth for three different groups of model cases
- Folder Fig4a-d: model cases with impactor diameter of 30 km, impact velocity of 15 km/s, and impact angles of 20-70 degree. The python script "Plot_V-phi_Fig4a-d.py" creates figures similar to Figs. 4a-d in the paper.
- Folder Fig4e-h: model cases with impactor diameter of 1-120 km, impact velocity of 15 km/s, and impact angle of 45 degree. The python script "Plot_V-phi_Fig4e-h.py" creates figures similar to Figs. 4e-h in the paper.
- Folder Fig4i-l: model cases with impactor diameter of 15 km, impact velocity of 10-30 km/s, and impact angle of 45 degree. The python script "Plot_V-phi_Fig4i-l.py" creates figures similar to Figs. 4i-l in the paper.
