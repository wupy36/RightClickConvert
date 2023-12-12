@ECHO OFF
md %USERPROFILE%\AppData\Local\RightClickConvert
Copy "A:\Data Files\Scripts\C-VR\data\favicon.ico" %USERPROFILE%\AppData\Local\RightClickConvert
regedit.exe /S data\prep-mesh-on-file.reg
PAUSE