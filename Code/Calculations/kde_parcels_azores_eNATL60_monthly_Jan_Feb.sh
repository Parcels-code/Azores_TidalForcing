#/bin/sh

# SGE: the job name
#$ -N Azores_eNATL60_KDE_MONTH_nT_wT_Jan_Feb
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
#python3 -c 'from kde_func import *; _,_,_=kde_parcels("/data/oceanparcels/input_data/eNATL60/Azores/outputs_parcels/Particle_AZO_grid100000p_no_tides_0101_hourly_MONTH.nc")'
#python3 -c 'from kde_func import *; _,_,_=kde_parcels("/data/oceanparcels/input_data/eNATL60/Azores/outputs_parcels/Particle_AZO_grid100000p_tides_0101_hourly_MONTH.nc")'

#python3 -c 'from kde_func import *; _,_,_=kde_parcels("/data/oceanparcels/input_data/eNATL60/Azores/outputs_parcels/Particle_AZO_grid100000p_no_tides_0201_hourly_MONTH.nc")'
python3 -c 'from kde_func import *; _,_,_=kde_parcels("/data/oceanparcels/input_data/eNATL60/Azores/outputs_parcels/Particle_AZO_grid100000p_tides_0201_hourly_MONTH.nc")'

