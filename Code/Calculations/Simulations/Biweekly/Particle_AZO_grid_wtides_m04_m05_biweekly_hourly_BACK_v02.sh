#!/bin/bash
#SBATCH -t 9:00:00
#SBATCH -N 1

#SBATCH --mail-user=l.gomeznavarro@uu.nl
#SBATCH --mail-type=ALL

cd /nethome/gomez023/parcels_Azores/eNATL60/
python3 -c 'from parcels_azores_eNATL60_v02 import *; parcels_simu(tide_name = "tides", nmonth = 4, simu_length = 14., outname_ref = "_biweekly_hourly_BACK_v02", timestep=-5, start_days = [1,15])'
python3 -c 'from parcels_azores_eNATL60_v02 import *; parcels_simu(tide_name = "tides", nmonth = 5, simu_length = 14., outname_ref = "_biweekly_hourly_BACK_v02", timestep=-5, start_days = [1,15])'

