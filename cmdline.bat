@echo off
for %%a in (%*) do set /a num+=1
if defined num (echo 调用了 %num% 个参数) else echo 没有调用任何参数
pause