from appium.webdriver.common.mobileby import MobileBy


class Base_Page():

    def __init__(self, driver):
        self.driver = driver

    def find(self, By, locator):
        element = self.driver.find_element(By, locator)
        return element

    def find_click(self, By, locator):
        self.driver.find_element(By, locator).click()

    def find_send(self, By, locator, text):
        self.driver.find_element(By, locator).send_keys(text)

    def move_page_seach(self, text):
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                 'new UiScrollable(new UiSelector().'
                                 'scrollable(true).instance(0)).'
                                 'scrollIntoView(new UiSelector().'
                                 f'text("{text}").instance(0));').click()  # 滑动页面，并找到添加成员按钮
