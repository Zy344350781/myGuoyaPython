import time

from Demo.Common import Assert
from Demo.Common import baseui

assertions = Assert.Assertions()
id = []
orderSn = []
class TestDemo1:
    def test_demo1(self,driver):
        base = baseui.baseUI(driver)
        base.click("点击订单",'//span[text()="订单"]')
        base.click("点击订单列表",'//span[text()="订单列表"]')
        base.click("点击订单状态",'//label[text()="订单状态："]/following-sibling::div')
        base.click("点击待发货",'//span[text()="待发货"]')
        base.click("点击查询搜索",'//span[contains(text(),"查询搜索")]')
        base.scroll_screen("滚动窗口")
        # base.click("点击条数",'//span[contains(text(),"共 ")]/following-sibling::span[1]//div/div')
        # base.click("点击5条",'//span[text()="5条/页"]')
        yeShu = driver.find_elements_by_xpath('//li[@class="number"]')
        if len(yeShu) >= 1:
            base.click("点击下一页", '(//span[text()="前往"]/preceding-sibling::button)[2]')
        check_box = driver.find_elements_by_xpath('//input[@type="checkbox"]')
        for i in range(1,len(check_box)):
            id_xpath = '((//tbody)[1]/tr/td[2]/div)[%s]'%(i)
            orderSn_xpath = '((//tbody)[1]/tr/td[3]/div)[%s]'%(i)
            id_text = base.get_text("获取编号", id_xpath)
            orderSn_text = base.get_text("获取订单编号",orderSn_xpath)
            id.append(id_text)
            orderSn.append(orderSn_text)
        base.click("点击全选",'(//label[@role="checkbox"])[1]')
        base.click("点击批量操作",'//input[@placeholder="批量操作"]/parent::div')
        base.click("点击批量发货",'//span[text()="批量发货"]')
        base.click("点击确定",'(//span[contains(text(),"确定")])[1]')
        for i in range(1,len(id)+1):
            base.click("点击配送方式",'((//tbody)[1]/tr[%s]/td[6])/div/div'%(i))
            base.click("点击顺丰快递",'(//span[text()="顺丰快递"])[%s]'%(len(id)))
            base.send_keys("输入物流单号",'((//tbody)[1]/tr[%s]/td[7])/div/div/input'%i,"20190404000000%s"%i)
        base.click("点击确定提交",'//span[text()="确定"]')
        base.click("点击确定",'//p[text()="是否要进行发货操作?"]/following::span[contains(text(),"确定")]')
        faHuo = base.get_text("发货成功", '//div[@role="alert"]/p')
        assertions.assert_in_text(faHuo,"发货成功")
        base.click("点击订单状态", '//label[text()="订单状态："]/following-sibling::div')
        base.click("点击待发货", '//span[text()="已发货"]')
        for i in range(1,len(id)+1):
            base.send_keys("输入订单编号",'//label[text()="输入搜索："]/following-sibling::div//input',orderSn[i-1])
            base.click("点击查询搜索", '//span[contains(text(),"查询搜索")]')
            id_xpath_ = driver.find_elements_by_xpath('(//tbody)[1]/tr/td[2]')
            b = False
            for n in id_xpath_:
                if n.text == id[i-1]:
                    b = True
            assert b == True
        time.sleep(2)
