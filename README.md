# Capstone Project Repository
This project compares model outputs for a specific variable (sea surface salinity) at set locations given lattitude and longitude, comparing them using summary statistics (max, min, average, standard deviation)

The environment used can be found in the environment.yml file.
* Python 		3.11.2
* Pandas		1.5.3
* Numpy 		1.23.5
* Matplotlib	3.7.1 
* Cartopy 		0.21.1
* Xarray 		2022.11.0
* jupyter 		1.0.0

## Introduction
Paleoceanography looks at the reconstruction of past climate and ocean data. In most cases, there is not any way to analyze these variables directly, and so proxies must be used. When determining the validity of a proxy, it is explored in modern day conditions. 

This repository focuses on the development of a new surface salinity proxy using foraminifera shells. These shells are collected from the upper few centimeters of cores, and compared with modern sea surface salinity measurements. However, while this depth is relatively modern, it does not necessarily correspond to the immediate present, and the foraminifera may be hundreds or thousands of years old, which produces a source of error. 

While there are no direct salinity measurements going that far back, modelling can help determine what salinity may have been like over the past 1000 years. This can help determine whether the salinity in a given location has been stable, or if it has changed greatly, helping to reduce potential error from the foraminifera samples. 

## Data
The data used comes from the Earth System Grid Federation National Computer Interface node, a database of global model outputs. It can be found at https://esgf.nci.org.au/search/esgf-nci/

All datasets were found using the search parameters:
* Experiment = past1000 (model recreating 850-1850)
* Variable = sos        (sea surface salinity)  

Most of the code presented here assumes that the model outputs are in the /data folder, with the GISS models being in a seperate folder. However, due to their large sizes, these were not able to be uploaded to the github repository. As such, alternate codes are included for direct download links to circumvent this. All download files must have "#mode=bytes" added to the end to be read by xarray; this has been included in the code, but should be taken into account if replacing the links. 

Important to note, the size of the files means that pulling via the link will be slow on most systems. This is manageable for the GISS files due to their smaller size but the larger HADCM3 and CSIRO files are extensively and prohibitively slow. It is strongly recommended to download these directly through the links given to avoid this long processing time.

The cores.txt file is a list of the locations used, representing ocean sediment cores from various locations globally.

cores_stdsss.csv is the output of the Total Variation jupyter notebook. 

## Notebooks
The only notebook strictly required is the TotalVariation notebook which produces the final output. Other notebooks are included to display the working process. 

### EDA_netcdf.ipynb
Workbook that provides the initial exploration used for the development of the **ncsumstat** function, including the Exploratory Data Analysis on the netcdf files used for this repository.

### ncsumstat.py
This function automates the summary statistics. All require the inputs (lon, lat, ncfile) with longitude being from 0 to 360. 

The include functions included are:
* max - returns maximum sss value for given lon and lat for all times
* min - returns minimum sss value for given lon and lat for all times
* avg - returns average of sss values for given lon and lat 
* std - returns standard deviation of sss values for given lon and lat
* count - returns the count of non-null cells for the given lon and lat

### Combining GISS
Workbook that provides the initial exploration used for the development of the **combo** function, as well as the inputting of the GISS files.  

### combo.py
This function is used to combine netcdf files with the same experiment but different timespans and returns summary statistics. The inputs required are (lon,lat,array).

The include functions included are:
* max - returns the max of max values for all individual netcdf files
* min - returns the min of min values for all individual netcdf files
* avg - returns the average for the combined netcdf files via the formula sum(average * count)/sum(count)
 
### Total Variation
This notebook covers the use of the **ncsumstat** and **combo** functions on all models for all core sites, outputting the cores_stdsss.csv file in the data folder.

It also contains the analysis of the standard deviations and draws initial conclusions for these sites.
