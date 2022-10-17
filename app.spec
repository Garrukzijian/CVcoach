# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(
    ['app.py'],
    pathex=['D:\\Openpose\\openpose\\CVcoach\\openpose\\bin\\python\\openpose\\Release','D:\\Openpose\\openpose\\CVcoach\\openpose\\models\\pose\\body_25'],
    binaries=[],
    datas=[(r"res\*",r"res"),
    (r"config\skin\white.qss",r"config\skin"),
    (r"models\db.sql",r"models")],
    hiddenimports=['opencv-python', 'pyopenpose'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='CVcoach',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    version="file_verison_info.txt"
)
coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='CVcoach',
)
