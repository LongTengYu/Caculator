import os
import pytest
import yaml
from Appium.WeChatWork.PageObject.MainPage import Main_Page
from Appium.WeChatWork.Public.SetupTeardown import test_setup_teardown
from time import *


class Test_Case(test_setup_teardown):

    @pytest.mark.parametrize('contactdata',
                             yaml.safe_load(open('Data/AddContact.yaml', encoding='utf-8')))  # 加载yaml测试数据
    def test_add_contact(self, contactdata):
        contact = Main_Page(self.driver).goto_contacts().goto_addcontact().goto_manaul_input()  # 获取添加成员页面
        contact.add_name(contactdata['name'])  # 填写名字
        contact.seach_sex(contactdata['sex'])  # 选择性别
        contact.add_email(contactdata['email'])  # 填写email
        address = contact.goto_seachaddress()  # 进入选择地址界面
        address.input_address(contactdata['addressname'])  # 填写地址
        address.seach_address(contactdata['seachaddress'])  # 选择地址
        address.input_determine()  # 点击地址页面的确定按钮
        toast = contact.input_save()  # 点击保存按钮
        assert toast == '添加成功'  # 判断是否添加成功
        sleep(2)
        self.driver.back()
        sleep(2)


if __name__ == '__main__':
    pytest.main(['--alluredir', 'Report', 'TestAddContact.py', '-vs'])
    split = 'allure ' + 'generate ' + 'Report ' + '-o ' + 'Report/HtmlReport ' + '--clean'
    os.system(split)
