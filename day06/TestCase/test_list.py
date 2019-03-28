import allure
from day06.Common import Request
from day06.Common import Assert
from day06.Common import read_excel
import pytest

request = Request.Request()
assertions = Assert.Assertions()
head = {''}
id = []
status = []

excel_list_login = read_excel.read_excel_list('./doctment/login.xlsx')
ids =[]
for i in range(len(excel_list_login)):
    ids.append(excel_list_login[i].pop())

@allure.feature("test")
class TestLogin(object):
    @allure.story("login")
    @pytest.mark.parametrize(
        "name,pwd,msg",excel_list_login,
        ids=ids
    )
    def test_login(self,name,pwd,msg):
        login_url = 'http://192.168.60.132:8080/admin/login'
        login_data = {'username':name,'password':pwd}
        login_response = request.post_request(url=login_url, json=login_data)
        login_json = login_response.json()
        assertions.assert_in_text(login_json['message'],msg)
        # assertions.assert_code(login_json['data'],1)
        data_login = login_json['data']
        if 'token' in login_response.text:
            token = data_login['token']
            tokenHead = data_login['tokenHead']
            myToken = tokenHead + ' ' + token
            global head
            head = {'Authorization': myToken}

    @allure.story("login_info")
    def test_info(self):
        info_url = 'http://192.168.60.132:8080/admin/info'
        info_response = request.get_request(url=info_url, headers=head)
        info_json = info_response.json()
        if info_json['code'] == 200:
            assertions.assert_in_text(info_json,'username')
        else:
            assertions.assert_in_text(info_json['data','null'])

    @allure.story('list')
    def test_list(self):
        list_url = 'http://192.168.60.132:8080/order/list'
        list_param = {'pageSize':20,'pageNum':1}
        list_resp = request.get_request(url=list_url, params=list_param, headers=head)
        resp_json = list_resp.json()
        assertions.assert_code(resp_json['code'],200)
        list_data = resp_json['data']
        list_list = list_data['list']
        if list_data['total'] != 0:
            for i in list_list:
                global id
                id.append(i['id'])

    @allure.story("order_info")
    def test_order(self):
        for i in range(len(id)):
            url = 'http://192.168.60.132:8080/order/%s'%id[i]
            order_resp = request.get_request(url=url, headers=head)
            resp_json = order_resp.json()
            assertions.assert_code(resp_json['code'],200)
            order_data = resp_json['data']
            global status
            status.append(order_data['status'])

    @allure.story("moneyInfo")
    def test_moneyInfo(self):
        for i in range(len(id)):
            url = 'http://192.168.60.132:8080/order/update/moneyInfo'
            data = {'discountAmount':20,'freightAmount':8,'orderId':id[i],'status':status[i]}
            moneyInfo_resp = request.post_request(url=url, json=data, headers=head)
            resp_json = moneyInfo_resp.json()
            assertions.assert_code(resp_json['data'],1)

