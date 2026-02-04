#!/bin/bash
#SBATCH -t 6:00:00
#SBATCH -N 1 
#SBATCH -o log.%j.o     # the name of the file where the standard output will be written to. %j will be the jobid determined by SLURM
#SBATCH -e log.%j.e     # the name of the file where potential errors will be written to. %j will be the jobid determined by SLURM
#SBATCH --mail-user=l.gomeznavarro@uu.nl
#SBATCH --mail-type=ALL

cd /storage/home/gomez023/parcels_Azores/eNATL60/
python3 dist_km_Oct_nT.py
#python3 dist_km_Nov_nT.py
#python3 dist_km_Dec_nT.py
#python3 dist_km_Jan_nT.py
#python3 dist_km_Feb_nT.py
