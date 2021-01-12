# SnowfallPredictor

## Description
SnowfallPredictor is a Jupyter notebook which compares the accuracy of different models in predicting the amount of snowfall on any given day based on the depth of the existing snowpack, temperature, the amount of precipitation and the date.

The models are trained and tested on data from Glacier National Park in Canada. They are also tested on data from nearby, Yoho National Park. All data was sourced from the NOAA climate data website. (www.ncdc.noaa.gov/cdo-web/)

The data is provided as a csv file with the following attributes:
* STATION
* NAME
* PROVINCE
* DATE
* MDPR = Multiday precipitation total /mm 
* MDSF = Multiday snowfall total /mm
* PRCP = Precipitation /mm
* SNOW = Snowfall /mm 
* SNWD = Snow depth /mm
* TMAX = Maximum temperature /Celsius 
* TMIN = Minimum temperature /Celsius 
