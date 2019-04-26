from Common import Request,Assert,read_excel,Tools
import allure
import pytest

request = Request.Request()
assertions = Assert.Assertions()
iphone = Tools.phone_num()
username = Tools.random_str_abc(3) + Tools.random_123(3)
newpwd = Tools.random_str_abc(4) + Tools.random_123(2)
url='http://192.168.1.137:1811/'
head={}
@allure.feature('用户模块')
class Test_login:


        @allure.story('注册')
        def test_zhuce(self):
            zhuce_resp = request.post_request(url=url + 'user/signup',
                                                json={"phone":iphone, "pwd": "abcd12345678",
                                                      "rePwd": "abcd12345678", "userName": username})

            zhuce_resp_json = zhuce_resp.json()
            assertions.assert_code(zhuce_resp.status_code,200)
            assertions.assert_in_text(zhuce_resp_json['respBase'],'成功')
        @allure.story('登录')
        def test_login(self):
            login_resp = request.post_request(url=url + 'user/login',
                                                json={"pwd": 'hjc19940225', "userName": 'abss256'})
            login_resp_json = login_resp.json()
            assertions.assert_code(login_resp.status_code, 200)
            assertions.assert_in_text(login_resp_json['respDesc'], '成功')
        @allure.story('修改密码')
        def test_xiugai(self):
            xiugai_resp = request.post_request(url=url + 'user/changepwd',
                                                json={"newPwd": 'hjc19940225', "oldPwd": "abcd12345678",
                                                      "reNewPwd": 'hjc19940225', "userName": "abss256"})
            xiugai_resp_json = xiugai_resp.json()
            assertions.assert_code(xiugai_resp.status_code, 200)
            assertions.assert_in_text(xiugai_resp_json['respDesc'], '成功')
        @allure.story('冻结用户')
        def test_dongjie(self):
            dongjie_resp = request.post_request(url=url + 'user/lock', params={'userName': 'abss256'},headers={"Content-Type": "application/x-www-form-urlencoded"})
            dongjie_resp_json = dongjie_resp.json()
            assertions.assert_code(dongjie_resp.status_code, 200)
            assertions.assert_in_text(dongjie_resp_json['respDesc'], '成功')
        @allure.story('用户解冻')
        def test_jiedong(self):
            jiedong_resp = request.post_request(url=url + 'user/unLock', params={'userName': 'abss256'},
                                                headers={"Content-Type": "application/x-www-form-urlencoded"})
            jiedong_resp_json = jiedong_resp.json()
            assertions.assert_code(jiedong_resp.status_code, 200)
            assertions.assert_in_text(jiedong_resp_json['respDesc'], '成功')









