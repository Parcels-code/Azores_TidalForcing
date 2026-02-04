#!/bin/bash
#SBATCH -t 22:00:00
#SBATCH -N 1 
#SBATCH -o log.%j.o     # the name of the file where the standard output will be written to. %j will be the jobid determined by SLURM
#SBATCH -e log.%j.e     # the name of the file where potential errors will be written to. %j will be the jobid determined by SLURM
#SBATCH --mail-user=l.gomeznavarro@uu.nl
#SBATCH --mail-type=ALL

cd /storage/home/gomez023/parcels_Azores/eNATL60/local_gemini_notebooks/
python3 dist_km_Jul_nT.py
python3 dist_km_Aug_nT.py
python3 dist_km_Sep_nT.py
python3 dist_km_Oct_nT.py
