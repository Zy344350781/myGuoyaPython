import requests

class Login(object):
    def login(self):
        login_url = 'http://192.168.60.132:8080/admin/login'
        login_json = {'username':'admin','password':'123456'}
        response_login = requests.post(url=login_url,json=login_json)
        print(response_login.text)
        json_login = response_login.json()
        login_data = json_login['data']
        self.token = login_data['token']
        self.tokenHead = login_data['tokenHead']
        assert 'token' in json_login['data']

class Info(Login):
    def info(self):
        self.login()
        info_url = 'http://192.168.60.132:8080/admin/info'
        self.head = {'Authorization':self.tokenHead+' '+self.token}
        response_info = requests.get(url=info_url, headers=self.head)
        print(response_info.text)
        json_info = response_info.json()
        assert 200 == json_info['code']

if __name__ == '__main__':
    # a = Login()
    # a.login()
    b = Info()
    b.info()