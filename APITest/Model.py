import requests
from APITest.Base import BasePage


class test_demo(BasePage):

    # 创建用户
    def creat_user(self, userid, name, mobile, department):
        url = f'https://qyapi.weixin.qq.com/cgi-bin/user/create'
        data = {
            "userid": userid,
            "name": name,
            "mobile": mobile,
            "department": department}
        r = self.send('post', url,json=data)
        return r

    # 读取用户
    def cheak_user(self, userid):
        url = f'https://qyapi.weixin.qq.com/cgi-bin/user/get?userid={userid}'
        r = requests.get(url)
        return r

    # 修改用户
    def update_user(self, userid, name):
        url = f'https://qyapi.weixin.qq.com/cgi-bin/user/update'
        data = {
            "userid": userid,
            "name": name,
        }
        r=self.send('post',url,json=data)
        return r

    # 删除用户
    def delect_user(self, userid):
        url = f'https://qyapi.weixin.qq.com/cgi-bin/user/delete?userid={userid}'
        r = self.send('get',url)
        return r
