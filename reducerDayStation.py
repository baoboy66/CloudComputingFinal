#!/usr/bin/env python

from operator import itemgetter
import sys

max = 0
min = 100
hotDay = ''
coldDay = ''
hotStation = ''
coldStation = ''
for line in sys.stdin:

        line = line.strip()
        tmin, tmax, station, date = line.split('\t',3)

        try:
                tmin = int(tmin)
                tmax = int(tmax)
        except ValueError:
                continue

        if max < tmax:
                max = tmax
                hotDay = date
                hotStation = station
        if min > tmin:
                min = tmin
                coldDay = date
                coldStation = station

print 'Min: %s\t Day: %s\t Station: %s\n Max: %s\t Day: %s\t Station: %s' % (min,coldDay, coldStation, max, hotDay, hotStation)
