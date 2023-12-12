@ECHO OFF
md %USERPROFILE%\AppData\Local\RightClickConvert
Copy "A:\Data Files\Scripts\C-VR\data\favicon.ico" %USERPROFILE%\AppData\Local\RightClickConvert
regedit.exe /S data\prep-mesh-on-file.reg
setlocal

:: Define the Python installer path
set "PYTHON_INSTALLER=data\\python-3.10.11-amd64.exe"

:: Define the Python installation path
set "PYTHON_PATH=C:\\Python310"

:: Install Python
"%PYTHON_INSTALLER%" /quiet InstallAllUsers=1 PrependPath=1 TargetDir="%PYTHON_PATH%"

:: Wait for Python installation to complete
timeout /t 10

:: Install bpy
"%PYTHON_PATH%\\Scripts\\pip.exe" install bpy

endlocal
PAUSE