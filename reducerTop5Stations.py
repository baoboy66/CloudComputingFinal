#!/usr/bin/env python

from operator import itemgetter
import sys

max = [0,0,0,0,0]
hotStations = ['1','2','3','4','5']
coldStations = ['1','2','3','4','5']
min = [100,100,100,100,100]

for line in sys.stdin:

        line = line.strip()
        tmin, tmax, station = line.split('\t',2)

        try:
                tmin = int(tmin)
                tmax = int(tmax)
        except ValueError:
                continue

        if min[4] > tmin and station not in coldStations:
                min.append(tmin)
                coldStations.append(station)
                min, coldStations = (list(x) for x in zip(*sorted(zip(min,coldStations))))
                min = min[:5]
                coldStations = coldStations[:5]

        if max[0] < tmax and station not in hotStations:
                max.append(tmax)
                hotStations.append(station)
                max, hotStations = (list(x) for x in zip(*sorted(zip(max,hotStations))))
                max = max[1:]
                hotStations = hotStations[1:]


print 'High: %s\t Stations: %s' %(max, hotStations)
print 'Low: %s\t Stations: %s' %(min, coldStations)
