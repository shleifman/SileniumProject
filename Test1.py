import unittest
import time
from selenium import webdriver


class Test1(unittest.TestCase):
    def test_first_selenium_test(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://www.walla.co.il/")
        time.sleep(22)
        self.driver.quit()
