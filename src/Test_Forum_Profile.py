import ConfigParser
import sys
import time
import unittest

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from utiliDoc.EditPost import EditPost
from utiliDoc.dropDownList import dropDownList

with open('resource/sid.txt', 'r') as outfile:
    sid = outfile.read()


class SimpleTestWebBrowser(unittest.TestCase):
    @classmethod
    def setUpClass(cls):

        cls.config = ConfigParser.RawConfigParser(allow_no_value=True)
        cls.config.read('resource/config.txt')
        cls.driver = webdriver.Firefox()
        cls.editpost = EditPost(cls.driver, cls.config)
        cls.editpost.driver.get("https://www.ranorex.com/forum/index.php?sid=" + sid)
        # cls.driver.get("https://www.ranorex.com/forum/index.php?sid=" + sid)
        cls.editGolableSetting = dropDownList(cls.driver, cls.config)
        try:
            WebDriverWait(cls.driver, 3).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, '.icon-ucp > a:nth-child(1)')))
            print ("you may update your profile!")
        except TimeoutException:
            print("Due to loading timeout expired or could not find the element,Close browser,script stops running ")
            cls.driver.quit()
            sys.exit()

    @classmethod
    def tearDownClass(cls):
        time.sleep(10)
        cls.driver.quit()

    def test_00_open_user_control_panel(self):
        control_panel = self.driver.find_element_by_css_selector(
            self.config.get('Forum', 'location_forum_css_btn_useruontropuanel'))
        control_panel.click()
        board_preferences = self.driver.find_element_by_css_selector(
            self.config.get('Forum', 'location_forum_css_btn_boardpreferences'))
        board_preferences.click()

    # perform fun dropdownloopselect
    def test_01_edit_global_settings(self):
        self.editGolableSetting.dropdownloopselect()

    def test_02_edit_posting(self):
        self.driver.get("https://www.ranorex.com/forum/index.php?sid=" + sid)
        time.sleep(8)
        edit_post = self.driver.find_element_by_xpath(self.config.get('editpost', 'edit_post_link_text'))
        edit_post.click()
        self.editpost.update()
        submit_edit_post = self.driver.find_element_by_name(self.config.get('editpost', 'location_submit'))
        submit_edit_post.click()


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(SimpleTestWebBrowser)
    suite.sortTestMethodsUsing = None
    unittest.TextTestRunner(verbosity=2).run(suite)
