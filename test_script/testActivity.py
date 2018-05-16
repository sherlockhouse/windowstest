import os
import re

sleeptime = "1"
testtimes = "3"

config_file = open('config.txt', 'rU')
for configLine in config_file:
    if (configLine.replace(' ', '').replace('\r', '').replace('\n', '') == ''):
        continue
    sleeptime = configLine.split(":")[1].replace('\n', '').replace(' ', '')
    testtimes = configLine.split(":")[3].replace('\n', '').replace(' ', '')

config_file.close()

def dosomething(textLine):
    for i in range(0, int(testtimes)) :
        os.system("C:\\Windows\\System32\\cmd.exe /c activityPerfomance.bat " + textLine.replace('\n', ' ')  + ' ' + sleeptime)
        print i + 1


file_object = open('activitynames.txt', 'rU')
try:
    for line in file_object:
        if (line.replace(' ', '').replace('\r', '').replace('\n', '') == ''):
            continue
        print line
        line.strip()
        tmpLine = re.split(r" +", line)[2].replace('\n', '')
        time_file = open('time.' + tmpLine + '.txt', 'w')
        time_file.truncate()
        time_file.close()

        dosomething(line)
        time_file = open('time.' + tmpLine + '.txt', 'r+')
        i = 0
        openTime = 0
        for timeLine in time_file:
            i += 1
            openTime += int(timeLine.split(":")[1].replace("\n", ""))
        
        if i > 0 :
            averageTime = "Average time : " + str(openTime / i)
            print averageTime
            time_file.write(averageTime)

        time_file.close()
        
finally:
    file_object.close()

