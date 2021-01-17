from appium.webdriver.common.mobileby import MobileBy
from Appium.WeChatWork.Public.BasePage import Base_Page


class Seach_Address_Page(Base_Page):
    def input_address(self,addressname):
        self.find_send(MobileBy.XPATH, "//*[@resource-id='com.tencent.wework:id/js']",addressname)  # 输入地址

    def seach_address(self,seachaddress):
        self.find_click(MobileBy.XPATH, f"//*[contains(@text,'{seachaddress}')]")  # 选择地址

    def input_determine(self):
        self.find_click(MobileBy.ID, 'com.tencent.wework:id/ie7')  # 点击确定按钮
