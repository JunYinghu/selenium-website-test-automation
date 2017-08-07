import os
import sys
import time
from time import sleep

import glob
import unittest

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


# Returns abs path relative to this file and not cwd
#PATH = lambda p: os.path.abspath(
  #  os.path.join(os.path.dirname(__file__), p)
#)

SLEEPY_TIME = 1

class SimpleBrowserTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
    
    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        
    def test_00_open(self):
        self.driver.get("http://www.python.org")
        assert "Python" in driver.title
        elem = self.driver.find_element_by_name("q")
        elem.clear()
        elem.send_keys("pycon")
        elem.send_keys(Keys.RETURN)
        assert "No results found." not in driver.page_source
		
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(SimpleBrowserTests)
    suite.sortTestMethodsUsing=None
    unittest.TextTestRunner(verbosity=2).run(suite)
