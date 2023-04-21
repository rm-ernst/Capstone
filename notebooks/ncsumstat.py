def max(lon,lat,ncfile):
	import xarray as xr
	ds = xr.load_dataset(ncfile)
	sss_alltime = ds.sos.sel(lon=lon, lat=lat, method='nearest')
	z = sss_alltime.max('time').values
	return z

def min(lon,lat,ncfile):
	import xarray as xr
	ds = xr.load_dataset(ncfile)
	sss_alltime = ds.sos.sel(lon=lon, lat=lat, method='nearest')
	z = sss_alltime.min('time').values
	return z

def avg(lon,lat,ncfile):
	import xarray as xr
	import numpy as np
	ds = xr.load_dataset(ncfile)
	sss_alltime = ds.sos.sel(lon=lon, lat=lat, method='nearest')
	z = np.average(sss_alltime.values)
	return z

def std(lon,lat,ncfile):
	import xarray as xr
	import numpy as np
	ds = xr.load_dataset(ncfile)
	sss_alltime = ds.sos.sel(lon=lon, lat=lat, method='nearest')
	z = np.std(sss_alltime.values)
	return z

def count(lon,lat,ncfile):
	import xarray as xr
	ds = xr.load_dataset(ncfile)
	sss_alltime = ds.sos.sel(lon=lon, lat=lat, method='nearest')
	z = sss_alltime.count().values
	return z