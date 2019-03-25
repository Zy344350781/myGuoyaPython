import requests

if __name__ == '__main__':
    url_login = 'http://192.168.60.132:8080/admin/login'
    json_login ={'username':'admin','password':'123456'}
    post_login = requests.post(url=url_login, json=json_login)
    print(post_login.text)
    json_login_ = post_login.json()
    data_login = json_login_['data']
    token_login = data_login['token']
    tokenHead_login = data_login['tokenHead']
    assert 200 == json_login_['code']

    url_adminInfo = 'http://192.168.60.132:8080/admin/info'
    head_login = {'Authorization':tokenHead_login+' '+token_login}
    get_adminInfo = requests.get(url=url_adminInfo, headers=head_login)
    print(get_adminInfo.text)
    json_adminInfo = get_adminInfo.json()
    assert 200 == json_adminInfo['code']

    url_list = 'http://192.168.60.132:8080/order/list'
    param_list = {'orderSn':201809130102000006}
    get_list = requests.get(url=url_list, params=param_list, headers=head_login)
    print(get_list.text)
    json_list = get_list.json()
    data_list = json_list['data']
    list_list = data_list['list']
    id_list = []
    for i in list_list:
        i_list = i['id']
        id_list.append(i_list)
    assert 200 == json_list['code']

    url_orderInfo = 'http://192.168.60.132:8080/order/%s'%id_list[0]
    get_orderInfo = requests.get(url=url_orderInfo, headers=head_login)
    print(get_orderInfo.text)
    json_orderInfo = get_orderInfo.json()
    data_orderInfo = json_orderInfo['data']
    status_orderInfo = data_orderInfo['status']
    assert 200 == json_orderInfo['code']

    url_receiverInfo = 'http://192.168.60.132:8080/order/update/receiverInfo'
    json_receiverInfo = {"orderId": id_list[0],"receiverName": "大大力","status": status_orderInfo}
    post_receiverInfo = requests.post(url=url_receiverInfo, json=json_receiverInfo, headers=head_login)
    print(post_receiverInfo.text)
    json_receiverInfo_ = post_receiverInfo.json()
    assert 1 == json_receiverInfo_['data']

    url_note = 'http://192.168.60.132:8080/order/update/note'
    param_note = {'id':id_list[0],'note':'测试','status':status_orderInfo}
    post_note = requests.post(url=url_note, params=param_note, headers=head_login)
    print(post_note.text)
    json_note = post_note.json()
    assert 1 == json_note['data']
    pass