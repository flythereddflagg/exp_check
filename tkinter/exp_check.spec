# -*- mode: python ; coding: utf-8 -*-
import os
APP_NAME = "Exp Check"
MAIN_APP = "main.py"
block_cipher = None


data = [
    ("./data/exp_check.ico", "./data"),
    ("./data/search_icon.png", "./data"),
    ("../LICENSE", ".")
]

bins = []

a = Analysis(
    [MAIN_APP],
    binaries=bins,
    datas=data,
    hiddenimports=[],
    hookspath=[],
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False
)
pyz = PYZ(
    a.pure, 
    a.zipped_data,
    cipher=block_cipher
)
exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name=APP_NAME,
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    icon="./data/exp_check.ico"
)
coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name=APP_NAME
)