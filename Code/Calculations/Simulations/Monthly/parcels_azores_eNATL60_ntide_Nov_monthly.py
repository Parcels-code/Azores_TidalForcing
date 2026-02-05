# Modules
from parcels import FieldSet, ParticleSet, JITParticle, AdvectionRK4, ErrorCode
from datetime import timedelta, datetime
from glob import glob
import xarray as xr
import numpy as np

# Defining functions

def DeleteParticle(particle, fieldset, time):
    particle.delete()

# Parameters:

# TO DOOO
#Particle_AZO_grid100000_notides_Dec_week01_hourly.nc
tide_name = "no_tides"
nmonth = 11 
simu_length = 28. # monthly # days

# Defining grid of starting particles:

step = .04 # degrees
lons, lats = np.meshgrid(np.arange(-35, -18+step, step), np.arange(30, 40+step, step))
lons.shape[0]*lons.shape[1]

#

if tide_name == "no_tides":
    tide_nameF    = "BLB002"
    tide_out = "ntides"
elif tide_name == "tides":
    tide_nameF    = "BLBT02"
    tide_out = "wtides"
else:
    print("Error")
    dsgsdgs

if nmonth > 6:
    nyear = 2009

elif nmonth <= 6:
    nyear = 2010
else:
    print('error')
    fsdgsdgg

data_path = '/data/oceanparcels/input_data/eNATL60/Azores/'

ufiles = sorted(glob(data_path + 'UV/' + tide_name + '/eNATL60ACOl-' + tide_nameF + '_y' + str(nyear) + 'm' + str(nmonth).zfill(2) + 'd*.1h_sozocrtx.nc'))
vfiles = sorted(glob(data_path + 'UV/' + tide_name + '/eNATL60ACOl-' + tide_nameF + '_y' + str(nyear) + 'm' + str(nmonth).zfill(2) + 'd*.1h_somecrty.nc'))

variables = {'U': 'sozocrtx', 'V': 'somecrty'}

mesh_mask = data_path + 'coordinates_eNATL60ACOl.nc' 

filenames = {'U': {'lon': mesh_mask, 'lat': mesh_mask, 'data': ufiles},
             'V': {'lon': mesh_mask, 'lat': mesh_mask, 'data': vfiles}}

dimensions = {'U': {'lon': 'glamf', 'lat': 'gphif', 'time': 'time_counter'},
              'V': {'lon': 'glamf', 'lat': 'gphif', 'time': 'time_counter'}}

fieldset_AZO = FieldSet.from_nemo(filenames, variables, dimensions)

#

ds_mesh = xr.open_dataset(mesh_mask)

outdir_root = "/scratch/gomez023/outputs_parcels/"
outdir = outdir_root + tide_out + "/monthly/"

# Define start date:
start_days = [1] #[1, 8, 15, 22]

for start_day in start_days:

       outname = outdir + "Particle_AZO_grid100000p_" + tide_out + "_" + str(nmonth).zfill(2) + str(start_day).zfill(2) + "_hourly_MONTH"
       pset_AZO_grid = ParticleSet(fieldset=fieldset_AZO, pclass=JITParticle, lon=lons, lat=lats, time=datetime(nyear, nmonth, start_day, 0, 30)) 
       output_file = pset_AZO_grid.ParticleFile(name=outname, outputdt=timedelta(hours=1))
       pset_AZO_grid.execute(AdvectionRK4, runtime=timedelta(days=simu_length), dt=timedelta(minutes=5),
             recovery={ErrorCode.ErrorOutOfBounds: DeleteParticle}, output_file=output_file)
       output_file.export()  # export the trajectory data to a netcdf file


