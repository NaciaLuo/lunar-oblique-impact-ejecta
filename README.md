# Dataset of "Ejecta pattern of oblique impacts on the Moon from numerical simulations"
This repository includes sample input files for iSALE-3D and the simulations results of ejecta launch velocities, launch angles, and ejecta deposit patterns. Please note the iSALE-3D code is distributed on a case-by-case basis in the impact community, restricted to non-commercial use. 

Folders that contain the source data specific to a model case use the name convention I(impactor diameter)_deg(impact angle)_V(impact velocity), where the units are km, degree, and km/s.

## Folder "Fig4-Ejecta launch velocity"
Constains simulation results of the ejecta launch velocity distribution with respect to azimuth for three different groups of model cases. The Python script "Plot_V-phi_(subfolder name).py" creates subfigures of Figure 4 in the paper.
  - Subfolder "Fig4a-d": model cases with impactor diameter of 30 km, impact velocity of 15 km/s, and impact angles of 20-70 degree
  - Subolder "Fig4e-h": model cases with impactor diameter of 1-120 km, impact velocity of 15 km/s, and impact angle of 45 degree
  - Subfolder "Fig4i-l": model cases with impactor diameter of 15 km, impact velocity of 10-30 km/s, and impact angle of 45 degree

## Folder "Fig5-Ejecta launch angle"
Constains simulation results of the ejecta launch angle distribution with respect to azimuth for three different groups of model cases. The Python script "Plot_Alpha-phi_(subfolder name).py" creates subfigures of Figure 5 in the paper.
  - Subfolder "Fig5a": same parameter set as "Fig4a-d"
  - Subfolder "Fig5b": same parameter set as "Fig4e-h"
  - Subfolder "Fig5c": same parameter set as "Fig4i-l"
