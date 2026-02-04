#/bin/sh

# SGE: the job name
#$ -N dist_tot_km_monthly_nT
#
# The requested run-time, expressed as (xxxx sec or hh:mm:ss)
#$ -l h_rt=03:00:00
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
python3 dist_tot_km_monthly_nT.py
 
