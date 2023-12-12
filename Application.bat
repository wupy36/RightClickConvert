@echo off

echo looking through files selected...

setlocal EnableExtensions DisableDelayedExpansion
pushd "%~dp0"

"C:\Program Files\Python310\python.exe" "A:\Data Files\Scripts\RightClickConvert\main.py" %*

popd
endlocal

pause