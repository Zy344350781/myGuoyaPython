import time

def send_keys(driver,xpath,text):
    name = driver.find_element_by_xpath(xpath)
    name.clear()
    name.send_keys(text)
    time.sleep(2)

def click(driver,xpath):
    yingXiao = driver.find_element_by_xpath(xpath)
    yingXiao.click()
    time.sleep(1)