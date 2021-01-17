from appium import webdriver


class test_setup_teardown():
    def setup_class(self):
        package = 'com.tencent.wework'
        activity = 'launch.WwMainActivity'
        des = {}
        des['platformName'] = 'Android'
        des['platformVersion'] = '6.0'
        des['deviceName'] = 'emulator-5554'
        des['appPackage'] = package
        des['appActivity'] = activity
        des['noReset'] = 'true'
        des['unicodeKeyBaord'] = 'true'
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', des)
        self.driver.implicitly_wait(10)

    def teardown_class(self):
        self.driver.quit()
