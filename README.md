# Explore US Bikeshare Data
## Description
Over the past decade, bicycle-sharing systems have been growing in number and popularity in cities across the world. Bicycle-sharing systems allow users to rent bicycles on a very short-term basis for a price. In this project, I used data provided by Motivate, a bike share system provider for many major cities in the United States, to uncover bike share usage patterns. I compared the system usage between three large cities: Chicago, New York City, and Washington, DC.

The data is filtered according to one of the following four criterias: 
1. the city 
2. the month 
3. the day of the week
4. the month and the day of the week

The program proide the following informations:
1. Popular times of travel (i.e., occurs most often in the start time)
   * most common month
   * most common day of week
   * most common hour of day

2. Popular stations and trips
   * most common start station
   * most common end station
   * most common trip from start to end (i.e., most frequent combination of start station and end station)

3. Trip duration
   * total travel time
   * average travel time

4. User info
   * counts of each user type
   * counts of each gender (only available for NYC and Chicago)
   * earliest, most recent, most common year of birth (only available for NYC and Chicago)
<br><br>

## Files used
I used the following three datasets in the program:
* [chicago.csv](chicago.csv)
* [new_york_city.csv](new_york_city.csv)
* [washington.csv](washington.csv)
<br><br>

## Software
* Language: Python 3.8 or above
* Packages: Pandas (1.1.0), re, sys, timeit
<br><br>

### License
The contents of this repository are covered under the [MIT License](LICENSE).

