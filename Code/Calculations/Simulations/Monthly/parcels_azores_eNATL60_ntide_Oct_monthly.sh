#/bin/sh

# SGE: the job name
#$ -N Azores_eNATL60_ntide_Oct_MONTHLY
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
cd /nethome/gomez023/parcels_Azores/ntides/monthly/
python3 parcels_azores_eNATL60_ntide_Oct_monthly.py
