from Appium.XueQiuObject.BasePage import Base_Page
from Appium.XueQiuObject.search import Search


class Market(Base_Page):
    def goto_search(self):
        self.steps('market.yaml')  # 通过yaml数据驱动，操作Market页面控件
        return Search(self.driver)  # 调用Search页面
