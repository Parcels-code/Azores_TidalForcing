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


# In[2]:


from math import sin, cos, sqrt, atan2, radians
import numpy as np
import xarray as xr
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


# In[3]:


filedir_m = '/storage/shared/oceanparcels/output_data/data_LauraGN/outputs_parcels/Azores/eNATL60/'


ds_nT_Jul = xr.open_dataset(filedir_m + 'ntides/monthly/Particle_AZO_grid100000p_ntides_0701_hourly_MONTH.nc')
ds_nT_Aug = xr.open_dataset(filedir_m + 'ntides/monthly/Particle_AZO_grid100000p_ntides_0801_hourly_MONTH.nc')
ds_nT_Sep = xr.open_dataset(filedir_m + 'ntides/monthly/Particle_AZO_grid100000p_ntides_0901_hourly_MONTH.nc')

ds_nT_Oct = xr.open_dataset(filedir_m + 'ntides/monthly/Particle_AZO_grid100000p_ntides_1001_hourly_MONTH.nc')
ds_nT_Nov = xr.open_dataset(filedir_m + 'ntides/monthly/Particle_AZO_grid100000p_ntides_1101_hourly_MONTH.nc')
ds_nT_Dec = xr.open_dataset(filedir_m + 'ntides/monthly/Particle_AZO_grid100000p_ntides_1201_hourly_MONTH.nc')

ds_nT_Jan = xr.open_dataset(filedir_m + 'ntides/monthly/Particle_AZO_grid100000p_ntides_0101_hourly_MONTH.nc')
ds_nT_Feb = xr.open_dataset(filedir_m + 'ntides/monthly/Particle_AZO_grid100000p_ntides_0201_hourly_MONTH.nc')
ds_nT_Mar = xr.open_dataset(filedir_m + 'ntides/monthly/Particle_AZO_grid100000p_ntides_0301_hourly_MONTH.nc')
# In[16]:

ds_nT_Apr = xr.open_dataset(filedir_m + 'ntides/monthly/Particle_AZO_grid100000p_ntides_0401_hourly_MONTH.nc')
ds_nT_May = xr.open_dataset(filedir_m + 'ntides/monthly/Particle_AZO_grid100000p_ntides_0501_hourly_MONTH.nc')
ds_nT_Jun = xr.open_dataset(filedir_m + 'ntides/monthly/Particle_AZO_grid100000p_ntides_0601_hourly_MONTH.nc')

dsps_nT = [ds_nT_Jul, ds_nT_Aug, ds_nT_Sep, ds_nT_Oct, ds_nT_Nov, ds_nT_Dec,
            ds_nT_Jan, ds_nT_Feb, ds_nT_Mar, ds_nT_Apr, ds_nT_May, ds_nT_Jun]

ntitles = ['Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec', 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'] # , 'Feb'

# Loop

for mm in range(0,len(ntitles)):
    ds = dsps_nT[mm]
    dist_tot_km = ds.lon[:,0].copy()
    dist_tot_km[:] = np.nan
    for tt in range(0, len(ds.traj)):
        lon_t = ds.lon[tt,:].dropna(dim='obs')
        lat_t = ds.lat[tt,:].dropna(dim='obs')
        dist_tot_km[tt] = dist_pairs_km(lon_t[0], lon_t[-1], lat_t[0], lat_t[-1])
    dist_tot_km.to_netcdf('dist_tot_km_nT_' + ntitles[mm] + '.nc')

