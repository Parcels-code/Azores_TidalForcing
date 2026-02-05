#!/bin/bash
#SBATCH -t 11:00:00
#SBATCH -N 2

#SBATCH --mail-user=l.gomeznavarro@uu.nl
#SBATCH --mail-type=ALL

cd /nethome/gomez023/parcels_Azores/eNATL60/
python3 -c 'from parcels_azores_eNATL60_v02 import *; parcels_simu(tide_name = "tides", nmonth = 8, simu_length = 14., outname_ref = "_biweekly_hourly_BACK_v02", timestep=-5, start_days = [15])'
python3 -c 'from parcels_azores_eNATL60_v02 import *; parcels_simu(tide_name = "tides", nmonth = 9, simu_length = 14., outname_ref = "_biweekly_hourly_BACK_v02", timestep=-5, start_days = [1,15])'
python3 -c 'from parcels_azores_eNATL60_v02 import *; parcels_simu(tide_name = "tides", nmonth = 1, simu_length = 14., outname_ref = "_biweekly_hourly_BACK_v02", timestep=-5, start_days = [1,15])'

