import requests

from day04.Class_login import Class_login

class Class_adminInfo:
    def test_info(self):
        a = Class_login()
        a.login_login()
        url_adminInfo = 'http://192.168.60.132:8080/admin/info'
        head_adminInfo = {'Authorization':a.tokenHead+' '+a.token}
        get_adminInfo = requests.get(url=url_adminInfo, headers=head_adminInfo)
        print(get_adminInfo.text)