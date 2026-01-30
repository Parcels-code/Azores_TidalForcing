# Repository under construction!

Codes used for the paper: Gomez-Navarro _et al_. (2026)

Reference: Gómez-Navarro, L.; van Sebille, E.; Morales-Márquez, V.; Hernández-Carrasco, I.; Albert, A.; Ubelmann, C.; Molines, J.M.; Le Sommer, J. and Brodeau, L. Impact of Tidal Forcing on Surface Particle Transport Properties: Insights From Twin Ocean Simulations. _Journal of Advances in Modeling Earth Systems_ **2026**, **_10_, 599.** (edit) www.doi.org/10.1029/2024MS004805

**venv_??**

**Use?** https://github.com/Parcels-code/Azores_TidalForcing/blob/main/Code/Plotting/plots_source_code.md

Figures:

* [fig_01.ipynb](Code/Plotting/fig_01.ipynb)

    * In:<br>
		* .nc
		
	* Out: <br>
[Figure 1](Figures/Map_regions_Azores.jpg): Spatial domain of the eNATL60 simulation (except the Gulf of Mexico, Black Sea and eastern Mediterranean Sea domains). Black box shows the region of this study where virtual surface particles are released. Red box shows the subregion used for some of the analyses.

* [fig_02.ipynb](Code/Plotting/fig_02.ipynb)

	* In:<br>
		* xx.nc Obtained from: xx.py
		
	* Out: <br>
[Figure 02](Figures/cumsum_km_and_abs_dist_km_BOXPLOT_01.jpg): Box plots of mean cumulative distance [km] (top) and mean absolute distance [km]
(bottom) travelled by the virtual particles per month.

    * Pendings: <br>
        * thicker lines? to see better bottom part???? 

* [fig_03_04.ipynb](Code/Plotting/fig_03_04.ipynb)
	
	* In:
		* .nc
		
    * Out: <br>
		* [Figure 03](Figures/KDE_nT_wT_monthly_ALL_nosubregionBOX.jpg): Gaussian Kernel Density Estimation (GKDE) comparison between non-tidal (top) and tidal (bottom) simulations. Maximum GKDE value (top) and percentage of particles with a high GKDE value (greater than 0.008) (bottom) are shown in the top left textbox.
		* [Figure 04](Figures/KDE_nT_wT_monthly_ALL_perc_0080_Line.jpg): Comparison of the percentage of particles with a high GKDE value (≥0.008) per month. Non-tidal results are shown in blue and tidal in red. 
    
    * Pendings: <br>
        * add dot in titles?? Apr. 2010
        * equation needed somewhere?  ![equation](http://latex.codecogs.com/gif.latex?SSH$_{obs}$)   (fig 4 caption??)
        * fig. 4 : Date [dd/mm/YYYY] , mm or MM, dd or DD?  

* [fig_05](Code/Plotting/fig_05_08_10_12.ipynb)
	
	* In:  [List of input files](/input_files/list_fig_05_08_10_12.md)
		
	* Out: 
	[Figure 05](Figures/hist1d_nT_wT_monthly_nobox_new.jpg): Probability density functions of the surface particle accumulation (from the 2D, 0.1◦ binned histograms) after 28 days of advection. Results of the non-tidal simulation are shown in blue and from the tidal in red. Vertical, dashed lines indicate the maximum value.
        
* [fig_06.ipynb](Code/Plotting/fig_06.ipynb)
 
 	* In: 
		* *.nc
	
	* Out: <br>
	[Figure 06](Figures/skewness_intime_border_nT_wT_monthly_v02_wBARS.jpg): Skewness temporal evolution in time for each month for non-tidal (blue) and tidal
(red) simulations. Values in the text box are the variance of the skewness from the beginning of the month until the vertical line. The vertical line indicates the moment in time when any of the particles released at the boundary of the region first enters the subregion (see Section 2.3.2.2). Bottom plot shows the skewness value at the vertical line.

	* Pendings: <br>
        * add dot in titles?? Apr. 2010
        * colour vertical line
          
* [fig_07_08_09.ipynb](Code/Plotting/fig_07_08_09.ipynb)
    	
	* In: 
		* 
	
	* Out: 
		* **[Figure 07](Figures/KDE_nT_wT_monthly_ALL_nosubregionBOX.jpg)**: Comparison of attracting LCS structures (bFTLEs) on day 1 of each month from July to December 2009, for the non-tidal (left) and the tidal simulation (right).
		* **[Figure 08](Figures/KDE_nT_wT_monthly_ALL_perc_0080_Line.jpg)**: Comparison of attracting LCS structures (bFTLEs) on day 1 of each month from January to June 2010, for the non-tidal (left) and the tidal simulation (right).
		* [Figure 09](Figures/FTLE_backward_v02_biweekly_perc05_SKEW_nT_wT_AllMonths_newSkew_LinePlot.jpg): Top: Percentage of virtual particles with backward FTLE >0.5 days−1. Bottom: Skewness values of the backward FTLE fields.
    
  * Pendings:
      * Date [dd/MM/YYYY] , MM and dd or DD?

* [fig_10.ipynb](Code/Plotting/fig_10.ipynb)
    	
	* In: [List of input files](input_files/list_fig_015.md)
	
	* Out: [Figure 10](Figures/Joint_plot_02.jpg): Percentage difference with tidal forcing per month for each diagnostic calculated. From top to bottom: cumulative distance (CD), absolute distance (AD), percentage of particles with high Gaussian Kernel Density Estimation (GKDE ≥ 0.008) and percentage of particles with high backward Finite Time Lyapunov Exponents (bFTLE ≥ 0.5 **days−1).**
   
	  * Pendings:
          * Date [dd/MM/YYYY] , MM and dd or DD?
            
Appendix figures:

* [fig_A1.ipynb](Code/Plotting/fig_A1.ipynb)
  
	* In:
		* wnoises_loop_try2_cut.mat
    	
	* Out: <br>
	[Figure A1](Figures/FTLE_backward_v02_biweekly_AllMonths_day01_hist1d_bins1_vline05.jpg): Probability density function of the backward FTLE fields on day 1 of each month for the no tidal forcing (blue) and tidal forcing (red) simulations. The vertical black line shows the threshold used at 0.5 days−1.

Supplementary figures:

* [fig_S1_S2.ipynb](Code/Plotting/fig_S1_S2.ipynb)
    	
	* In:
		* wnoises_loop_try2_cut.mat
		* wnoises_loop_try2.mat
    	
	* Out: <br>
		* [Figure S1](Figures/KDE_nT_wT_monthly_ALL_nosubregionBOX.jpg): Gaussian Kernel Density Estimation (GKDE) comparison between non-tidal (top) and tidal (bottom) simulations. Maximum GKDE value (top) and percentage of particles with a high GKDE value (greater than 0.008) (bottom) are shown in the top left textbox.
		* [Figure S2](Figures/KDE_nT_wT_monthly_ALL_perc_0080_Line.jpg): Comparison of the percentage of particles with a high GKDE value (≥0.008) per month. Non-tidal results are shown in blue and tidal in red.

	* pENDING:
		* UPDATE AS 7 and 8??
		* cbar label
		* . in title Apr.
    
# Calculations:
* 

