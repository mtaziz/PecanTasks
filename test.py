import netCDF4
import pandas as pd
import numpy as np
precip_nc_file1 = 'C:\\Users\\Yadav\\Desktop\\Pecan opensource\\new images\\2002.nc'
precip_nc_file2 = 'C:\\Users\\Yadav\\Desktop\\Pecan opensource\\new images\\2003.nc'
precip_nc_file3 = 'C:\\Users\\Yadav\\Desktop\\Pecan opensource\\new images\\2004.nc'
precip_nc_file4 = 'C:\\Users\\Yadav\\Desktop\\Pecan opensource\\new images\\2005.nc'
nc1 = netCDF4.Dataset(precip_nc_file1, mode='r')
nc2 = netCDF4.Dataset(precip_nc_file2, mode='r')
nc3 = netCDF4.Dataset(precip_nc_file3, mode='r')
nc4 = netCDF4.Dataset(precip_nc_file4, mode='r')
print(nc1.variables.keys())
print(nc2.variables.keys())
print(nc3.variables.keys())
print(nc4.variables.keys())
time1=nc1.variables['time']
time2=nc2.variables['time']
time3=nc3.variables['time']
time4=nc4.variables['time']
dtime1 = netCDF4.num2date(time1[:],time.units)
dtime2 = netCDF4.num2date(time2[:],time.units)
dtime3 = netCDF4.num2date(time3[:],time.units)
dtime4 = netCDF4.num2date(time4[:],time.units)
LAI1=nc1.variables['LAI'][:]
LAI2=nc2.variables['LAI'][:]
LAI3=nc3.variables['LAI'][:]
LAI4=nc4.variables['LAI'][:]
LAI1=np.ravel(LAI1)
LAI2=np.ravel(LAI2)
LAI3=np.ravel(LAI3)
LAI4=np.ravel(LAI4)
print(np.shape(LAI1))
print(np.shape(LAI2))
print(np.shape(LAI3))
print(np.shape(LAI4))
print(LAI1)
print(LAI2)
print(LAI3)
print(LAI4)
#print(dtime)
precip_ts1 = pd.Series(LAI1, index=dtime1) 
precip_ts2 = pd.Series(LAI2, index=dtime2) 
precip_ts3 = pd.Series(LAI3, index=dtime3) 
precip_ts4 = pd.Series(LAI4, index=dtime4) 
precip_ts1.to_csv('2002.csv',index=True, header=True)
precip_ts2.to_csv('2003.csv',index=True, header=True)
precip_ts3.to_csv('2004.csv',index=True, header=True)
precip_ts4.to_csv('2005.csv',index=True, header=True)
import pandas as pd
df1=pd.read_csv('2002.csv')
df2=pd.read_csv('2003.csv')
df3=pd.read_csv('2004.csv')
df4=pd.read_csv('2005.csv')
df = pd.concat([df1,df2,df3,df4])
df.to_csv('LAI.csv',index=True, header=True)