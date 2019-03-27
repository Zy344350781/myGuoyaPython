import allure
from Demo.Common import Assert
from Demo.Common import Request

assertions = Assert.Assertions()
request = Request.Request()
myToken = ''
head = {''}
id_list = []

@allure.feature('登录模块')
class TestLogin(object):
    @allure.story('登录功能')
    def test_login(self):
        login_url = 'http://192.168.60.132:8080/admin/login'
        login_data = {'username':'admin','password':'123456'}
        login_response = request.post_request(url=login_url, json=login_data)
        assertions.assert_code(login_response.status_code,200)
        login_json = login_response.json()
        json_data = login_json['data']
        token = json_data['token']
        tokenHead = json_data['tokenHead']
        global myToken
        global head
        myToken = tokenHead+' '+token
        head = {'Authorization':myToken}

    @allure.story('获取登录信息功能')
    def test_info(self):
        info_url = 'http://192.168.60.132:8080/admin/info'
        info_response = request.get_request(url=info_url, headers=head)
        assertions.assert_code(info_response.status_code,200)

    @allure.story('查询订单功能')
    def test_list(self):
        list_url = 'http://192.168.60.132:8080/order/list'
        list_param = {'orderSn':201809130102000006}
        list_response = request.get_request(url=list_url, params=list_param, headers=head)
        assertions.assert_code(list_response.status_code,200)
        list_json = list_response.json()
        list_data = list_json['data']
        list_list = list_data['list']
        for i in list_list:
            i_list = i['id']
            global id_list
            id_list.append(i_list)

    @allure.story('批量关闭订单')
    def test_close(self):
        close_url = 'http://192.168.60.132:8080/order/update/close'
        close_param = {'ids':id_list[0],'note':'已关闭'}
        close_response = request.post_request(url=close_url, params=close_param, headers=head)
        assertions.assert_code(close_response.status_code,200)



