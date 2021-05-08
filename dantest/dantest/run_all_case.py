# coding:utf-8
import unittest
import HTMLTestRunner
def all_case():
    #待执行用例的目录
    case_dir= "C:\\Users\\lidan\\PycharmProjects\\dantest\\dantest\\case"
    testcase=unittest.TestSuite()
    discover=unittest.defaultTestLoader.discover(case_dir,pattern='test*.py',top_level_dir=None)
#discover方法筛选出来的用例，循环添加到测试用例中
    #方法1：
    # for test_suite in discover:
    #     for test_case in test_suite:
    #         #添加测试用例到testcase
    #         testcase.addTests(test_case)
    #方法2：
    testcase.addTests(discover)

    print(testcase)
    return testcase
if __name__ =="__main__":
    #返回实例
    #runner=unittest.TextTestRunner()

    report_path='C:\\Users\\lidan\\PycharmProjects\\dantest\\dantest\\report\\result.html'
    fp=open(report_path,"wb")
    runner=HTMLTestRunner.HTMLTestRunner(stream=fp,title=u'测试报告',description=u'测试报告执行情况')
    #run所有用例
    runner.run(all_case())
    fp.close()

