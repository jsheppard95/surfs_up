# surfs_up
Jupyter Notebooks for analysis of weather data contained in an SQLite database using SQLAlchemy.

## Overview of the analysis
Here we analyze weather data contained in [hawaii.sqlite](hawaii.sqlite) using [`SQLAlchemy`](https://www.sqlalchemy.org/). This dataset includes
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
- Larger range for December temperature data than that of June.
  - 27&deg;F difference between the maximum and minimum measurement in December versus 21&deg;F in June.
  - Also reflected in the increased standard deviation for December data.
- Roughly equal interquartile ranges between June and December data.

## Summary
