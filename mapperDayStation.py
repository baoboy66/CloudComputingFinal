''' This mapper function return TMIN, TMAX, Stations, Dates'''


import sys
import csv

# input comes from STDIN (standard input)
flag = True
for line in csv.reader(iter(sys.stdin.readline, '')):
        if(flag):
                flag = False
                continue
        qflag = line[5]
        tmax = 0
        tmin = 0
        if qflag == '':
                if line[2] == 'TMIN':
                        tmin = line[3]
                if line[2] == 'TMAX':
                        tmax = line[3]
                if tmax != 0 or tmin !=0:
                        print '%s\t%s\t%s\t%s' % (tmin,tmax,line[0],line[1])
