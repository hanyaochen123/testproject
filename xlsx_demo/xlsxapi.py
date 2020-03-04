import unittest
from xlsx_demo import excel_for
import paramunittest
'''调用封装读取xlsx'''
querylist = excel_for.test_xlsx('testapi')
@paramunittest.parametrized(*querylist)
class Excelrun(unittest.TestCase):
    def setParameters(self,case_name,method,url,data,resultType,errno,error):
        self.case_name = str(case_name)
        self.method = str(method)
        self.url = str(url)
        self.data = str(data)
        self.resultType = str(resultType)
        self.errno = str(errno)
        self.error = str(error)

    def setUp(self):
        pass

    def read_xlsx(self):
        print(self.url)

    def tearDown(self):
        pass
if __name__ == "__main__":
    unittest.main()