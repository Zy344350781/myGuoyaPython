import os,pytest,allure,time
from selenium import webdriver
from day07.Common import Assert
from day07.Common.baseui import baseUI

assertions = Assert.Assertions()
@pytest.fixture(scope = "session")
def driver():
    # 确定chromedriver.exe的位置
    driver_path = os.path.join(os.path.dirname(__file__), "../chromedriver/chromedriver.exe")
    driver = webdriver.Chrome(driver_path)# 打开浏览器
    driver.maximize_window()  # 最大化浏览器
    driver.implicitly_wait(8)  # 设置隐式时间等待
    time.sleep(2)# 等待2秒
    driver.get("file:///C:/Users/Administrator/Desktop/demo.html")
    # driver.get("http://192.168.60.132/#/login")# 打开网站
    time.sleep(1)
    # base = baseUI(driver)
    # base.send_keys('输入账号','//input[@name = "username"]',"admin")
    # # username = driver.find_element_by_xpath('//input[@name = "username"]')#从xpath中找到元素(用户名)
    # # username.clear()#清空
    # # username.send_keys("admin")#输入"admin"
    # base.send_keys('输入密码','//input[@name = "password"]',"123456")
    # # password = driver.find_element_by_xpath('//input[@name = "password"]')#从xpath中找到元素(密码)
    # # password.clear()#清空
    # # password.send_keys("123456")#输入"123456"
    # base.click('点击登录','(//span[contains(text(),"登录")])[1]')
    # # login = driver.find_element_by_xpath('(//span[contains(text(),"登录")])[1]')#从xpath中找到元素(登录按钮)
    # # login.click()#点击自己
    # # time.sleep(2)
    # source = driver.page_source
    # assertions.assert_in_text(source,"首页")
    yield driver
    driver.quit()
