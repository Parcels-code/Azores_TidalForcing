#!/bin/bash
#SBATCH -t 14:00:00
#SBATCH -N 1 
#SBATCH -o log.%j.o     # the name of the file where the standard output will be written to. %j will be the jobid determined by SLURM
#SBATCH -e log.%j.e     # the name of the file where potential errors will be written to. %j will be the jobid determined by SLURM
#SBATCH --mail-user=l.gomeznavarro@uu.nl
#SBATCH --mail-type=ALL

cd /storage/home/gomez023/parcels_Azores/eNATL60/
python3 dist_km_Nov_wT.py
#python3 dist_km_Dec_wT.py
python3 dist_km_Jan_wT.py
python3 dist_km_Feb_wT.py
