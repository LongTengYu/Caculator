import requests

class BasePage():
    # 获取token
    def __init__(self):
        corpid = 'ww446d485f1c5d2bee'
        corpsecret = 'IEvhPO__LPqbiGKlJnE3wy3l__g4LXhccVfjL94ymXU'
        url = f'https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={corpid}&corpsecret={corpsecret}'
        r = requests.get(url)
        self.access_token = r.json()['access_token']
        self.session=requests.Session()
        self.session.params={'access_token':self.access_token}

    def send(self,*args, **kwargs):
        r=self.session.request(*args,**kwargs)
        return r.json()

