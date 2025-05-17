import sys
import os
import xlrd
from openpyxl import Workbook
import pandas as pd

def xls_to_xlsx (xls_path, xlsx_path=None):
    output_dir = "output"
    os.makedirs(output_dir, exist_ok=True)
    if not xlsx_path:
        base = os.path.splitext(os.path.basename(xls_path))[0]
        xlsx_path = os.path.join(output_dir, base + '.xlsx')
    book = xlrd.open_workbook (xls_path)
    wb = Workbook ()
    ws = wb.active
    sheet = book.sheet_by_index (0)
    for row in range (sheet.nrows):
        ws.append (sheet.row_values (row))
    wb.save (xlsx_path)
    print (f"已將 {xls_path} 轉換為 {xlsx_path}")

def html_xls_to_xlsx (xls_path, xlsx_path=None):
    output_dir = "output"
    os.makedirs(output_dir, exist_ok=True)
    if not xlsx_path:
        base = os.path.splitext(os.path.basename(xls_path))[0]
        xlsx_path = os.path.join(output_dir, base + '.xlsx')
    dfs = pd.read_html (xls_path, header=0)
    with pd.ExcelWriter (xlsx_path, engine='openpyxl') as writer:
        for idx, df in enumerate (dfs):
            sheet_name = f'Sheet {idx+1}'
            df.to_excel (writer, sheet_name=sheet_name, index=False)
    print (f"已將 HTML 格式 {xls_path} 轉換為 {xlsx_path}")

if __name__ == "__main__":
    data_dir = "data"
    if not os.path.exists (data_dir):
        print (f"找不到 {data_dir} 資料夾")
        sys.exit (1)
    for filename in os.listdir (data_dir):
        if filename.lower ().endswith ('.xls') and not filename.lower ().endswith ('.xlsx'):
            xls_path = os.path.join (data_dir, filename)
            try:
                xls_to_xlsx (xls_path)
            except Exception as e:
                print (f"{xls_path} 不是標準 xls，嘗試用 HTML 方式轉換...")
                try:
                    html_xls_to_xlsx (xls_path)
                except Exception as e2:
                    print (f"{xls_path} 轉換失敗: {e2}")
    print ("全部轉檔完成！")