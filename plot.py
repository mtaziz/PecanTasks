import matplotlib.pyplot as plt
from datetime import datetime, timedelta
from matplotlib import dates as mpl_dates
import pandas as pd
plt.style.use('seaborn')

data = pd.read_csv('Newdata.csv')
print(data['NDVI'])
data['DATE'] = pd.to_datetime(data['DATE'])
data.sort_values('DATE', inplace=True)
date = data['DATE']
LAI = data['LAI']
NDVI=data['NDVI']
plt.plot(date,LAI, label="LAI")
plt.plot(date,NDVI, label="NDVI")
plt.plot()
plt.xlabel("x axis")
plt.ylabel("y axis")
plt.title("Line Graph Example")
plt.legend()
plt.show()

