import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class FirstTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def test_1(self):
        self.driver.get("https://www.wikipedia.org")
        assert "Wikipedia" in self.driver.title
        self.driver.find_element_by_id("searchInput").send_keys("Python")
        time.sleep(1)
        self.driver.find_element_by_xpath('//a[2]/div/h3').click()

    def tearDown(self):
        time.sleep(5)
        self.driver.quit()
