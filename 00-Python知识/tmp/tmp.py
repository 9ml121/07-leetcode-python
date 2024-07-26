import os.path
from datetime import *
from openpyxl.utils.dataframe import dataframe_to_rows

import pandas as pd
import mysql
import openpyxl


# 获取上个月日期字符串'2023-09'
# today = date.today()
today = date(2020, 8, 1)
last_month = today.replace(day=1) - timedelta(days=1)
last_month_str = last_month.strftime('%Y-%m')
# print(last_month_str)  # 2023-09

# 1.连接sr
conn = pymysql.connect(host='localhost',
                       port=3306,
                       user='root',
                       password='qq19880305',
                       db='mytest')
cursor = conn.cursor()

# 2.执行查询语句，获取表数据rows
query = f"SELECT order_id, order_date FROM orders where order_date = '2020-08-01'"
cursor.execute(query)
rows = cursor.fetchall()
# print(rows)

# 3.将查询结果转换为 DataFrame
df = pd.DataFrame(rows, columns=['order_id', 'order_date'])
# print(df)

# 4.创建一个新的 Excel 文件和工作表
workbook = openpyxl.Workbook()
sheet = workbook.active

# 5.将 DataFrame 的数据写入工作表中
for row in dataframe_to_rows(df, index=False, header=True):
    sheet.append(row)

# 6.保存 Excel 文件到指定路径
path = './'
file_name = f'report_{last_month_str}.xlsx'
save_path = os.path.join(path, file_name)
workbook.save(save_path)

print(f"Excel 文件已保存到 {save_path}")
