from datetime import timedelta, datetime
import xarray as xr
import numpy as np
import xarray as xr

from math import sin, cos, sqrt, atan2, radians, pi

def dist_km(lona, lonb, lata, latb):

    # approximate radius of earth in km
    R = 6373.0

    lat1 = radians(lata)
    lon1 = radians(lona)
    lat2 = radians(latb)
    lon2 = radians(lonb)

    dlon = lon2 - lon1
    dlat = lat2 - lat1

    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    distance = R * c

    return distance

filedir = '/storage/shared/oceanparcels/output_data/data_LauraGN/outputs_parcels/Azores/eNATL60/'

ds = xr.open_dataset(filedir + 'ntides/monthly/Particle_AZO_grid100000p_ntides_0701_hourly_MONTH.nc')

dist_km_all = ds.lon.copy() * np.nan

for tt in range(0, len(ds.traj)):
    lon_t = ds.lon[tt,:].dropna(dim='obs')
    lat_t = ds.lat[tt,:].dropna(dim='obs')
    for oo in range(1, len(lat_t)): # calculate as distance at x0 = distance at x-x0
        dist_km_all[tt,oo-1] = dist_km(lon_t[oo-1], lon_t[oo], lat_t[oo-1], lat_t[oo])
            
dist_km_all.to_netcdf(filedir + "dist_km_Jul_nT.nc")
