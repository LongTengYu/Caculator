import os

import yaml
import pytest
import allure
class Test_Case():

    @pytest.mark.parametrize('data',
                             yaml.safe_load(open('Test.yaml', encoding='utf-8')))  # 加载yaml测试数据
    def test_add_contact(self, data):
        # print(name,sex,email,addressname,seachaddress)
        print()
        print(data)
        print(type(data))
        print(data['email'])



if __name__ == '__main__':
    pytest.main(['--alluredir','Report','Test.py', '-vs'])
    split='allure '+'generate '+'Report '+'-o '+'Report/HtmlReport '+'--clean'
    os.system(split)

