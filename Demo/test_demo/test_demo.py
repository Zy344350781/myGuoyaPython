import os,time,pytest,allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from Demo.Common import baseui
from Demo.Common import Assert

assertions = Assert.Assertions()

@allure.feature("优惠券")
class TestDemo:
    @allure.story("流程1")
    def test_demo(self,driver):
        base = baseui.baseUI(driver)
        base.click("点击营销",'//span[contains(text(),"营销")]')
        base.click("点击优惠券列表",'//span[contains(text(),"优惠券列表")]')
        base.click("点击编辑",'(//span[contains(text(),"编辑")])[1]')
        base.send_keys("输入有效期到期时间",'//span[text() = "至"]/following-sibling::div//input',"2020-04-25")
        base.click("点击提交",'//span[text() = "提交"]')
        base.click("点击确定",'//p[text() = "是否提交数据"]/following::div//span[contains(text(),"确定")]')
        # WebDriverWait  driver浏览器驱动,5 最大等待时间,0.5 每0.5秒查找一次
        # until直到xpath中返回ture
        # expected_conditions.presence_of_element_located((By.XPATH, xpath)) 预期\条件.存在\元素\位置((以xpath定位,xpath))
        # WebDriverWait成功查找到元素后,会返回查找到的元素,xiuGai = ,将返回的元素赋值给xiuGai
        xpath = '//div[@role = "alert"]/child::p[contains(text(),"修改成功")]'
        xiuGai = WebDriverWait(driver, 5, 0.5).until(expected_conditions.presence_of_element_located((By.XPATH, xpath)))
        # xiuGai = base.get_text("修改成功", xpath)
        # xiuGai = base.get_text("修改成功",'//div[@role = "alert"]/child::p[contains(text(),"修改成功")]')
        assertions.assert_in_text(xiuGai.text,"修改成功")
        # assertions.assert_in_text(xiuGai, "修改成功")
        time.sleep(1)
        # expected_conditions.presence_of_element_located(By.XPATH,xpath)



