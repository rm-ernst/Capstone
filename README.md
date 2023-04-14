# Capstone Project Repository
This project compares model outputs for a specific variable (sea surface salinity) at set locations. 

The data used comes from the Earth System Grid Federation National Computer Interface node, a database of global model outputs. It can be found at https://esgf.nci.org.au/search/esgf-nci/

All datasets were found using the search parameters:
> Experiment = past1000 (model recreating 850-1850)
>
> Variable = sos        (sea surface salinity)  

All netcdf files are accessed via direct download link due to large file size. In order to load in a netcdf file using xarray, "#mode=bytes" must be added to the end of the URL. 

The locations used are from the "cores.txt" file, representing ocean sediment cores from various locations globally. 

The environment used can be found in the environment.yml file.
* Python 		3.11.2
* Pandas		1.5.3
* Numpy 		1.23.5
* Matplotlib	3.7.1 
* Cartopy 		0.21.1
* Xarray 		2022.11.0
* jupyter 		1.0.0


## Notebooks
### Summmary Statistics of netcdf
Workbook that provides the initial exploration used for the development of the sumstat function. 

### sumstat.py
This function automates the summary statistics. All require the inputs (lon, lat, ncfile) with longitude being from 0 to 360. 

The include functions included are:
* max - returns maximum sss value for given lon and lat for all times
* min - returns minimum sss value for given lon and lat for all times
* avg - returns average of sss values for given lon and lat 
* std - returns standard deviation of sss values for given lon and lat
* count - returns the count of non-null cells for the given lon and lat

### Combining GISS
Workbook that provides the initial exploration used for the development of the combo function. 

### combo.py
This function is used to combine netcdf files with the same experiment but different timespans and returns summary statistics. The inputs required are (lon,lat,array).

The include functions included are:
* max - returns the max of max values for all individual netcdf files
* min - returns the min of min values for all individual netcdf files
* avg - returns the average for the combined netcdf files via the formula sum(average * count)/sum(count)
 
### Total Variation
A comparison of the results between the HADCM3 model, the CSIRO-Mk3L model, and the various combined GISS models.