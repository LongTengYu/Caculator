from time import sleep

from APITest.Model import test_demo
import pytest


class Test_MailList():
    def setup(self):
        self.add_member = test_demo()

    @pytest.mark.parametrize('userid,name,mobile,department',
                             [('jina', '吉娜', '13511110001', [1]),
                              ('andelei', '安德烈', '13511110002', [1])])
    def test_add_member(self, userid, name, mobile, department):
        # self.add_member = test_demo()
        d=self.add_member.delect_user(userid)
        sleep(2)
        r = self.add_member.creat_user(userid, name, mobile, department)
        assert r.get('errmsg') == 'created'

if __name__=='__main__':

    pytest.main(['TestCase.py', '-v', '-s'])


