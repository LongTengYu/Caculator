from Appium.XueQiuObject.BasePage import Base_Page
from appium import webdriver
from Appium.XueQiuObject.main import Main


class App(Base_Page):
    def start(self):
        package = 'com.xueqiu.android'  # 声明包名变量
        activity = 'com.xueqiu.android.main.view.MainActivity'  # 声明首页界面变量
        if self.driver is None:
            des = {}
            des['platformName'] = 'Android'  # 操作系统名称
            des['platformVersion'] = '6.0'  # 操作系统版本
            des['deviceName'] = 'emulator-5554'  # 连接设别ID
            des['appPackage'] = package  # 被调用程序包名
            des['appActivity'] = activity  # 被调用首页界面
            des['noReset'] = 'true'  # 不重置操作选项
            des['unicodeKeyBaord'] = 'true'  # 设置 unicode属性，设置完成后可以输入中文
            des['resedKeyBoard'] = 'true'  # 与上一个属性一起使用
            self.driver = webdriver.Remote('http://localhost:4723/wd/hub', des)  # 调用被测app
            self.driver.implicitly_wait(3)  # 隐式等待
        else:
            self.driver.start_activity(package, activity)  # 若driver不为None，则直接通过start_activity连接被测app

    def main(self):
        return Main(self.driver)  # 调用Main页面
