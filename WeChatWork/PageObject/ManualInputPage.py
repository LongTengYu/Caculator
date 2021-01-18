from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from Appium.WeChatWork.Public.BasePage import Base_Page
from Appium.WeChatWork.PageObject.SeachAddressPage import Seach_Address_Page
from time import *


class Manaul_Input_Page(Base_Page):
    def add_name(self, contactname):
        self.find_send(MobileBy.XPATH, "//*[@resource-id='com.tencent.wework:id/ern']/*/*[3]", contactname)  # 输入姓名

    def seach_sex(self, sex=None):
        self.find_click(MobileBy.XPATH, "//*[@resource-id='com.tencent.wework:id/d9j']/*[2]")  # 点击性别按钮
        if sex == 'man':
            self.find_click(MobileBy.XPATH, "//*[@resource-id='com.tencent.wework:id/boh']/*[1]/*/*")  # 获取性别男的节点
        else:
            self.find_click(MobileBy.XPATH, "//*[@resource-id='com.tencent.wework:id/boh']/*[2]/*/*")  # 获取性别女的节点

    def add_email(self, email):
        self.find_send(MobileBy.XPATH, "//*[@resource-id='com.tencent.wework:id/er1']/*/*[2]", email)  # 输入邮箱

    def goto_seachaddress(self):
        self.find_click(MobileBy.XPATH, "//*[@resource-id='com.tencent.wework:id/jr']/*[2]")  # 点击地址框，弹出地址页面
        return Seach_Address_Page(self.driver)  # 返回添加地址界面

    def input_save(self):
        locator = (MobileBy.ID, 'com.tencent.wework:id/ie7')
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(locator))
        self.find_click(MobileBy.ID, 'com.tencent.wework:id/ie7')  # 点击保存按钮
        t = (MobileBy.XPATH, '//*[@class="android.widget.Toast"]')
        sleep(1)
        toast = self.find(MobileBy.XPATH, '//*[@class="android.widget.Toast"]').text  # 获取保存成功提示信息
        return toast
