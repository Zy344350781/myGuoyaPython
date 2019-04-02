import pytest,requests,allure,json,xlrd
from selenium import webdriver
import os,time

class TestFirstUIDemo:
    def test_demo1(self):
        # 打开浏览器
        # 确定chromedriver.exe的位置
        driver_path = os.path.join(os.path.dirname(__file__), "../../chromedriver/chromedriver.exe")
        print(driver_path)
        driver = webdriver.Chrome(driver_path)
        driver.maximize_window()  # 最大化浏览器
        driver.implicitly_wait(8)  # 设置隐式时间等待
        time.sleep(2)
        driver.get("https://www.baidu.com")
        time.sleep(2)
        driver.quit()