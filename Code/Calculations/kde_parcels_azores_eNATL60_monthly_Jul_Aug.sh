#/bin/sh

# SGE: the job name
#$ -N Azores_eNATL60_KDE_weekly_nT_wT_Jul_Aug
#
# The requested run-time, expressed as (xxxx sec or hh:mm:ss)
#$ -l h_rt=02:00:00
#
# SGE: your Email here, for job notification
#$ -M l.gomeznavarro@uu.nl
#
# SGE: when do you want to be notified (b : begin, e : end, s : error)?
#$ -m es
#
# SGE: output in the current working dir
#$ -cwd    
#
cd /nethome/gomez023/parcels_Azores/kde_calcs/

python3 -c 'from kde_func import *; _,_,_=kde_parcels("/scratch/gomez023/outputs_parcels/Particle_AZO_grid100000p_no_tides_0701_hourly_MONTH.nc")'
python3 -c 'from kde_func import *; _,_,_=kde_parcels("/scratch/gomez023/outputs_parcels/Particle_AZO_grid100000p_tides_0701_hourly_MONTH.nc")'

python3 -c 'from kde_func import *; _,_,_=kde_parcels("/scratch/gomez023/outputs_parcels/Particle_AZO_grid100000p_no_tides_0801_hourly_MONTH.nc")'
python3 -c 'from kde_func import *; _,_,_=kde_parcels("/scratch/gomez023/outputs_parcels/Particle_AZO_grid100000p_tides_0801_hourly_MONTH.nc")'
