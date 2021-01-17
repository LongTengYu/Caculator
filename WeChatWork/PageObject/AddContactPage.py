from appium.webdriver.common.mobileby import MobileBy
from Appium.WeChatWork.Public.BasePage import Base_Page
from Appium.WeChatWork.PageObject.ManualInputPage import Manaul_Input_Page


class AddContact_Page(Base_Page):
    def goto_manaul_input(self):
        self.find_click(MobileBy.ID, 'com.tencent.wework:id/imz')  # 点击手动输入添加
        return Manaul_Input_Page(self.driver)
