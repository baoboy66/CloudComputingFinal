import sys
import csv

# input comes from STDIN (standard input)
flag = True
for line in csv.reader(iter(sys.stdin.readline, '')):
        if(flag):
                flag = False
                continue
        qflag = line[5]
        if qflag == '':
                if line[2] == 'TMAX':
                        print '%s\t' % (line[3])
