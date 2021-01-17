from Appium.WeChatWork.Public.BasePage import Base_Page
from Appium.WeChatWork.PageObject.AddContactPage import AddContact_Page


class Contacts_Page(Base_Page):
    def goto_addcontact(self):
        self.move_page_seach('添加成员')  # 滑动页面找到“添加成员”按钮，并点击
        return AddContact_Page(self.driver)
