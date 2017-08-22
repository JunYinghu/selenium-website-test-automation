import time
from time import sleep
import unittest
from selenium import webdriver
import ConfigParser
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import sys
from selenium.webdriver.support.ui import Select
import random

class SimpleTestWebBrowser(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.config = ConfigParser.RawConfigParser(allow_no_value=True)
        cls.config.read('config1.txt')
        cls.driver = webdriver.Firefox()
        sid = ''
        with open('sid.txt', 'r') as outfile:
            sid = outfile.read()
        cls.driver.get("https://www.ranorex.com/forum/index.php?sid=" + sid)
        try:
            WebDriverWait(cls.driver, 3).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.icon-ucp > a:nth-child(1)')))
            print ("you may update your profile!")

        except TimeoutException:
            print("Due to loading timeout expired or could not find the element,Close browser,script stops running ")
            cls.driver.quit()
            sys.exit()

    @classmethod

    def tearDownClass(cls):
        time.sleep(8)
        cls.driver.quit()

    def test_00_open_usercontrolpanel(self):
        elem = self.driver.find_element_by_css_selector(self.config.get('Forum', 'location_forum_css_btn_useruontropuanel'))
        elem.click()
        elem = self.driver.find_element_by_css_selector(self.config.get('Forum', 'location_forum_css_btn_boardpreferences'))
        elem.click()

        print ("user is in User Control Panel > Board Preferences")
    def test_01_open_user_board_preferences(self):
        user_email = self.driver.find_element_by_id(self.config.get('Board', 'location_board_video_id_user_email_n'))
        #email_option = user_email.getText
        #user_email.getAttribute("for")
        #print (email_option)
        user_email.click()
        admin_email = self.driver.find_element_by_id(self.config.get('Board', 'location_board_video_id_admin_email_n')).click()

        language_select = Select(self.driver.find_element_by_id(self.config.get('Board', 'location_board_drop_id_language')))
        language_select.select_by_index(0)
        time_zone = Select(self.driver.find_element_by_id(self.config.get('Board', 'location_board_drop_id_timezone')))
        i = [0,1,2,3,4,5]
        time_zone.select_by_index(random.choice(i))


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(SimpleTestWebBrowser)
    suite.sortTestMethodsUsing=None
    unittest.TextTestRunner(verbosity=2).run(suite)

