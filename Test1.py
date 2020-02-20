import unittest
import time
from selenium import webdriver


class FirstTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def test_1(self):
        self.driver.get("https://www.walla.co.il/")

    def test_2(self):
            self.driver.get("https://www.ynet.co.il/")

    def tearDown(self):
        time.sleep(10)
        self.driver.quit()
