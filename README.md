# surfs_up
Jupyter Notebooks for the analysis of weather data contained in an SQLite database using SQLAlchemy.

## Overview of the analysis
Here we analyze weather data contained in [hawaii.sqlite](hawaii.sqlite) using [`SQLAlchemy`](https://www.sqlalchemy.org/). This dataset includes
temperature and precipitation measurements in Hawaii from 2010 to 2017 summarized in two tables: `measurement` including the station, date,
and the recorded precipitation and temperature, along with `station` including geographic coordinates and elevation. In this
analysis we query and summarize key differences in Hawaii weather data between the months of December and June.

### Resources
- Data Source:
  - [hawaii.sqlite](hawaii.sqlite)
- Software:
  - Python 3.7.6
  - NumPy 1.18.1
  - pandas 1.0.1
  - SQLAlchemy 1.3.13
  - Flask 1.1.1
  - Jupyter Notebook 6.0.3

## Results
The summary statistics for temperature measurements (in &deg;F) for the months of June and December are shown in
[june_temps.png](Resources/june_temps.png) and [december_temps.png](Resources/december_temps.png), respectively, and are
summarized below:

|        | June | December |
| ------ | ---- | -------- |
| count  | 1700 | 1517     |
| mean   | 74.94 | 71.04   |
| std   | 3.26 | 3.75   |
| min   | 64.00 | 56.00   |
| 25%   | 73.00 | 69.00   |
| 50%   | 75.00 | 71.00   |
| 75%   | 77.00 | 74.00   |
| max   | 85.00 | 83.00   |

Key Differences:
- Higher average temperature in June than December, as expected.
- December temperature data has larger range than that of June.
  - 27 &deg;F difference between the maximum and minimum measurement in December versus 21 &deg;F in June.
  - Also reflected in the increased standard deviation for December data.
- Roughly equal interquartile ranges between June and December data.

## Summary
We see that on average the recorded temperature was higher in June than December by 3.9 &deg;F. We also find there is a larger spread in the
December data as shown by its increased standard deviation, indicating there are likley some December days with temperatures reaching those
of June. This is also confirmed by the roughly equal maximum temperatures for each month. Considering additional weather data, we can compare
levels of precipitation between the two months using the query:
```
results = session.query(Measurement.prcp).filter(extract('month', Measurement.date) == 6).all()
```
and similarly for December. Doing so shows there are increased levels of precipitation in December, but again with greater variation in the measured
data. Further, we can list the stations by decreasing number of measurements to compare June and December temperatures at the most active station.
We do so first using:
```
session.query(Measurement.station, func.count(Measurement.station)).\
    group_by(Measurement.station).order_by(func.count(Measurement.station).desc()).all()
```
which shows "USC00519281" to be the most active station with 2,772 measurements. We then determine the minimum, maximum, and average temperature
for June at this station as follows:
```
session.query(func.min(Measurement.tobs), func.max(Measurement.tobs), func.avg(Measurement.tobs)).\
    filter(Measurement.station == 'USC00519281').filter(extract('month', Measurement.date) == 6).all()
```
Repeating this query for December again shows a higher average temperature in June (73.3 &deg;F versus 69.9 &deg;F) and further reveals this station
is likely colder than many in this dataset.

## Usage
The majority of this analysis is contained in the Jupyter Notebook file
`SurfsUp_Challenge.ipynb`. Replicating is therefore possible by first cloning
the repository and installing all dependencies into an isolated conda
environment using:
```
conda env create -f environment.yml
```
One can then open `SurfsUp_Challenge.ipynb` and run all cells. In addition,
exploratory climate analysis with visualizations can be found by running all
cells contained in `climate_analysis.ipynb`, as shown for
[Precipitation](Images/precip_vis.png). Finally, this project contains a
`Flask` application that functions as a local API server providing
precipitation, station, and temperature data through web requests. To launch
this server, navigate to the root of this repository
and run the command:
```
flask run
```
which will output:
```
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```
Open a web browser and navigate to the local host running the server, in this case
`http://127.0.0.1:5000/`, as shown in [API Home](Images/app_home.png). One can then
navigate to any of the provided routes to access the associated data, as shown in
[Precipitation Request](Images/precip_req.png). All temperature data is accessible
at the route extension `/api/v1.0/tobs`, while the minimum, average, and maximum
temperatures over a specified range can be found as shown in
[Temperature Over Range Request](Images/temp_range_req.png), where the output is of
the form `[Min_Temp, Avg_Temp, Max_Temp]`.
