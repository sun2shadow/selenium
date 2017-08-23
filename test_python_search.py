#!/usr/bin/env python
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
class PythonSearch(unittest.TestCase):
    def setUp(self):
        self.driver = webDriver.Chrome()
    def test_search(self):
        driver = self.driver
        driver.get('http://www.python.org')
        elem = driver.find_elemrnt_by_name('q')
        elem.send_keys('pychon')
        elem.send_keys(Keys.RETURN)
        assert "No result found." not in driver.page_source
    def tearDown(self):
        self.driver.close()
    if __name__ == "__main__":
        unittest.main()
