@echo off
set "psdrexafolder=%~dp0PSDRexa"
set "pyfile=%~dp0PSDRexa.py"
set "syncerfile=%~dp0PSDRexa_syncer.py"
set "dummyfile=%~dp0dummy.png"
set "base1=C:\\ProgramData\\Blackmagic Design\\DaVinci Resolve"
set "base2=C:\\Users\\%username%\\AppData\\Local\\Blackmagic Design\\DaVinci Resolve"
set "base3=C:\\Users\\%username%\\AppData\\Roaming\\Blackmagic Design\\DaVinci Resolve\\Support\\Fusion\\Settings"

python --version >nul 2>&1
if errorlevel 1 (
    echo MsgBox "Python is not installed. If you're seeing this error despite having Python installed, please ensure that the PYTHONHOME environment variable is set correctly.", vbExclamation > %temp%\tmp.vbs
    cscript /nologo %temp%\tmp.vbs
    del %temp%\tmp.vbs
    exit /b
)

python -m pip --version >nul 2>&1
if errorlevel 1 (
    echo MsgBox "pip is not installed. Please ensure that pip is installed correctly.", vbExclamation > %temp%\tmp.vbs
    cscript /nologo %temp%\tmp.vbs
    del %temp%\tmp.vbs
    exit /b
)

echo [start]Install PSDRexa

if exist "%base1%" (
    set "module_folder=%base1%\\Fusion\\Modules"
    set "script_folder=%base1%\\Fusion\\Scripts\\Utility"
) else if exist "%base2%" (
    set "module_folder=%base2%\\Fusion\\Modules"
    set "script_folder=%base2%\\Fusion\\Scripts\\Utility"
) else (
    echo MsgBox "DaVinci Resolve folder is not exists.", vbExclamation > %temp%\tmp.vbs
    cscript /nologo %temp%\tmp.vbs
    del %temp%\tmp.vbs
    exit /b
)

if exist "%module_folder%\\PSDCharacterExporter\\" (
    echo delete old PSDCharacterExporterDirectory.
    rd /s /Q "%module_folder%\\PSDCharacterExporter
)
if exist "%module_folder%\\PSDRexa\\" (
    echo delete old PSDRexaDirectory
    rd /s /Q "%module_folder%\\PSDRexa"
)


xcopy /E /I /Y "%psdrexafolder%" "%module_folder%\\PSDRexa"
cd "%module_folder%\\PSDRexa"
python -m pip install -r requirements.txt -t module


if exist "%script_folder%\\PSDCharacterExporter.py" (
    echo delete old PSDCharacterExporter
    cd %script_folder%
    del /Q PSDCharacterExporter.py
)
if exist "%script_folder%\\PSDRexa.py" (
    echo delete old PSDRexa
    cd %script_folder%
    del /Q PSDRexa.py
)
copy /Y "%pyfile%" "%script_folder%"
if exist "%script_folder%\\PSDRexa_syncer.py" (
    echo delete old PSDRexa_syncer
    cd %script_folder%
    del /Q PSDRexa_syncer.py
)
copy /Y "%syncerfile%" "%script_folder%"

copy /Y "%dummyfile%" "%base3%"

echo [end]Install PSDRexa

echo MsgBox "Install PSDRexa Success!", vbInformation, "Installation Complete" > %temp%\tmp.vbs
cscript /nologo %temp%\tmp.vbs
del %temp%\tmp.vbs

