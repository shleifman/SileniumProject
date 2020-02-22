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
        # self.driver.find_element_by_css_selector("search-input-button")
        # self.driver.findElement(By.className("pure-button")).click()
        #self.driver.findElement(By.cssSelector("button[class=pure-button]")).click()
        #self.driver.findElement(By.cssSelector("button[class*='svg-search-icon']"))
        self.driver.find_element_by_xpath('//button[text()="submit"]').click()

    def tearDown(self):
        time.sleep(5)
        self.driver.quit()
