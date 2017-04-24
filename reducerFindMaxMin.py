# find max and min temperature


#!/usr/bin/env python

from operator import itemgetter
import sys

max = 0
min = 100
for line in sys.stdin:

        line = line.strip()
        tmin, tmax = line.split('\t',1)

        try:
                tmin = int(tmin)
                tmax = int(tmax)
        except ValueError:
                continue

        if max < tmax:
                max = tmax
        if min > tmin:
                min = tmin

print 'Min: %s\t max: %s' % (min,max)
