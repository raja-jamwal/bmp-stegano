@echo off
echo "Configuring system"
python Configure.py
python Makespec.py --onefile --console -nbmp-stegano bmp.py
echo "Builiding executable"
python Build.py bmp-stegano\bmp-stegano.spec
echo "Builiding installer (NSIS)"
copy bmp-stegano\dist\bmp-stegano.exe bmp-stegano.exe
makensis stegano_nullsoft.nsi
echo "installer saved in stegano_installer.exe"
echo "binary saved in bmp-stegano.exe"