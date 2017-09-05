from sys import argv, exit
from time import sleep
import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import ConfigParser
import sys


class SimpleTestWebBrowser(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.config = ConfigParser.RawConfigParser(allow_no_value=True)
        cls.config.read('config1.txt')
        cls.driver = webdriver.Firefox()
        cls.driver.get("https://www.google.com.sg")
        try:
            WebDriverWait(cls.driver, 3).until(EC.presence_of_element_located((By.NAME, 'btnK')))
            print ("google search is ready!")

        except TimeoutException:
            print("Due to loading timeout expired or could not find the element,Close browser,script stops running ")
            cls.driver.quit()
            sys.exit()

    @classmethod
    # Exit from Forum once script was run finished.
    def tearDownClass(cls):
        time.sleep(8)
        cls.driver.quit()

    # key in search keyword and open the websit
    def test_00_Open_Google_Search_Webpage(self):
        Validation_text_1 = "Server not found"
        Validation_text_2 = "Ranorex: Test Automation for GUI Testing"
        elem = self.driver.find_element_by_id("gs_htif0")
        # provide valid keyword 'ranorex'
        search_key = raw_input("Enter your search keyword (ranorex):")
        elem.send_keys(search_key)
        elem = self.driver.find_element_by_name("btnK")
        elem.click()
        time.sleep(2)
        # self.assertEqual(elem.text, "Ranorex: Test Automation for GUI Testing", "failed")
        # sys.exit()
        # decoded = self.driver.page_source.encode('ascii', 'ignore')
        decoded = self.driver.page_source.encode('utf8', )
        # if below either 1 or 2 conditions are meeting, then script is stopped.
        if Validation_text_2 not in decoded:
            validation = 2
            # print(validation)
        else:
            # print ("path2")
            validation = 1
        while (validation > 1):
            self.driver.back()
            print("Expected website are not found")
            search_key = raw_input("Re-enter your search keyword (ranorex):")
            elem = self.driver.find_element_by_id("gs_htif0")
            elem.send_keys(search_key)
            elem = self.driver.find_element_by_name("btnK")
            elem.click()
            time.sleep(2)
            decoded = self.driver.page_source.encode('utf8', )
            print(decoded)
            if Validation_text_2 not in decoded:
                validation = 2
                # print("validation1")
                # print(validation)
            else:
                # print ("path2")
                validation = 1
                # print("validation2")
                # print(validation)

        print("Launch websit:" + Validation_text_2)
        self.driver.find_element_by_css_selector(
            'div._NId:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > h3:nth-child(1) > a:nth-child(1)').click()
        # print("validation2")
        # print(validation)

    # open Forum while the page was load properly
    def test_01_Open_Forum_Webpage(self):
        try:
            WebDriverWait(self.driver, 3).until(EC.presence_of_element_located(
                (By.CSS_SELECTOR, '#language-nav > ul:nth-child(1) > li:nth-child(4) > a:nth-child(1)')))
            Page_url = self.driver.current_url
            print ("Pass: validation  You are in " + Page_url + " Ready: Launch Login page")
            elem = self.driver.find_element_by_css_selector(
                '#language-nav > ul:nth-child(1) > li:nth-child(4) > a:nth-child(1)').click()
        except TimeoutException:
            print("Due to loading timeout expired or could not find the element,Close browser,script stops running ")
            cls.driver.quit()
            sys.exit()

    # login in Forum with username / password validation
    def test_02_Login_Forum(self):
        # Go to Login Page
        elem = self.driver.find_element_by_css_selector(".icon-logout > a:nth-child(1)").click()
        # Enter user name / pass word before the script is running so that everyone can use own username / password to login.
        user_name = argv[1]
        pass_word = argv[2]
        Validation_wrong_password = "You have specified an incorrect password"
        Validation_wrong_username = "You have specified an incorrect username"
        Validation_wrong_max = "You exceeded the maximum allowed number of login attempts."
        Validation_wrong_confirmation_code = "The confirmation code you entered was incorrect"
        Validation_long_successfully = "You have been successfully logged in."

        elem_user = self.driver.find_element_by_id("username")
        elem_user.send_keys(user_name)
        elem_pass = self.driver.find_element_by_id("password")
        elem_pass.send_keys(pass_word)
        # Click on Login
        Login_button = self.driver.find_element_by_name("login")
        Login_button.click();

        decoded = self.driver.page_source.encode('utf8', )
        elem = self.driver.find_element_by_css_selector(".icon-logout > a:nth-child(1)")

        if Validation_wrong_username in decoded:
            loginvalidation = 1
            print (loginvalidation)
        elif Validation_wrong_password in decoded:
            loginvalidation = 2
            print (loginvalidation)
        elif Validation_wrong_max in decoded:
            loginvalidation = 3
            print (loginvalidation)
        else:
            self.assertEqual(elem.text, "Logout [ jun ]", "failed")
            print("Pass validation " + elem.text + " login successfully")
            loginvalidation = 0
            print (loginvalidation)

            sid = ''
            while True:
                kv = self.extract_param()
                if 'sid' in kv:
                    sid = kv['sid']
                    break
                else:
                    time.sleep(1)

            with open('sid.txt', 'w') as outfile:
                outfile.write(sid)
                #
                # outfile = open('sid.txt', 'w')
                # outfile.write(sid)
                # outfile.close()

        while (loginvalidation > 0):
            elem_user = self.driver.find_element_by_id("username")
            elem_user.send_keys(user_name)
            elem_pass = self.driver.find_element_by_id("password")
            elem_pass.send_keys(pass_word)
            # print (pass_word)
            # Click on Login
            Login_button = self.driver.find_element_by_name("login")
            Login_button.click()
            decoded = self.driver.page_source.encode('utf8', )
            elem = self.driver.find_element_by_css_selector(".icon-logout > a:nth-child(1)")
            if Validation_wrong_username in decoded:
                loginvalidation = 1
                print("error:" + Validation_wrong_username)
                user_name = raw_input("enter user_name (jun):")
            elif Validation_wrong_password in decoded:
                loginvalidation = 2
                print("error:" + Validation_wrong_password)
                pass_word = raw_input("enter pass_word (hjyhappy):")
            elif Validation_wrong_max in decoded:
                loginvalidation = 3
                print("error:" + Validation_wrong_max)
                user_name = raw_input("enter user_name (jun):")
                pass_word = raw_input("enter pass_word (hjyhappy):")
                confirm_code = raw_input("confirm_code:")
                elem_user = self.driver.find_element_by_id("confirm_code")
                elem_user.send_keys(confirm_code)

            elif Validation_wrong_confirmation_code in decoded:
                loginvalidation = 4
                print("error:" + Validation_wrong_confirmation_code)
                user_name = raw_input("enter user_name (jun):")
                pass_word = raw_input("enter pass_word (hjyhappy):")
                confirm_code = raw_input("confirm_code:")
                elem_user = self.driver.find_element_by_id("confirm_code")
                elem_user.send_keys(confirm_code)
            else:
                Validation_long_successfully in decoded
                print("Pass:" + Validation_long_successfully)
                loginvalidation = 0

        # print(loginvalidation)
        # print("in laststep")
        elem = self.driver.find_element_by_css_selector(self.config.get('Login', 'location_css_btn_logout'))
        self.assertEqual(elem.text, "Logout [ jun ]", "failed")
        print("Pass validation " + elem.text + " login successfully")
        # value = self.config.get('Login', 'UserControlPanel')
        # print value

    def extract_param(self):
        kv = {}
        (_, param) = self.driver.current_url.split('?')
        for entry in param.split('&'):
            (k, v) = entry.split('=')
            kv[k] = v
        return kv


if __name__ == '__main__':
    if len(argv) < 3:
        print "please supply username and password"
        exit(1)
    suite = unittest.TestLoader().loadTestsFromTestCase(SimpleTestWebBrowser)
    suite.sortTestMethodsUsing = None
    unittest.TextTestRunner(verbosity=2).run(suite)
