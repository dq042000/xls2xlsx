# Windows EXE 打包指南

1. 安裝 Python 3.x 與 pip
2. 安裝相依套件：
   ```
   pip install -r requirements.txt
   ```
3. 安裝 pyinstaller：
   ```
   pip install pyinstaller
   ```
4. 執行以下指令將 main.py 打包成 EXE：
   ```
   pyinstaller --onefile --name xls2xlsx main.py
   ```
5. 產生的 EXE 會在 dist\xls2xlsx.exe，可直接於 Windows 執行。

---
如需自動化，請直接雙擊 run_xls2xlsx.bat 或執行打包後的 xls2xlsx.exe。
