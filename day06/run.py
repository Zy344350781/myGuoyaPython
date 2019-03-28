import pytest
from day06.Common import Log
from day06.Common import Shell

if __name__ == '__main__':
    log = Log.MyLog()
    shell = Shell.Shell()
    xml_report_path = './Report/xml/'
    html_report_path = './Report/html/'
    pytest.main(['-s','-q','--alluredir',xml_report_path,'./TestCase/test_list.py'])
    cmd = 'allure generate %s -o %s --clean'%(xml_report_path,html_report_path)

    try:
        shell.invoke(cmd)
    except:
        log.error("执行用例失败,请检查环境配置!")
        raise