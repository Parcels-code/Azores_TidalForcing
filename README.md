# Repository under construction!

Codes used for the paper: Gomez-Navarro _et al_. (2026)

Reference: Gómez-Navarro, L.; van Sebille, E.; Morales-Márquez, V.; Hernández-Carrasco, I.; Albert, A.; Ubelmann, C.; Molines, J.M.; Le Sommer, J. and Brodeau, L. Impact of Tidal Forcing on Surface Particle Transport Properties: Insights From Twin Ocean Simulations. _Journal of Advances in Modeling Earth Systems_ **2026**, **_10_, 599.** (edit) www.doi.org/10.1029/2024MS004805


## Virtual environment 

env_parcels_Azores_analyses.yml

Install by: **xx**


## Figures:

* [fig_01.ipynb](Code/Plotting/fig_01.ipynb)
		
	* Output: <br>
[Figure 1](Figures/Map_regions_Azores.jpg): Spatial domain of the eNATL60 simulation (except the Gulf of Mexico, Black Sea and eastern Mediterranean Sea domains). Black box shows the region of this study where virtual surface particles are released. Red box shows the subregion used for some of the analyses.

* [fig_02.ipynb](Code/Plotting/fig_02.ipynb)

	* In:<br>
		* Monthly netcdfs: dist_km_Jul_nT.nc. Obtained from: 
            * [dist_km_monthly_nT_JASO.sh](Code/Calculations/Distances/dist_km_monthly_nT_JASO.sh)
            * [dist_km_monthly_nT_MAMJ.sh](Code/Calculations/Distances/dist_km_monthly_nT_MAMJ.sh)
            * [dist_km_monthly_nT_ONDJF.sh](Code/Calculations/Distances/dist_km_monthly_nT_ONDJF.sh)
		* Monthly netcdfs: dist_km_Jul_wT.nc. Obtained from:             
            * [dist_km_monthly_wT_JASO.sh](Code/Calculations/Distances/dist_km_monthly_wT_JASO.sh)
            * [dist_km_monthly_wT_MAMJ.sh](Code/Calculations/Distances/dist_km_monthly_wT_MAMJ.sh)
            * [dist_km_monthly_wT_ONDJF.sh](Code/Calculations/Distances/dist_km_monthly_wT_ONDJF.sh)
		* Monthly netcdfs: dist_tot_km_nT_Jul.nc. Obtained from:             
            * [dist_tot_km_monthly_nT.sh](Code/Calculations/Distances/dist_tot_km_monthly_nT.sh)
		* Monthly netcdfs: dist_tot_km_wT_Jul.nc. Obtained from:             
            * [dist_tot_km_monthly_wT.sh](Code/Calculations/Distances/dist_tot_km_monthly_wT.sh)
		
	* Out: <br>
[Figure 02](Figures/cumsum_km_and_abs_dist_km_BOXPLOT_01.jpg): Box plots of mean cumulative distance [km] (top) and mean absolute distance [km] (bottom) travelled by the virtual particles per month.

* [fig_03_04.ipynb](Code/Plotting/fig_03_04.ipynb)
	
	* In:
		* Monthly nectdf simulation files. Obtained from:
            *
        * GKDE npz monthly files: KDE_Particle_AZO_grid100000p_ntides_0701_hourly_MONTH.npz. Obtained from:
            * s
    * Out: <br>
		* [Figure 03](Figures/KDE_nT_wT_monthly_ALL_nosubregionBOX.jpg): Gaussian Kernel Density Estimation (GKDE) comparison between non-tidal (top) and tidal (bottom) simulations. Maximum GKDE value (top) and percentage of particles with a high GKDE value (greater than 0.008) (bottom) are shown in the top left textbox.
		* [Figure 04](Figures/KDE_nT_wT_monthly_ALL_perc_0080_Line.jpg): Comparison of the percentage of particles with a high GKDE value (≥0.008) per month. Non-tidal results are shown in blue and tidal in red. 
    
