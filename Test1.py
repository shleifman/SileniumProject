import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class FirstTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def test_1(self):
        self.driver.get("https://www.wikipedia.org")
        assert "Wikipedia" in self.driver.title
        searchBar = self.driver.find_element_by_id("searchInput")
        searchBar.send_keys("Python")
        searchButton = self.driver.find_element_by_class_name("sprite svg-search-icon")
        searchButton.click(self)

    def tearDown(self):
        time.sleep(5)
        self.driver.quit()
