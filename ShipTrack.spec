# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(['mainWindowShiptrack.py'],
             pathex=['C:\\Users\\Zach\\Documents\\NEU\\Spring2021\\IS4300\\shiptrack'],
             binaries=[],
             datas=[('Logo.png', '.'), ('Logobackg.jpg', '.'), ('Logowhite.png', '.'), ('map.png', '.')],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='ShipTrack',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False )
