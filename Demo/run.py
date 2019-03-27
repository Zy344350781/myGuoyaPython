from Demo.Common import Log
from Demo.Common import Shell
import pytest

if __name__ == '__main__':
    log = Log.MyLog()
    shell = Shell.Shell()
    Xml_Report_Path = './Report/xml'
    Html_Report_Path = './Report/html'
    pytest.main(['-s','-q','--alluredir',Xml_Report_Path,'./TestCase'])
    cmd = 'allure generate %s -o %s --clean'%(Xml_Report_Path,Html_Report_Path)
    try:
        shell.invoke(cmd)
    except:
        log.error('执行用例失败，请检查环境配置')
        raise