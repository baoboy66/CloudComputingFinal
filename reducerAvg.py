# Compute the average


#!/usr/bin/env python

from operator import itemgetter
import sys

sum = 0
count = 0

for line in sys.stdin:

        line = line.strip()

        try:
                temp = int(line)
        except ValueError:
                continue

        sum = sum + temp
        count = count + 1

avg = sum/count

print '%s\t' % (avg)
