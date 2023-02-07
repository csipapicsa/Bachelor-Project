import datetime as dt  # Python standard library datetime  module
import numpy as np
from netCDF4 import Dataset  # http://code.google.com/p/netcdf4-python/
#import matplotlib.pyplot as plt
#from mpl_toolkits.basemap import Basemap, addcyclic, shiftgrid

print("get it")
time.sleep(1)


import netCDF4 as nc
fn = 'rawPoints/tx_ens_spread_0.25deg_reg_2011-2022_v26.0e.nc'
ds = nc.Dataset(fn)
print("get it")
t2 = ds['tx'][:]
print(ts[0])

import time
time.sleep(10) # Sleep for 3 seconds

print("get it")
time.sleep(1)