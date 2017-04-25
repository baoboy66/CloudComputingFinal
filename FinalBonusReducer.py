#!/usr/bin/env python

from operator import itemgetter
import sys

val = []
stations = []

for line in sys.stdin:

        line = line.strip()
        temp, station = line.split('\t',1)

        try:
                temp = int(temp)
        except ValueError:
                continue

        val.append(temp)
        stations.append(station)
val, stations = (list(x) for x in zip(*sorted(zip(val,stations))))
mid = len(max)/2
print 'Median: %s\t Station: %s' % (val[mid], stations[mid])
