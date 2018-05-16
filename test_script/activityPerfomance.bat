
adb shell  am start -W -n %3 | findstr WaitTime >> %2
adb shell sleep 1
adb shell am force-stop %4
if not "%5" == "" (adb shell am force-stop %5)
adb shell sleep %1


REM @..\python\bin\python2.7 test.py %1
@exit
