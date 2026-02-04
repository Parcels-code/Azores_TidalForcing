#!/bin/bash
#SBATCH -t 18:00:00
#SBATCH -n 1 
#SBATCH -o log.%j.o     # the name of the file where the standard output will be written to. %j will be the jobid determined by SLURM
#SBATCH -e log.%j.e     # the name of the file where potential errors will be written to. %j will be the jobid determined by SLURM
#SBATCH --mail-user=l.gomeznavarro@uu.nl
#SBATCH --mail-type=ALL

cd /storage/home/gomez023/parcels_Azores/eNATL60/
#python3 dist_km_Mar_wT.py
python3 dist_km_Apr_wT.py
python3 dist_km_May_wT.py
python3 dist_km_Jun_wT.py
