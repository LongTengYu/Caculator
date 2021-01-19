from Appium.XueQiuObject.BasePage import Base_Page


class Search(Base_Page):
    def search(self, value):
        self.params["value"] = value  # 因继承Base_Page类，调用Base_Page类中self.params变量并创建一个value字典键值对
        self.steps('search.yaml')  # 通过yaml数据驱动，操作Search页面控件
