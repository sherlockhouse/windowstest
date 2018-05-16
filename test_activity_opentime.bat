@cd /d %~dp0
@cd test_script
adb shell svc power stayon usb
adb shell input keyevent 82
start ..\python\bin\python2.7 .\testActivity.py
exit