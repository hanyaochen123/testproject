import xlrd
res=xlrd.open_workbook('493.xls')
s=res.sheet_by_index(0)
print(s.cell(0,0).value)
import pymysql
from parameterized import parameterized