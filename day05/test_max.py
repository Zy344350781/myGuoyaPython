import allure#导入allure_pytest模块

@allure.feature("类上装饰器")

class TestZy:#以Test开头命名类

    @allure.story("Max1方法上的装饰器")
    def testMax1(self):#以test开头命名方法名
        assert 1>2

    @allure.story("Max2方法上的装饰器")
    def testMax2(self):
        assert 5<6

    @allure.story("Max3方法上的装饰器")
    def testMax3(self):
        assert 3>2