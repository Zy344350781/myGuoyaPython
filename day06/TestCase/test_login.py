from day06.Common import Request
from day06.Common import Assert
import allure

request = Request.Request()
assertions = Assert.Assertions()
head = {''}
id = []

@allure.feature("登录-获取登录信息-查询商品")
class TestLogin:
    @allure.story("登录")
    def test_login(self):
        login_url = 'http://192.168.60.132:8080/admin/login'
        login_data = {'username':'admin','password':'123456'}
        login_response = request.post_request(url=login_url, json=login_data)
        assertions.assert_code(login_response.status_code,200)
        login_json = login_response.json()
        data_ = login_json['data']
        token = data_['token']
        tokenHead = data_['tokenHead']
        myToken = tokenHead+token
        global head
        head = {'Authorization':myToken}

    @allure.story("获取登录信息")
    def test_info(self):
        info_url = 'http://192.168.60.132:8080/admin/info'
        info_response = request.get_request(url=info_url, headers=head)
        assertions.assert_code(info_response.status_code,200)

    @allure.story("查询商品")
    def test_product_list(self):
        product_list_url = 'http://192.168.60.132:8080/product/list'
        product_list_param = {'pageSize':5,'pageNum':1}
        product_list_response = request.get_request(url=product_list_url, params=product_list_param, headers=head)
        assertions.assert_code(product_list_response.status_code,200)
        product_list_json = product_list_response.json()
        product_list_data = product_list_json['data']
        product_list_list = product_list_data['list']
        for i in product_list_list:
            i_list = i['id']
            global id
            id.append(i_list)

    @allure.story("更新商品")
    def test_product_update(self):
        product_update_url = 'http://192.168.60.132:8080/product/update/%s'%id[0]
        product_update_data = {'deleteStatus':1,'brandName':'大大大'}
        product_update_response = request.post_request(url=product_update_url, json=product_update_data, headers=head)
        product_update_json = product_update_response.json()
        assertions.assert_in_text(product_update_json['data'],'1')
