import requests

from day04.Class_login import Class_login#from类文件名import类名

class Class_adminInfo(Class_login):#继承Class_login父类
    def test_info(self):
        self.login_login()  # a.方法名,使用方法
        url_adminInfo = 'http://192.168.60.132:8080/admin/info'
        head_adminInfo = {'Authorization':self.tokenHead+' '+self.token}#使用方法后才能调用login类中的变量
        get_adminInfo = requests.get(url=url_adminInfo, headers=head_adminInfo)
        print(get_adminInfo.text)
        info_json = get_adminInfo.json()
        assert 200 == info_json['code']