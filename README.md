# PecanTasks
Gsoc task given for evaluation
In the following task given we must compare the values of lai vs Ndvi by pecan and gee

1)In first task we have used pecan and gathered some insights for the LAI vs time series for each individual year and plotted as shown then the other outputs were taken screenshots of but this doesnt show continuous time series so using python The .nc files were converted to .csv files of each year say 2002.nc to 2002.csv using test.py then all of them were combined using concat.py and LAI was plotted using plot.py
2)In second task we used python api for gee and used image data using ee collection the task was to calculate nvdi formula
nvdi=(nir-red)/(nir+red) which were retrieved from image but since we were dealing with image collection we wanted to map nvdi for images and fetch data point from single image but that resulted in failure so we used only single image and used reducecolumn and reducer to convert image to datapoints into list then using numpy we have data points the value no. of pixels was found by using trial and error so we can plot data equal to no of dates and no of lai tuples in concated csv file which was uploaded to google colab the ndvi values were concatednated 
3)The file was downloaded and plot was used on lai and ndvi to get plot finally  
