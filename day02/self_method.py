


    # range(10)       #从0开始小于10
    # range(5,10)     #从5开始小于10
    # range(2,10,2)   #从2开始小于10且步长2
    # range(10,2,-1)  #从10开始大于2且步长-1
    # alist = range(10) #声明一个0-9的数组


    # for i in range(1,10):
    #     for j in range(1,10):
    #         if i<=j :
    #             a = i * j
    #             print('%s * %s = %s' % (i, j, a),end='\t')
    #             if j == 9:
    #                 print()

    # for i in range(0,5):
    #     for j in range(i,5):
    #         print('*',end='   ')
    #     print()

    # a = 20
    # b = 30
    # if a>b:
    #     print(a)
    # else:
    #     print(b)

    # a = 1
    # b = 2
    # c = 3
    # if a>b:
    #     print(a)
    # elif c>a:
    #     print(c)
    # else:
    #     print(b)
    # pass


    # blist =[]
    # alist = range(1,10)
    # print(type(alist))
    # print(alist[5])
    # for i in range(0,9):
    #     blist.append(i)
    # print(blist)

    # 周末作业
    # 写一个方法,传入两个 int参数, 将两个参数之间的 偶数加起来
def int():
    a = 2
    b = 100
    sum = 0
    if a < b:
        for i in range(a + 1, b):
            if i % 2 == 0:
                sum += i
    elif a > b:
        for i in range(b + 1, a):
            if i % 2 == 0:
                sum += i
    else:
        print('两数相等')
    print(sum)

if __name__ == '__main__':
    int()
    pass