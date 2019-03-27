import pytest#导入pytest模块

if __name__ == '__main__':
    # pytest.main(['-s','q','.'])#固定写法,'.'是当前路径中所有test开头的文件
    #调用测试框架 pytest  --alluredir:制定 allure的目录地址; ../Report/xml:实际地址
    pytest.main(['-s', '-q','--alluredir','../Report/xml/', '.'])
    # allure generate ./Report/xml -o ./Report/html/ --clean #使用cmd将xml文件转成html,cmd要在项目目录下运行
    # allure serve ./Report/xml   使用Terminal打开