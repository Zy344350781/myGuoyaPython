import allure
from day06.Common import Request
from day06.Common import Assert
from day06.Common import read_excel
import pytest

request = Request.Request()
assertions = Assert.Assertions()
excel_list = read_excel.read_excel_list('./doctment/test.xlsx')
ids =[]
for i in range(len(excel_list)):
    ids.append(excel_list[i].pop())

@allure.feature("演示")
class TestLogin(object):
    @allure.story("演示功能")
    @pytest.mark.parametrize(
        "name,pwd,msg",excel_list,
        ids=ids
    )
    def test_login(self,name,pwd,msg):
        login_url = 'http://192.168.60.132:8080/admin/login'
        login_data = {'username':name,'password':pwd}
        login_response = request.post_request(url=login_url, json=login_data)
        login_json = login_response.json()
        assertions.assert_in_text(login_json['message'],msg)