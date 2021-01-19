from Appium.XueQiuObject.BasePage import Base_Page
from Appium.XueQiuObject.market import Market


class Main(Base_Page):
    def goto_market(self):
        self.steps('main.yaml')  # 通过yaml数据驱动，操作Main页面控件
        return Market(self.driver)  # 调用Market页面