* [fig_05](Code/Plotting/fig_05.ipynb)
	
	* In: 
        * Monthly nectdf simulation files: Particle_AZO_grid100000p_ntides_0301_hourly_MONTH.nc. Obtained from: 
            * 

	* Out: 
	[Figure 05](Figures/hist1d_nT_wT_monthly_nobox_new.jpg): Probability density functions of the surface particle accumulation (from the 2D, 0.1◦ binned histograms) after 28 days of advection. Results of the non-tidal simulation are shown in blue and from the tidal in red. Vertical, dashed lines indicate the maximum value.
        
* [fig_06.ipynb](Code/Plotting/fig_06.ipynb)
 
 	* In: 
        * Skewness npz skew_2D_months_subregion_v02.npz. Obtained from:
            * ../Calculations/2021-02-22_Azores_simus_100000p_hists_MONTHLY_allMONTHS_subregion_v02_SKEWNESS.ipynb
        * Monthly nectdf simulation files: Particle_AZO_grid100000p_ntides_0301_hourly_MONTH.nc. Obtained from: 
            * 
	
	* Out: <br>
	[Figure 06](Figures/skewness_intime_border_nT_wT_monthly_v02_wBARS.jpg): Skewness temporal evolution in time for each month for non-tidal (blue) and tidal
(red) simulations. Values in the text box are the variance of the skewness from the beginning of the month until the vertical line. The vertical line indicates the moment in time when any of the particles released at the boundary of the region first enters the subregion (see Section 2.3.2.2). Bottom plot shows the skewness value at the vertical line.
          
* [fig_07_08_09.ipynb](Code/Plotting/fig_07_08_09.ipynb)
    	
	* In: 
		* bFTLE npz files: FTLE_b_nT_Jan_biw_w01_v02.npz. Obtained from:
            * Code/Calculations/2021-10-12_FTLE_back_season_subregion_v02_BIWEEKLY_comparison_CALCS.ipynb
            * Code/Calculations/2022-01-18_FTLE_back_season_subregion_v02_BIWEEKLY_other_MONTHS_comparison_CALCS.ipynb
	
	* Out: 
		* [Figure 07](Figures/FTLE_backward_v02_biweekly_AllMonths_day01_05_nTwT_2009.jpg): Comparison of attracting LCS structures (bFTLEs) on day 1 of each month from July to December 2009, for the non-tidal (left) and the tidal simulation (right).
		* [Figure 08](Figures/FTLE_backward_v02_biweekly_AllMonths_day01_05_nTwT_2010.jpg): Comparison of attracting LCS structures (bFTLEs) on day 1 of each month from January to June 2010, for the non-tidal (left) and the tidal simulation (right).
		* [Figure 09](Figures/FTLE_backward_v02_biweekly_perc05_SKEW_nT_wT_AllMonths_newSkew_LinePlot.jpg): Top: Percentage of virtual particles with backward FTLE >0.5 days⁻¹. Bottom: Skewness values of the backward FTLE fields.
    
* [fig_10.ipynb](Code/Plotting/fig_10.ipynb)
    	
	* In: [List of input files](input_files/list_fig_015.md)
	
	* Out: [Figure 10](Figures/Joint_plot_02.jpg): Percentage difference with tidal forcing per month for each diagnostic calculated. From top to bottom: cumulative distance (CD), absolute distance (AD), percentage of particles with high Gaussian Kernel Density Estimation (GKDE ≥ 0.008) and percentage of particles with high backward Finite Time Lyapunov Exponents (bFTLE ≥ 0.5 days⁻¹).
   
Appendix figures:

* [fig_A1.ipynb](Code/Plotting/fig_A1.ipynb)
  
	* In:
		* bFTLE npz files: FTLE_b_nT_Jan_biw_w01_v02.npz. Obtained from:
            * Code/Calculations/2021-10-12_FTLE_back_season_subregion_v02_BIWEEKLY_comparison_CALCS.ipynb
            * Code/Calculations/2022-01-18_FTLE_back_season_subregion_v02_BIWEEKLY_other_MONTHS_comparison_CALCS.ipynb
            
	* Out: <br>
	[Figure A1](Figures/FTLE_backward_v02_biweekly_AllMonths_day01_hist1d_bins1_vline05.jpg): Probability density function of the backward FTLE fields on day 1 of each month for the no tidal forcing (blue) and tidal forcing (red) simulations. The vertical black line shows the threshold used at 0.5 days⁻¹.

