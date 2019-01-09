import subprocess

commands = [
    ['cls'],
    ['set', 'PYTHONOPTIMIZE=1'],
    [
        'pyinstaller',
        '.\main.py',
        '--exclude-module', 'numpy',
        '--exclude-module', 'scipy', 
        '--exclude-module', 'bz2', 
        '--exclude-module', 'contextvars', 
        '--exclude-module', 'ctypes',
        '--exclude-module', 'decimal',
        '--exclude-module', 'lzma',
        '--exclude-module', 'multiprocessing',
        '--exclude-module', 'queue',
        '--exclude-module', 'ssl',
        '--exclude-module', 'unicodedata',
        '--i', '.\exp_check.ico']
    ]

for command in commands:
    subprocess.run(command, shell=True)

