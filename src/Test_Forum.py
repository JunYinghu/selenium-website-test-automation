import time
from time import sleep

import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

SLEEPY_TIME = 1


class SimpleTestWebBrowser(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
    @classmethod

    # Exit from Forum once script was run finished.
    def tearDownClass(cls):
        cls.driver.quit()

    def test_00_Open_Google_Search_Webpage(self):
        elem = self.driver.get("https://www.google.com.sg/?gfe_rd=cr&ei=XxeIWZSrOs2nvwStsIrICA&gws_rd=ssl")
        elem = self.driver.find_element_by_id("gs_htif0")
        #elem.clear()
        search_key="ranorex"
        elem.send_keys(search_key)
        elem = self.driver.find_element_by_name("btnK")
        elem.click()
        #elem.send_keys(Keys.RETURN)
        self.driver.find_element_by_css_selector('div._NId:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > h3:nth-child(1) > a:nth-child(1)').click()
        # tabUrl="http://www.google.com/?#q=";
        # term = raw_input("enter search query:");
        # webbrowser.open(tabUrl + term, new=new);

    #open Forum while the page was load properly
    def test_01_Open_Forum_Webpage(self):
        elem = self.driver.find_element_by_css_selector('#language-nav > ul:nth-child(1) > li:nth-child(4) > a:nth-child(1)').click()

    def test_02_Login_Forum(self):
        # Go to Login Page
        elem = self.driver.find_element_by_css_selector(".icon-logout > a:nth-child(1)").click()
        # Enter user name / pass word from your command window so that everyone can use own username / password to login.
        user_name = raw_input("enter_user_name:");
        pass_word = raw_input("enter_password:");
        elem_user = self.driver.find_element_by_id("username")
        elem_user.send_keys(user_name)
        elem_pass = self.driver.find_element_by_id("password")
        elem_pass.send_keys(pass_word)
        # Click on Login
        Login_button = self.driver.find_element_by_name("login")
        Login_button.click();

    #get current all opening windows    #def test_01_get_opening_window(self):
        #links = linkGrabber.Links('http://google.com')
        #gb=links.find(limit=8,duplicates=False,pretty=True)
        #print(gb)

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(SimpleTestWebBrowser)
    suite.sortTestMethodsUsing=None
    unittest.TextTestRunner(verbosity=2).run(suite)
