import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestWorkWeiXinCookie:
    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def teardown_method(self):
        self.driver.quit()

    def test_workweixin_cookie(self):
        self.driver.get("https://work.weixin.qq.com/")
        with open("./cookie.json") as f:
            cookies = json.load(f)
            for cookie in cookies:
                self.driver.add_cookie(cookie)
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        time.sleep(2)
        self.driver.find_element(By.ID, "menu_customer").click()
        time.sleep(2)