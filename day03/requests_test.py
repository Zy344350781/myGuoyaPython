import requests#调用requests模块
import json#调用json模块


if __name__ == '__main__':
    url_login = 'http://192.168.60.132:8080/admin/login'
    data = {'username':'admin','password':'123456'}#封装请求参数
    #发送请求 带上url和json(请求正文)两个参数
    post = requests.post(url=url_login, json = data)
    text_body = post.text#获取text格式的响应报文(str)
    json_body = post.json()#获取json格式的响应报文(dict)
    # print(type(text_body))
    # print(text_body)
    # print(type(json_body))
    print(json_body)

    # loads = json.loads(text_body)#使用json.loads讲str格式转换成dict格式,并赋值loads
    # print(type(loads))
    # dumps = json.dumps(loads)#使用json.dumps讲dict格式转换成str格式,并赋值dumps
    # print(type(dumps))

    # assert 200 == post.status_code#断言code码判断
    # assert '操作成功' in json_body['message']#断言message是否有'操作成功'
    # assert 200 == json_body['code']#断言code码中是否有200

    url_info = 'http://192.168.60.132:8080/admin/info'
    data_dict = json_body['data']#获取响应正文中'data'中的内容
    token_ = data_dict['token']#获取data中token内容
    token_head = data_dict['tokenHead']#获取data中tokenHead内容
    head = {'Authorization':token_head+' '+token_}#封装head,将Authorization和tokenHead/token键值对
    # 将head放入headers中发送get请求
    get_info = requests.get(url=url_info, headers=head)
    print(get_info.text)
    info_json = get_info.json()
    assert 200 == info_json['code']

    url_list = 'http://192.168.60.132:8080/order/list'#将url_list作为一个变量存入网址
    # url_list = 'http://192.168.60.132:8080/order/list?pageNum=1&pageSize=10'#get 请求,将参数直接放入url
    param_list = {'pageNum':1,'pageSize':10}#get请求,将参数封装成一个字典
    # get_list = requests.get(url=url_list, params=param_list, headers=head)
    get_list = requests.get(url=url_list,params=param_list,headers=head)#请求时将封装好的参数传入 params
    print(get_list.text)
    json_list = get_list.json()
    data_list = json_list['data']
    list_list = data_list['list']
    for i in list_list:#遍历list.list
        print(i)




