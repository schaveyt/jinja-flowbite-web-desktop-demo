# -*- mode: python ; coding: utf-8 -*-

import os
import sys

EXE_NAME = "my_app"
COMPANY = "UNDEFINED"
ICONS = True

# Compute the icon path based on the platform and the 'icons' variable
ICON_PATH = None

if ICONS:
    if os.name == "nt": # Windows
        ICON_PATH = "icons/windows/flowbite-icon.ico"
    elif sys.platform == "linux": # Linux
        ICON_PATH = "icons/linux/flowbite-icon.png"
    elif sys.platform == "darwin": # Mac
        ICON_PATH = "icons/macos/icon.icns"

current_dir = os.path.dirname(os.path.realpath(__name__))
venv_dir = os.path.join(current_dir, "venv")
jinja_flowbite_dir = os.path.join(venv_dir, "Lib", "site-packages", "jinja_flowbite")

a = Analysis(
    ['desktop.py'],
    pathex=[current_dir],
    binaries=[],
    datas=[("my_app", "my_app"), ("test", "test"), (jinja_flowbite_dir,"jinja_flowbite")],
    upx=True,
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
)
pyz = PYZ(a.pure)

print(ICON_PATH)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name=EXE_NAME,
    icon=ICON_PATH,
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    version='my_app/win_exe_version_info.py'
)

# if targeting macOS, you'd also want to generate the .app bundle
# --COMMENT THIS OUT-- if you are bundling from a Linux or Window machine
# app = BUNDLE(exe,
#              name=f'{EXE_NAME}.app',
#              icon=ICON_PATH,
#              bundle_identifier=f'com.{COMPANY}.{EXE_NAME}')