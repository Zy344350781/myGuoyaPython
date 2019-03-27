# class Classname:
#     @staticmethod
#     def fun():
#         print('静态方法')
#
#     @classmethod
#     def a(cls):
#         print('类方法')
#
#     # 普通方法
#     def b(self):
#         print('普通方法')
#
#
# if __name__ == '__main__':
#
#     Classname.fun()
#     Classname.a()
#
#     C = Classname()
#     C.fun()
#     C.a()
#     C.b()

class Person:
    def __init__(self,name,age):
        self.name=name
        self.age = age
        name1=name #name1只属于_init_方法，sayhello不能使用
    def sayhello(self):
        print ('Hello, my name is:',self.name,self.age)

if __name__ == '__main__':
    p = Person('Bill', 20)
    p.sayhello()
    pass