Supplementary figures:

* [fig_S1_S2.ipynb](Code/Plotting/fig_S1_S2.ipynb)
    	
	* In:
		* bFTLE npz files: FTLE_b_nT_Jan_biw_w01_v02.npz. Obtained from:
            * Code/Calculations/2021-10-12_FTLE_back_season_subregion_v02_BIWEEKLY_comparison_CALCS.ipynb
            * Code/Calculations/2022-01-18_FTLE_back_season_subregion_v02_BIWEEKLY_other_MONTHS_comparison_CALCS.ipynb
    	
	* Out: <br>
		* [Figure S1](Figures/FTLE_backward_v02_biweekly_AllMonths_day01_nT.jpg): Backward FTLE fields [days⁻¹] on day 01 of each month for the non-tidal simulation.
		* [Figure S2](Figures/FTLE_backward_v02_biweekly_AllMonths_day01_wT.jpg): Backward FTLE fields [days⁻¹] on day 01 of each month for the tidal simulation.      

# Calculations:
* Monthly simulations: One simulation file per month and tidal simulation, e.g.:
    * [parcels_azores_eNATL60_ntide_Apr_monthly.sh](Code/Calculations/Simulations/Monthly/parcels_azores_eNATL60_ntide_Apr_monthly.sh), which runs: [parcels_azores_eNATL60_ntide_Apr_monthly.py](Code/Calculations/Simulations/Monthly/parcels_azores_eNATL60_ntide_Apr_monthly.py) 
    * In: eNATL60 model surface u and v outputs. Data available upon request.
    
    * Out: Monthly nectdf simulation files: Particle_AZO_grid100000p_ntides_0401_hourly_MONTH.nc
    
* Biweekly simulations: 
    * Simualtions launched from .sh files : [Particle_AZO_grid_Jul_w01_biweekly_hourly_BACK_v02.sh](Code/Calculations/Simulations/Biweekly/Particle_AZO_grid_Jul_w01_biweekly_hourly_BACK_v02.sh), which call the function: [parcels_azores_eNATL60_v02.py](Code/Calculations/Simulations/Biweekly/parcels_azores_eNATL60_v02.py)
    * In: eNATL60 model surface u and v outputs. Data available upon request.
    * Out: Bieekly nectdf simulation files: Particle_AZO_grid_ntides_0101_biweekly_hourly_BACK_v02.nc
    
* skewness: 2021-02-22_Azores_simus_100000p_hists_MONTHLY_allMONTHS_subregion_v02_SKEWNESS.ipynb
 	* In: 
        * Monthly nectdf simulation files: Particle_AZO_grid100000p_ntides_0401_hourly_MONTH.nc. Obtained from: 
            * [parcels_azores_eNATL60_ntide_Apr_monthly.sh](Code/Calculations/Simulations/Monthly/parcels_azores_eNATL60_ntide_Apr_monthly.sh)
 	* Out: [skew_2D_months_subregion_v02.npz](Code/Calculations/skew_2D_months_subregion_v02.npz)

* bFTLEs: Calculated monthly from:
    * [2021-10-12_FTLE_back_season_subregion_v02_BIWEEKLY_comparison_CALCS.ipynb](Code/Calculations/2021-10-12_FTLE_back_season_subregion_v02_BIWEEKLY_comparison_CALCS.ipynb)
    * [2022-01-18_FTLE_back_season_subregion_v02_BIWEEKLY_other_MONTHS_comparison_CALCS.ipynb](Code/Calculations/2022-01-18_FTLE_back_season_subregion_v02_BIWEEKLY_other_MONTHS_comparison_CALCS.ipynb)
    * In:
        * Biweekly nectdf simulation files: Particle_AZO_grid_ntides_0101_biweekly_hourly_BACK_v02.nc
    * Out:
        * bFTLE npz files: FTLE_b_nT_Jan_biw_w01_v02.npz.
    
    
