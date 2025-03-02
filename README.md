# Dataset of "Ejecta pattern of oblique impacts on the Moon from numerical simulations"
This repository includes ejecta launch velocities, launch angles, and ejecta deposit patterns from iSALE-3D simulations. Please note the iSALE-3D code is distributed on a case-by-case basis in the impact community, restricted to non-commercial use. 

Source data for producing Figures 4-8 in the paper "Ejecta Pattern of Oblique Impacts on the Moon From Numerical Simulations" (https://doi.org/10.1029/2022JE007333) are stored in folders that use the name convention I(impactor diameter)\_deg(impact angle)\_V(impact velocity), where the units are km, degree, and km/s. 

## Folder "Fig4-Ejecta launch velocity"
Each subfolder contains ejecta launch velocity distribution with respect to azimuth for one group of model cases. In each folder I(impactor diameter)\_deg(impact angle)\_V(impact velocity), files ***v.txt*** and ***phi.txt*** are the ejecta launch velocity and azimuthal angle. The Python script Plot\_V-phi\_(subfolder name).py creates subfigures of Figure 4 in the paper.

## Folder "Fig5-Ejecta launch angle"
Each subfolder constains ejecta launch angle distribution with respect to azimuth for one groups of model cases. In each folder I(impactor diameter)\_deg(impact angle)\_V(impact velocity), ***alpha.txt*** and ***phi.txt*** are the ejecta launch angle and azimuthal angle. The Python script Plot\_Alpha-phi\_(subfolder name).py creates subfigures of Figure 5 in the paper. 

## Folders "Fig6-d1,6-EjectaPatterns", "Fig7-d30,120-EjectaPatterns", "Fig8-U10,20-EjectaPatterns"
Each subfolder contains ejecta deposit pattern for one groups of model cases. In each folder I(impactor diameter)\_deg(impact angle)\_V(impact velocity), ***Te_grid.txt*** is the ejecta thickness grid, ***gridx.txt*** and ***gridy.txt*** are the coordinates of the grid corners, and ***transient_outline.txt*** contains cooridinates of the transient crater outline. The Python script Plot_EjectaPattern_(subfolder name).py creates subfigures of Figures 6, 7 and 8 in the paper.
