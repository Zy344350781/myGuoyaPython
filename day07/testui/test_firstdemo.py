import allure,time

from day07.Common.Assert import Assertions
from day07.Common.base_ui import *

assertions =Assertions()

@allure.feature("UI自动化")
class TestFirstUIDemo:
    @allure.story("流程1")
    def test_demo1(self,driver):
        # 确定chromedriver.exe的位置
        # driver_path = os.path.join(os.path.dirname(__file__), "../chromedriver/chromedriver.exe")
        # driver = webdriver.Chrome(driver_path)# 打开浏览器
        # driver.maximize_window()  # 最大化浏览器
        # driver.implicitly_wait(8)  # 设置隐式时间等待
        # time.sleep(2)# 等待2秒
        # driver.get("http://192.168.60.132/#/login")# 打开网站
        # time.sleep(1)
        # username = driver.find_element_by_xpath('//input[@name = "username"]')#从xpath中找到元素(用户名)
        # username.clear()#清空
        # username.send_keys("admin")#输入"admin"
        # password = driver.find_element_by_xpath('//input[@name = "password"]')#从xpath中找到元素(密码)
        # password.clear()#清空
        # password.send_keys("123456")#输入"123456"
        # login = driver.find_element_by_xpath('(//span[contains(text(),"登录")])[1]')#从xpath中找到元素(登录按钮)
        # login.click()#点击自己
        # time.sleep(2)
        # source = driver.page_source
        # assertions.assert_in_text(source,"首页")
        click(driver,'(//span[contains(text(),"营销")])[1]')
        click(driver,'(//span[contains(text(),"优惠券列表")])[1]')
        source = driver.page_source
        assertions.assert_in_text(source, "优惠券列表")
        time.sleep(1)
        send_keys(driver,'//input[@placeholder="优惠券名称"]',"全品类通用券")
        click(driver,'(//span[contains(text(),"查询搜索")])[1]')
        source = driver.page_source
        assertions.assert_in_text(source, "共 5 条")
        click(driver,'(//span[contains(text(),"查看")])[1]')
        click(driver,'//input[@type="text"and@placeholder="全部"]')
        click(driver,'(//span[contains(text(),"未使用")])[1]')
        click(driver,'(//span[contains(text(),"查询搜索")])[1]')
        source = driver.page_source
        assertions.assert_in_text(source, "共 7 条")

    @allure.story("流程2")
    def test_demo2(self,driver):
        # # 确定chromedriver.exe的位置
        # driver_path = os.path.join(os.path.dirname(__file__), "../chromedriver/chromedriver.exe")
        # driver = webdriver.Chrome(driver_path)  # 打开浏览器
        # driver.maximize_window()  # 最大化浏览器
        # driver.implicitly_wait(8)  # 设置隐式时间等待
        # time.sleep(2)  # 等待2秒
        # driver.get("http://192.168.60.132/#/login")  # 打开网站
        # time.sleep(1)
        # username = driver.find_element_by_xpath('//input[@name = "username"]')  # 从xpath中找到元素(用户名)
        # username.clear()  # 清空
        # username.send_keys("admin")  # 输入"admin"
        # password = driver.find_element_by_xpath('//input[@name = "password"]')  # 从xpath中找到元素(密码)
        # password.clear()  # 清空
        # password.send_keys("123456")  # 输入"123456"
        # login = driver.find_element_by_xpath('(//span[contains(text(),"登录")])[1]')  # 从xpath中找到元素(登录按钮)
        # login.click()  # 点击自己
        # time.sleep(2)
        # source = driver.page_source
        # assertions.assert_in_text(source, "首页")
        click(driver,'//span[@slot="title"and contains(text(),"商品")]')
        click(driver,'//span[contains(text(),"添加商品")]')
        time.sleep(1)
        source = driver.page_source
        assertions.assert_in_text(source,"下一步，填写商品促销")
        click(driver,'(//label[contains(text(),"商品分类")]/following-sibling::div//span)[1]')
        # shangPinFenLei = driver.find_element_by_xpath('(//label[contains(text(),"商品分类")]/following-sibling::div//span)[1]')
        # shangPinFenLei.click()#click报错,就是点击位置或元素不对,尝试切换其他
        # time.sleep(1)
        click(driver,'//li[contains(text(),"手机数码")]')
        click(driver,'//li[contains(text(),"手机通讯")]')
        send_keys(driver,'//label[contains(text(),"商品名称")]/following-sibling::div//input',"iPhone")
        # shangPinMingCheng = driver.find_element_by_xpath('//label[contains(text(),"商品名称")]/following-sibling::div//input')
        # shangPinMingCheng.clear()#输入文本前先清除文本框
        # shangPinMingCheng.send_keys("iPhone")
        # time.sleep(1)
        send_keys(driver,'//label[contains(text(),"副标题")]/following-sibling::div//input',"苹果")
        click(driver,'//label[contains(text(),"商品品牌")]/following-sibling::div//input')
        click(driver,'//span[contains(text(),"苹果")]')
        send_keys(driver,'//label[contains(text(),"商品介绍：")]/following-sibling::div//textarea',"这是一款最新的苹果手机,50英寸大屏幕,8卡8待,16个扬声器,搭载英特尔I20-128核-30代处理器")
        send_keys(driver,'//label[contains(text(),"商品货号：")]/following-sibling::div//input',"123456789")
        send_keys(driver,'//label[contains(text(),"商品售价：")]/following-sibling::div//input',"12,345,678")
        send_keys(driver,'//label[contains(text(),"市场价：")]/following-sibling::div//input',"12,345,678")
        send_keys(driver,'//label[contains(text(),"商品库存：")]/following-sibling::div//input',"1")
        send_keys(driver,'//label[contains(text(),"计量单位：")]/following-sibling::div//input',"元")
        send_keys(driver,'//label[contains(text(),"商品重量：")]/following-sibling::div//input',"200")
        send_keys(driver,'//label[contains(text(),"排序")]/following-sibling::div//input',"1")
        time.sleep(1)
        click(driver,'//span[contains(text(),"下一步，填写商品促销")]')
        source = driver.page_source
        assertions.assert_in_text(source, "下一步，填写商品属性")
        send_keys(driver,'//label[contains(text(),"赠送积分：")]/following-sibling::div//input',"10")
        send_keys(driver,'//label[contains(text(),"赠送成长值：")]/following-sibling::div//input',"10")
        send_keys(driver,'//label[contains(text(),"积分购买限制：")]/following-sibling::div//input',"100")
        click(driver,'//label[contains(text(),"预告商品：")]/following-sibling::div//span')
        click(driver,'//label[contains(text(),"商品上架：")]/following-sibling::div//span')
        click(driver,'//span[text()="新品"]/following-sibling::div[1]//span')
        click(driver,'//span[text()="推荐"]/following-sibling::div//span')
        click(driver,'//span[contains(text(),"免费包邮")]')
        send_keys(driver,'//label[contains(text(),"详细页标题：")]/following-sibling::div//input',"苹果手机专卖")
        send_keys(driver,'//label[contains(text(),"详细页描述：")]/following-sibling::div//input',"这是一款高端大气上档次的手机")
        send_keys(driver,'//label[contains(text(),"商品关键字：")]/following-sibling::div//input',"苹果")
        send_keys(driver,'//label[contains(text(),"商品备注：")]/following-sibling::div//textarea',"好东西啊,快买啊!")
        click(driver,'//span[contains(text(),"特惠促销")]')
        send_keys(driver,'//div[contains(text(),"开始时间：")]/child::div//input',"2019-04-02 13:14:08")
        send_keys(driver,'//div[contains(text(),"结束时间：")]/child::div//input',"2020-04-02 13:14:08")
        send_keys(driver,'//div[contains(text(),"促销价格：")]/child::div//input',"123,456")
        click(driver,'//span[contains(text(),"下一步，填写商品属性")]')
        time.sleep(5)
        source = driver.page_source
        assertions.assert_in_text(source, "下一步，选择商品关联")