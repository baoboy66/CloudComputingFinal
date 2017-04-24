
import os


def getAvgTmax():
        for i in range(0,17):
                year = 2000 + i
                command = "hadoop fs -cat /user/tatavag/PIIweather/" + str(year) + ".csv | python maxTempMapper.py | python reducer1.py"
                os.system(command)

def getAvgTmin():
        for i in range(0,17):
                year = 2000 + i
                command = "hadoop fs -cat /user/tatavag/PIIweather/" + str(year) + ".csv | python minTempMapper.py | python reducer1.py"
                os.system(command)


def getMaxMin():
        for i in range(0,17):
                year = 2000 + i
                print 'year: %s' % str(year)
                command = "hadoop fs -cat /user/tatavag/PIIweather/" + str(year) + ".csv | python mapper.py | python reducer2.py"
                os.system(command)

def getWeatherStations():
        for i in range(0,17):
                year = 2000 + i
                print 'year: %s' % str(year)
                command = "hadoop fs -cat /user/tatavag/PIIweather/" + str(year) + ".csv | python weatherstations.py | python reducer3.py"
                os.system(command)

def getHotColdDay():
        command = "hadoop fs -cat /user/tatavag/PIIweather/* | python mapper4.py | python reducer4.py"
        os.system(command)
