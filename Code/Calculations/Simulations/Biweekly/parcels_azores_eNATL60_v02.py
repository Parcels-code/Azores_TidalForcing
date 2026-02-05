# Modules
from parcels import FieldSet, ParticleSet, JITParticle, AdvectionRK4, ErrorCode
from datetime import timedelta, datetime
from glob import glob
import xarray as xr
import numpy as np

# Defining functions

def DeleteParticle(particle, fieldset, time):
    particle.delete()

def parcels_simu(nmonth, tide_name, simu_length, outname_ref, timestep, start_days):
    """
    # Parameters:
    tide_name = "no_tides"
    nmonth = 8 
    simu_length = 14. # monthly # days
    outname_ref = "_biweekly_hourly_BACK"
    timestep = -5
    # Define start date:
    start_days = [1, 15] #[1, 
    """

    if nmonth > 6:
        nyear = 2009

    elif nmonth <= 6:
        nyear = 2010
    else:
        print('error')
        fsdgsdgg

    #
    if tide_name == "no_tides":
        tide_nameF    = "BLB00*" #02, but for June 01 so *
        tide_out = "ntides"
    elif tide_name == "tides":
        tide_nameF    = "BLBT0*" #02, but for June 01 so *
        tide_out = "wtides"
    else:
        print("Error")
        dsgsdgs
    
    # Defining grid of starting particles:
    step = .004 # degrees
    lons, lats = np.meshgrid(np.arange(-27, -21+step, step), np.arange(32.5, 36.5+step, step))
    lons.shape[0]*lons.shape[1]

    #
    data_path = '/storage/shared/oceanparcels/input_data/eNATL60/Azores/'

    ufiles = sorted(glob(data_path + 'UV/' + tide_name + '/eNATL60ACOl-' + tide_nameF + '_y*.1h_sozocrtx.nc')) 
    vfiles = sorted(glob(data_path + 'UV/' + tide_name + '/eNATL60ACOl-' + tide_nameF + '_y*.1h_somecrty.nc')) 
    print(ufiles[0])
    print(vfiles[0])

    variables = {'U': 'sozocrtx', 'V': 'somecrty'}

    mesh_mask = data_path + 'coordinates_eNATL60ACOl.nc' 

    filenames = {'U': {'lon': mesh_mask, 'lat': mesh_mask, 'data': ufiles},
                 'V': {'lon': mesh_mask, 'lat': mesh_mask, 'data': vfiles}}

    dimensions = {'U': {'lon': 'glamf', 'lat': 'gphif', 'time': 'time_counter'},
                  'V': {'lon': 'glamf', 'lat': 'gphif', 'time': 'time_counter'}}

    fieldset_AZO = FieldSet.from_nemo(filenames, variables, dimensions)

    #

    ds_mesh = xr.open_dataset(mesh_mask)

    outdir_root = "/storage/shared/oceanparcels/output_data/data_LauraGN/"
    #outdir = outdir_root + tide_out + "/weekly/"
    #outdir = "/nethome/gomez023/parcels_Azores/outputs_parcels/"

    for start_day in start_days:
        #outname = outdir + "Particle_AZO_grid100000p_" + tide_out + "_" + str(nmonth).zfill(2) + str(start_day).zfill(2) + "_hourly_BACK"
        outname = outdir_root + "Particle_AZO_grid_" + tide_out + "_" + str(nmonth).zfill(2) + str(start_day).zfill(2) + outname_ref
        print(outname)
        pset_AZO_grid = ParticleSet(fieldset=fieldset_AZO, pclass=JITParticle, lon=lons, lat=lats, time=datetime(nyear, nmonth, start_day, 0, 30)) 
        output_file = pset_AZO_grid.ParticleFile(name=outname, outputdt=timedelta(hours=1))
        pset_AZO_grid.execute(AdvectionRK4, runtime=timedelta(days=simu_length), dt=timedelta(minutes=timestep), recovery={ErrorCode.ErrorOutOfBounds: DeleteParticle}, output_file=output_file)
        output_file.export()  # export the trajectory data to a netcdf file


