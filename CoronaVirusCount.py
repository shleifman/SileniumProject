import unittest
import time
from selenium import webdriver
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class FirstTest(unittest.TestCase):
    def setUp(self):
        path = 'C:/Users/shlei/PycharmProjects/SileniumProject/venv/'
        scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
        creds = ServiceAccountCredentials.from_json_keyfile_name(path + 'CoronaVirus.json', scope)
        self.client = gspread.authorize(creds)
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def test_1(self):
        self.driver.get("https://www.worldometers.info/coronavirus/")
        time.sleep(1)
        statistics = self.driver.find_elements_by_xpath('//*[@id="maincounter-wrap"]/div/span')
        print('Number of cases world wide: ' + statistics[0].text + '\n')
        print('Number of deaths world wide: ' + statistics[1].text + '\n')
        print('Number of recoveries world wide: ' + statistics[2].text + '\n')
        sheet = self.client.open('CoronaVirus').sheet1
        sheet.update_cell(2, 2, statistics[0].text)
        sheet.update_cell(2, 3, statistics[1].text)
        sheet.update_cell(2, 4, statistics[2].text)


    def tearDown(self):
        time.sleep(5)
        self.driver.quit()

