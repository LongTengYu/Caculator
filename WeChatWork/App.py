from appium.webdriver.common.mobileby import MobileBy
import pytest
from Appium.WeChatWork.Public.BasePage import Base_Page


class Test_addcontact(Base_Page):

    def test_addcontact(self):
        self.driver.find_element(MobileBy.XPATH, "//*[@text='通讯录']").click()  # 点击通讯录
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                 'new UiScrollable(new UiSelector().'
                                 'scrollable(true).instance(0)).'
                                 'scrollIntoView(new UiSelector().'
                                 'text("添加成员").instance(0));').click()  # 滑动页面，并找到添加成员按钮
        self.driver.find_element(MobileBy.ID, 'com.tencent.wework:id/imz').click()  # 点击手动输入添加
        self.driver.find_element(MobileBy.XPATH, "//*[@resource-id='com.tencent.wework:id/ern']/*/*[3]").send_keys(
            'Test01')  # 输入姓名
        self.driver.find_element(MobileBy.XPATH, "//*[@resource-id='com.tencent.wework:id/d9j']/*[2]").click()  # 点击性别按钮
        a = self.driver.find_element(MobileBy.XPATH,
                                     "//*[@resource-id='com.tencent.wework:id/boh']/*[2]/*/*")  # 获取性别女的节点
        a.click()  # 点击性别女
        self.driver.find_element(MobileBy.XPATH, "//*[@resource-id='com.tencent.wework:id/er1']/*/*[2]").send_keys(
            '1@qq.com')  # 输入邮箱
        self.driver.find_element(MobileBy.XPATH,
                                 "//*[@resource-id='com.tencent.wework:id/jr']/*[2]").click()  # 点击地址框，弹出地址页面
        self.driver.find_element(MobileBy.XPATH, "//*[@resource-id='com.tencent.wework:id/js']").send_keys(
            '外交部')  # 输入地址
        self.driver.find_element(MobileBy.XPATH, "//*[contains(@text,'中华人民共和国外交部')]").click()  # 选择地址
        self.driver.find_element(MobileBy.ID, 'com.tencent.wework:id/ie7').click()  # 点击确定按钮
        self.driver.find_element(MobileBy.XPATH,
                                 "//*[@resource-id='com.tencent.wework:id/bck']/*/*[7]/*[last()]").click()  # 点击设置部门按钮

        '''注意：
        前者获取的是集合列表，所以需要用(XPath)将XPath路径包起来表示集合，然后在用[n]来获取某一个元素，后者获取的是子节点可以直接用[n]来获取某一节点
        (//*[@resource-id='com.tencent.wework:id/e8s']/*)[1]" 和 //*[@resource-id='com.tencent.wework:id/bcz']/*[1] 的区别
        '''

        self.driver.find_element(MobileBy.XPATH,
                                 "(//*[@resource-id='com.tencent.wework:id/e8s']/*)[1]")  # 获取第一个部门,不进行任何操作
        self.driver.find_element(MobileBy.ID, 'com.tencent.wework:id/gzz').click()  # 点击确定按钮

        self.driver.find_element(MobileBy.ID, 'com.tencent.wework:id/ie7').click()  # 点击保存按钮
        toast = self.driver.find_element(MobileBy.XPATH, '//*[@class="android.widget.Toast"]').text()  # 获取保存成功提示信息


if __name__ == '__main__':
    pytest.main(['App.py', '-vs'])
