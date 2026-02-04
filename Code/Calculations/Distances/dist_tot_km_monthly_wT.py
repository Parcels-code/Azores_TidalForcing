#!/usr/bin/env python
# coding: utf-8

# In[1]:


from datetime import timedelta, datetime
from glob import glob
import xarray as xr
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import matplotlib.dates as mdates

from collections import namedtuple
from shapely import geometry

import scipy 
from scipy import stats, optimize, interpolate

from math import sin, cos, sqrt, atan2, radians
import numpy.linalg as LA

# Adapted from test03, adding the sqrt in FTLE calcn after discussing with Darshika (this version should be up to date w/ github function!!!
# reorganized filename and savename so easier to modify!!!

def dist_pairs_km(inlon1, inlon2, inlat1, inlat2):
    """
    source: https://stackoverflow.com/questions/19412462/getting-distance-between-two-points-based-on-latitude-longitude
    
    """
    # approximate radius of earth in km
    R = 6373.0

    lon1 = radians(inlon1)
    lat1 = radians(inlat1)
    lon2 = radians(inlon2)
    lat2 = radians(inlat2)

    dlon = lon2 - lon1
    dlat = lat2 - lat1

    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    distance = R * c

    return distance

filedir_m = '/storage/shared/oceanparcels/output_data/data_LauraGN/outputs_parcels/Azores/eNATL60/'

ds_wT_Jul = xr.open_dataset(filedir_m + 'wtides/monthly/Particle_AZO_grid100000p_wtides_0701_hourly_MONTH.nc')
ds_wT_Aug = xr.open_dataset(filedir_m + 'wtides/monthly/Particle_AZO_grid100000p_wtides_0801_hourly_MONTH.nc')
ds_wT_Sep = xr.open_dataset(filedir_m + 'wtides/monthly/Particle_AZO_grid100000p_wtides_0901_hourly_MONTH.nc')

ds_wT_Oct = xr.open_dataset(filedir_m + 'wtides/monthly/Particle_AZO_grid100000p_wtides_1001_hourly_MONTH.nc')
ds_wT_Nov = xr.open_dataset(filedir_m + 'wtides/monthly/Particle_AZO_grid100000p_wtides_1101_hourly_MONTH.nc')
ds_wT_Dec = xr.open_dataset(filedir_m + 'wtides/monthly/Particle_AZO_grid100000p_wtides_1201_hourly_MONTH.nc')

ds_wT_Jan = xr.open_dataset(filedir_m + 'wtides/monthly/Particle_AZO_grid100000p_wtides_0101_hourly_MONTH.nc')
ds_wT_Feb = xr.open_dataset(filedir_m + 'wtides/monthly/Particle_AZO_grid100000p_wtides_0201_hourly_MONTH.nc')
ds_wT_Mar = xr.open_dataset(filedir_m + 'wtides/monthly/Particle_AZO_grid100000p_wtides_0301_hourly_MONTH.nc')
# In[16]:

ds_wT_Apr = xr.open_dataset(filedir_m + 'wtides/monthly/Particle_AZO_grid100000p_wtides_0401_hourly_MONTH.nc')
ds_wT_May = xr.open_dataset(filedir_m + 'wtides/monthly/Particle_AZO_grid100000p_wtides_0501_hourly_MONTH.nc')
ds_wT_Jun = xr.open_dataset(filedir_m + 'wtides/monthly/Particle_AZO_grid100000p_wtides_0601_hourly_MONTH.nc')

dsps_wT = [ds_wT_Jul, ds_wT_Aug, ds_wT_Sep, ds_wT_Oct, ds_wT_Nov, ds_wT_Dec,
            ds_wT_Jan, ds_wT_Feb, ds_wT_Mar, ds_wT_Apr, ds_wT_May, ds_wT_Jun]

ntitles = ['Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec', 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'] # , 'Feb'

# Loop

for mm in range(0,len(ntitles)):
    ds = dsps_wT[mm]
    dist_tot_km = ds.lon[:,0].copy()
    dist_tot_km[:] = np.nan
    for tt in range(0, len(ds.traj)):
        lon_t = ds.lon[tt,:].dropna(dim='obs')
        lat_t = ds.lat[tt,:].dropna(dim='obs')
        dist_tot_km[tt] = dist_pairs_km(lon_t[0], lon_t[-1], lat_t[0], lat_t[-1])
    dist_tot_km.to_netcdf('dist_tot_km_wT_' + ntitles[mm] + '.nc')

