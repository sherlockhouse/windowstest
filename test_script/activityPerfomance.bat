
adb shell  am start -W -n %1 | findstr WaitTime >> time.%3.txt
adb shell am force-stop %2
adb shell sleep %4

REM @..\python\bin\python2.7 test.py %1
@exit
