def max(lon,lat,array):
	import pandas as pd
	import numpy as np
	import ncsumstat as ns

	df = pd.DataFrame(np.nan, index=range(len(array)), columns=['URL', 'Max'])
	df['URL']=array
	for x in range(df.shape[0]):
		df.loc[x,'Max'] = ns.max(lon,lat,df.loc[x,'URL'])
	maximum = df['Max'].max()
	return maximum

def min(lon,lat,array):
	import pandas as pd
	import numpy as np
	import ncsumstat as ns

	df = pd.DataFrame(np.nan, index=range(len(array)), columns=['URL','Min'])
	df['URL']=array
	for x in range(df.shape[0]):
		df.loc[x,'Min'] = ns.min(lon,lat,df.loc[x,'URL'])
	minimum = df['Min'].min()
	return minimum

def avg(lon,lat,array):
	import pandas as pd
	import numpy as np
	import ncsumstat as ns

	df = pd.DataFrame(np.nan, index=range(len(array)), columns=['URL', 'Avg', 'Count', 'Avg*Count'])
	df['URL']=array
	for x in range(df.shape[0]):
		df.loc[x,'Avg'] = ns.avg(lon,lat,df.loc[x,'URL'])
		df.loc[x,'Count'] = ns.count(lon,lat,df.loc[x,'URL'])
		df.loc[x,'Avg*Count'] = df.loc[x,'Avg'] * df.loc[x,'Count']
	totalavgcount = df['Avg*Count'].sum() 
	totalsum = df['Count'].sum()
	totalavg = totalavgcount / totalsum
	return totalavg