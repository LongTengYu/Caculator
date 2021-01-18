from appium.webdriver.common.mobileby import MobileBy
from Appium.WeChatWork.Public.BasePage import Base_Page
from Appium.WeChatWork.PageObject.ContactsPage import Contacts_Page


class Main_Page(Base_Page):
    def goto_contacts(self):
        self.find_click(MobileBy.XPATH, "//*[@text='通讯录']")  # 点击通讯录
        return Contacts_Page(self.driver)  # 返回通讯录页面
