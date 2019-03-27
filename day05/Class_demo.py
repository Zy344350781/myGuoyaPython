import pytest
import allure_pytest
# class 类
# object 对象 / 或所有类的父类

class Human(object):
    def __init__(self,name,age,sex):#__init__初始化变量
        self.name = name#初始化变量
        self.age = age#初始化变量
        self.sex = sex#初始化变量

    def myInfo(self):
        print('我叫%s,今年%s岁,%s'%(self.name,self.age,self.sex))

class Tester(Human):
    def testing(self):
        print('我叫%s,我正在执行测试,我的详细信息在下方.'%self.name)
        self.myInfo()

if __name__ == '__main__':
    # c = Human('张喻',29,'男')
    # c.myInfo()
    tester = Tester('张喻', 29, '男')
    tester.testing()
    pass