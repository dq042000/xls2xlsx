# 建立一個 Python Dockerfile
FROM python:3.11-slim-bookworm

# 安全性更新
RUN apt-get update && apt-get upgrade -y && apt-get clean && rm -rf /var/lib/apt/lists/*

# 設定工作目錄
WORKDIR /app

# 複製需求檔案（如果有 requirements.txt）
COPY requirements.txt ./

# 安裝相依套件
RUN pip install --no-cache-dir -r requirements.txt || true

# 複製專案程式碼
COPY . .

# 預設啟動命令（可依需求修改）
CMD ["python", "main.py"]
