import time

from Demo.Common import Assert
from Demo.Common import baseui

assertions = Assert.Assertions()
id = []
orderSn = []
class TestDemo1:
    def test_demo1(self,driver):
        base = baseui.baseUI(driver)

