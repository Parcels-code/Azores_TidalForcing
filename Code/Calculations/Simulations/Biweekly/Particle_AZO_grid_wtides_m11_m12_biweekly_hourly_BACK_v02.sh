#!/bin/bash
# 
#SBATCH -t 9:00:00
#SBATCH -p normal
#SBATCH -N 1
#SBATCH -o log.%j.o     # the name of the file where the standard output will be written to. %j will be the jobid determined by SLURM
#SBATCH -e log.%j.e     # the name of the file where potential errors will be written to. %j will be the jobid determined by SLURM
#SBATCH --mail-user=l.gomeznavarro@uu.nl
#SBATCH --mail-type=ALL

cd /nethome/gomez023/parcels_Azores/eNATL60/
python3 -c 'from parcels_azores_eNATL60_v02 import *; parcels_simu(tide_name = "tides", nmonth = 11, simu_length = 14., outname_ref = "_biweekly_hourly_BACK_v02", timestep=-5, start_days = [1,15])'
python3 -c 'from parcels_azores_eNATL60_v02 import *; parcels_simu(tide_name = "tides", nmonth = 12, simu_length = 14., outname_ref = "_biweekly_hourly_BACK_v02", timestep=-5, start_days = [1,15])'

