# xls2xlsx 轉檔工具

## 專案簡介

本專案是一個自動化轉檔工具，能夠將 `data` 資料夾內的 `.xls` 檔案 (支援標準 Excel 及 HTML 格式) 自動轉換為 `.xlsx` 檔案，並將結果輸出到 `output` 資料夾。專案已封裝於 Python Docker 容器，方便跨平台執行。

## 功能特色

- 支援標準 Excel `.xls` 轉 `.xlsx`
- 支援 HTML 格式的 `.xls` 轉 `.xlsx`
- 批次處理 `data` 資料夾下所有 `.xls` 檔案
- 轉檔結果統一輸出至 `output` 資料夾
- 提供 Docker 化執行環境，免安裝相依套件

## 使用方式

### 1. 將待轉檔的 `.xls` 檔案放入 `data` 資料夾

### 2. Docker 執行

```sh
docker compose up --build
```

### 3. 轉檔結果

- 轉檔完成後，所有 `.xlsx` 檔案會自動產生於 `output` 資料夾。

## 主要檔案說明

- `main.py`：轉檔主程式，啟動時自動處理所有 `data` 內的 `.xls` 檔案
- `requirements.txt`：所需 Python 相依套件
- `Dockerfile`、`docker-compose.yml`：Docker 執行環境設定
- `data/`：放置待轉檔的 `.xls` 檔案
- `output/`：轉檔後的 `.xlsx` 檔案輸出資料夾

## 注意事項

- 若 `.xls` 檔案為 HTML 格式，會自動以 pandas 處理。
- 若遇到轉檔失敗，請檢查原始檔案格式或日誌訊息。

