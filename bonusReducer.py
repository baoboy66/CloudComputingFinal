#!/usr/bin/env python
import sys
import re

def natural_keys(text):
        return [ int(text) ]


# maps words to their counts
tmaxcount = {}
count = 0
# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    tmax = line.strip()
    count = count + 1
    try:
        tmaxcount[tmax] = tmaxcount[tmax] + 1
    except:
        tmaxcount[tmax] = 1

# write the tuples to stdout
# Note: they are unsorted

count = count/2
keyList = tmaxcount.keys()
keyList.sort(key=natural_keys)
for tmax in keyList:
    count = count - tmaxcount[tmax]
    if count <= 0:
        print 'Median: %s'% ( tmax)
        break
