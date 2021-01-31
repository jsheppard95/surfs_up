# surfs_up
Jupyter Notebooks and Flask API for analysis of weather data contained in an SQLite database.

## Overview of the analysis
Here we analyze weather data contained in [hawaii.sqlite](hawaii.sqlite) using [`sqlalchemy`](https://www.sqlalchemy.org/). This dataset includes
temperature and precipitation measurements in Hawaii from 2010 to 2017 summarized in two tables: `measurement` including the station, date,
and the recorded precipitation and temperature, along with `station` including each station's geographic coordinates and elevation. In this
analysis we query and summarize key differences in weather data between the months of December and June.

### Resources
- Data Source:
  - [hawaii.sqlite](hawaii.sqlite)
- Software:
  - Python 3.7.6
  - NumPy 1.18.1
  - pandas 1.0.1
  - SQLAlchemy 1.3.13
  - Jupyter Notebook 6.0.3

## Results
The summary statistics for temperature measurements (in &deg;F) for the months of June and December are shown in
[june_temps.png](Resources/june_temps.png) and [december_temps.png](Resources/december_temps.png), respectively. The key differences are
summarized below:

## Summary
