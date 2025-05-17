@echo off
REM Windows 批次檔，檢查 Python 與自動安裝相依套件
where python >nul 2>nul
if %errorlevel% neq 0 (
    echo 未偵測到 Python，將自動下載安裝...
    powershell -Command "Start-Process 'https://www.python.org/ftp/python/3.11.8/python-3.11.8-amd64.exe' -Wait"
    echo 請安裝完成後重新執行本檔案。
    pause
    exit /b
)

REM 直接安裝指定相依套件
python -m pip install --upgrade pip
python -m pip install xlrd openpyxl pandas lxml pyinstaller

REM 打包 main.py 為 exe
pyinstaller --onefile --name xls2xlsx main.py

REM 執行打包後的 exe
if exist dist\xls2xlsx.exe (
    dist\xls2xlsx.exe
) else (
    echo 打包失敗，請檢查 pyinstaller 設定。
)
pause
