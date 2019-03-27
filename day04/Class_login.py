import requests

class Class_login(object):#定义类名
    def login_login(self):#定义普通类方法
        url_login = 'http://192.168.60.132:8080/admin/login'
        json_login = {'username': 'admin', 'password': '123456'}
        post_login = requests.post(url=url_login, json=json_login)
        print(post_login.text)
        json_login_ = post_login.json()
        data_login = json_login_['data']
        self.tokenHead = data_login['tokenHead']#将要使用的变量+self.表示类.变量,可调用
        self.token = data_login['token']
        assert 'token' in json_login_['data']






