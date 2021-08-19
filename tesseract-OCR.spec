# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(['C:\\Users\\shinh\\OneDrive\\デスクトップ\\ohira\\python\\OCRツール\\OCR\\tesseract-OCR.py'],
             pathex=['C:\\Users\\shinh\\OneDrive\\デスクトップ\\ohira\\python\\OCRツール\\OCR'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             hooksconfig={},
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)

exe = EXE(pyz,
          Tree('C:\\Users\\shinh\\OneDrive\\デスクトップ\\ohira\\python\\OCRツール\\OCR\\tool\\data',prefix='data'),
          Tree('C:\\Users\\shinh\\OneDrive\\デスクトップ\\ohira\\python\\OCRツール\\OCR\\tool\\Tesseract-OCR',prefix='tesseract'),
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,  
          [],
          name='Tesseract-OCR',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=True,
          disable_windowed_traceback=False,
          target_arch=None,
          codesign_identity=None,
          entitlements_file=None )
