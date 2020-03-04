from xlrd import open_workbook
import os


def test_xlsx(name):
    '''设置一个空列表'''
    cls = []
    '''把xlsx路径参数化'''
    xlsxpath = os.path.join('493.xls')
    '''打开xlsx表格'''
    file = open_workbook(xlsxpath)
    '''给表单赋值，并参数化'''
    sheet = file.sheet_by_name(name)
    '''读取'''
    nrows = sheet.nrows

    for i in range(nrows):
        if sheet.row_values(i)[0] != 'case_name':
            cls.append(sheet.row_values(i))

    return cls


