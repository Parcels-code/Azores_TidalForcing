# conda activate venv_kde_xarray

## Written on 18/01/2021 by Laura Gomez Navarro

# Modules:

from glob import glob
import xarray as xr
import numpy as np
from scipy.stats import gaussian_kde

def rem_nans(ds):
    """
    This renders lon and lat variables without nans for the last timestep.
    """
    bad_indices = np.isnan(ds['lon'][:,-1]) | np.isnan(ds['lat'][:,-1])
    good_indices = ~bad_indices
    lon_end_nonans = ds['lon'][:,-1][good_indices]
    lat_end_nonans = ds['lat'][:,-1][good_indices]
    
    return lon_end_nonans, lat_end_nonans

def kde_vals(lon_end_nonans, lat_end_nonans):
    """
    TO DO
    """
    x = lon_end_nonans.copy()
    y = lat_end_nonans.copy()
    
    xy = np.vstack([x, y])
    z = gaussian_kde(xy)(xy)

    idx = z.argsort()
    x, y, z = x[idx], y[idx], z[idx]
    
    return x, y, z

def kde_parcels(nfile):
    """
    Inputs
    nfile : filedir + filename

    Outputs
    KDE for end fields of lon and lat
    """

    ds = xr.open_dataset(nfile)
	
    # Remove nans:
    lon_end_nonans, lat_end_nonans = rem_nans(ds)
	
    kde_x, kde_y, kde_z = kde_vals(lon_end_nonans, lat_end_nonans)
        
    savedir = '/data/oceanparcels/output_data/data_LauraGN/outputs_parcels/kde_calcs/'
    savename = savedir + 'KDE_' + nfile.split('/')[-1].split('.nc')[0] + '.npz'
    np.savez(savename, kde_x=kde_x, kde_y=kde_y, kde_z=kde_z)        

    return kde_x, kde_y, kde_z

def kde_parcels_bws(nfile, bw_set):
    """
    bw_set = np.arange(0.01, 0.26, 0.01)
    """
    ds = xr.open_dataset(nfile)

    # Remove nans:
    lon_end_nonans, lat_end_nonans = rem_nans(ds)

    x = lon_end_nonans.copy()
    y = lat_end_nonans.copy()

    xy = np.vstack([x, y])
 
    KDE_dict = {}
    for ii in range(0, len(bw_set)):
        KDE_dict["z%02d" %ii] =  gaussian_kde(xy, bw_method=bw_set[ii])(xy)

    # Saving:
    savedir = '/data/oceanparcels/output_data/data_LauraGN/outputs_parcels/kde_calcs/'
    savename = savedir + 'KDE_' + nfile.split('/')[-1].split('.nc')[0] + '_bws.npz'
    np.savez(savename, bw_set=bw_set, KDE_dict=KDE_dict) 

