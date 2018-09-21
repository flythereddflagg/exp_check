clear
set PYTHONOPTIMIZE=1
pyinstaller .\main.py --exclude-module numpy --exclude-module scipy --icon .\exp_check.ico