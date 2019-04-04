import allure,time

from day07.Common.Assert import Assertions
from day07.Common.baseui import baseUI

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
        base = baseUI(driver)
        base.click("点击营销",'(//span[contains(text(),"营销")])[1]')
        base.click("点击优惠券列表",'(//span[contains(text(),"优惠券列表")])[1]')
        source = driver.page_source
        assertions.assert_in_text(source, "优惠券列表")
        time.sleep(1)
        base.send_keys("输入优惠券名称",'//input[@placeholder="优惠券名称"]',"全品类通用券")
        base.click("点击查询搜索",'(//span[contains(text(),"查询搜索")])[1]')
        source = driver.page_source
        assertions.assert_in_text(source, "共 5 条")
        base.click("点击查看",'(//span[contains(text(),"查看")])[1]')
        base.click("点击全部",'//input[@type="text"and@placeholder="全部"]')
        base.click("点击未使用",'(//span[contains(text(),"未使用")])[1]')
        base.click("点击查询搜索",'(//span[contains(text(),"查询搜索")])[1]')
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
        base = baseUI(driver)
        base.click("点击商品",'//span[@slot="title"and contains(text(),"商品")]')
        base.click("点击添加商品",'//span[contains(text(),"添加商品")]')
        time.sleep(1)
        source = driver.page_source
        assertions.assert_in_text(source,"下一步，填写商品促销")
        base.click("点击商品分类",'(//label[contains(text(),"商品分类")]/following-sibling::div//span)[1]')
        # shangPinFenLei = driver.find_element_by_xpath('(//label[contains(text(),"商品分类")]/following-sibling::div//span)[1]')
        # shangPinFenLei.click()#click报错,就是点击位置或元素不对,尝试切换其他
        # time.sleep(1)
        base.click("点击手机数码",'//li[contains(text(),"手机数码")]')
        base.click("点击手机通讯",'//li[contains(text(),"手机通讯")]')
        base.send_keys("输入商品名称",'//label[contains(text(),"商品名称")]/following-sibling::div//input',"iPhone")
        # shangPinMingCheng = driver.find_element_by_xpath('//label[contains(text(),"商品名称")]/following-sibling::div//input')
        # shangPinMingCheng.clear()#输入文本前先清除文本框
        # shangPinMingCheng.send_keys("iPhone")
        # time.sleep(1)
        base.send_keys("输入副标题",'//label[contains(text(),"副标题")]/following-sibling::div//input',"苹果")
        base.click("点击商品品牌",'//label[contains(text(),"商品品牌")]/following-sibling::div//input')
        base.click("点击苹果",'//span[contains(text(),"苹果")]')
        base.send_keys("输入商品介绍",'//label[contains(text(),"商品介绍：")]/following-sibling::div//textarea',"这是一款最新的苹果手机,50英寸大屏幕,8卡8待,16个扬声器,搭载英特尔I20-128核-30代处理器")
        base.send_keys("输入商品货号",'//label[contains(text(),"商品货号：")]/following-sibling::div//input',"123456789")
        base.send_keys("输入商品售价",'//label[contains(text(),"商品售价：")]/following-sibling::div//input',"12,345,678")
        base.send_keys("输入市场价",'//label[contains(text(),"市场价：")]/following-sibling::div//input',"12,345,678")
        base.send_keys("输入商品库存",'//label[contains(text(),"商品库存：")]/following-sibling::div//input',"1")
        base.send_keys("输入计量单位",'//label[contains(text(),"计量单位：")]/following-sibling::div//input',"元")
        base.send_keys("输入商品重量",'//label[contains(text(),"商品重量：")]/following-sibling::div//input',"200")
        base.send_keys("输入排序",'//label[contains(text(),"排序")]/following-sibling::div//input',"1")
        time.sleep(1)
        base.click("点击下一步",'//span[contains(text(),"下一步，填写商品促销")]')
        source = driver.page_source
        assertions.assert_in_text(source, "下一步，填写商品属性")

        base.send_keys("输入赠送积分",'//label[contains(text(),"赠送积分：")]/following-sibling::div//input',"10")
        base.send_keys("输入赠送成长值",'//label[contains(text(),"赠送成长值：")]/following-sibling::div//input',"10")
        base.send_keys("输入积分购买限制",'//label[contains(text(),"积分购买限制：")]/following-sibling::div//input',"100")
        base.click("点击预告商品",'//label[contains(text(),"预告商品：")]/following-sibling::div//span')
        base.click("点击商品上架",'//label[contains(text(),"商品上架：")]/following-sibling::div//span')
        base.click("点击新品",'//span[text()="新品"]/following-sibling::div[1]//span')
        base.click("点击推荐",'//span[text()="推荐"]/following-sibling::div//span')
        base.click("点击免费包邮",'//span[contains(text(),"免费包邮")]')
        base.send_keys("输入详细页标题",'//label[contains(text(),"详细页标题：")]/following-sibling::div//input',"苹果手机专卖")
        base.send_keys("输入详细页描述",'//label[contains(text(),"详细页描述：")]/following-sibling::div//input',"这是一款高端大气上档次的手机")
        base.send_keys("输入商品关键字",'//label[contains(text(),"商品关键字：")]/following-sibling::div//input',"苹果")
        base.send_keys("输入商品备注",'//label[contains(text(),"商品备注：")]/following-sibling::div//textarea',"好东西啊,快买啊!")
        base.click("点击特惠促销",'//span[contains(text(),"特惠促销")]')
        base.send_keys("输入开始时间",'//div[contains(text(),"开始时间：")]/child::div//input',"2019-04-02 13:14:08")
        base.send_keys("输入结束时间",'//div[contains(text(),"结束时间：")]/child::div//input',"2020-04-02 13:14:08")
        base.send_keys("输入促销价格",'//div[contains(text(),"促销价格：")]/child::div//input',"123,456")
        base.click("点击下一步",'//span[contains(text(),"下一步，填写商品属性")]')
        source = driver.page_source
        assertions.assert_in_text(source, "下一步，选择商品关联")

        base.click("点击属性类型",'//label[contains(text(),"属性类型：")]/following-sibling::div//div/div')
        base.click("点击手机数码-手机通讯",'//span[contains(text(),"手机数码-手机通讯")]')
        base.send_keys("输入颜色",'//div[contains(text(),"颜色：")]/child::div//input','玫瑰红')
        base.click("点击增加",'//span[contains(text(),"增加")]')
        base.click("点击玫瑰红",'//span[contains(text(),"玫瑰红")]')
        base.click("点击128G",'//span[contains(text(),"128G")]')
        base.send_keys("输入屏幕尺寸",'//div[contains(text(),"屏幕尺寸:")]/following-sibling::*//input',"800 X 600")
        base.click("点击网络",'//div[contains(text(),"网络:")]/following-sibling::div')
        base.click("点击4G",'//span[text() = "4G"]')
        base.click("点击系统",'//div[contains(text(),"系统:")]/following-sibling::div')
        base.click("点击IOS",'//span[text() = "IOS"]')
        base.send_keys("输入电池容量",'//div[contains(text(),"电池容量:")]/following-sibling::*//input',"5000mA")
        #base.send_keys("上传商品相册",'//label[contains(text(),"商品相册：")]/following-sibling::div//input','C:\Users\Administrator\Pictures\sAmsnhbmuweDDdj.png')
        base.click("点击移动端详情",'//div[@id = "tab-mobile"]')
        iframe = driver.find_element_by_xpath('//div[@id="pane-mobile"]/descendant::iframe')
        driver.switch_to.frame(iframe)
        base.send_keys("输入规格参数",'//body[@id = "tinymce"]',"测试")
        driver.switch_to.default_content()
        base.click("点击下一步",'//span[contains(text(),"下一步，选择商品关联")]')
        base.click("点击完成，提交商品",'//span[contains(text(),"完成，提交商品")]')
        time.sleep(1)
        base.click("点击取消",'//span[contains(text(),"取消")]')
        time.sleep(1)
        time.sleep(5)