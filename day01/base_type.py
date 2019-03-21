# def int_demo():  #声明一个方法名,def声明方法
#     aint = 1     #声明变量并赋值
#     print(aint)  #输出变量
#
# def add(num1,num2):
#      return num1+num2
#
# def sub(num3,num4):
#     return num3-num4
#    #return num2-num1                  #return返回值
#
# def str_demo():                       #str是字符串类型
#     str1 = '1'
#     print(type(str1))
#
# def number():
#     aint = 10
#     bint = 20
#     cint = 0
#     print(aint, bint)
#     cint = aint
#     aint = bint
#     bint = cint
#     print(aint, bint)
#
# def float_demo():
#     afloat = 1.584824                  #float小数类型
#     print(afloat)
#     print(type(afloat))
#
# def str_demo1():
#     a = 'hello '
#     b = 'world'
#     print(a+b)                        #字符串拼接
#     print('你好世界,%s%s'%(a,b))      #%s调用变量,%(a,b)调用a,b变量
#
# if __name__ == '__main__':            # 使用main方法
#     int_demo()                        #引用方法
#     result1 = add(4,8)                #声明result变量,引用方法并传参,赋值给sum变量
#     print(result1)
#     result2 = sub(6,85)
#     print(result2)
#     str_demo()
#     number()
#     float_demo()
#     str_demo1()
#     pass

def str_demo():
    str1 = 'Hello '
    str2 = 'World!'
    print('%s%s'%(str1,str2))

def int_demo(num1,num2):
    print('num1=%s' % num1)
    print('num2=%s' % num2)
    print('交换数值')
    z = num1
    num1 = num2
    num2 = z
    print('num1=%s' % num1)
    print('num2=%s' % num2)

def float_demo():
    aF = 1.987748456216546789156
    bF = 4.1151248788446498
    return aF + bF

def list_demo():
    alist = [1,2,3,4,5,6,7,8,9]     #声明一个数组并赋值
    print(alist[7])                 #调用数组,下标0是第一个值,-1是最后一个值
    print(alist[2:7])               #取下标2至6的值
    print(alist[:7])                #从下标0取至6
    print(alist[2:])                #从下标2取至最后

if __name__ == '__main__':
    int_demo(2,30)
    str_demo()
    float = float_demo()
    print(float)
    list_demo()




















