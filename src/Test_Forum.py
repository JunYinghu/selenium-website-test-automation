import unittest
from sys import argv, exit

from selenium import webdriver

SLEEPY_TIME = 1
timeout = 3


class SimpleTestWebBrowser(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.get("https://www.google.com.sg")
        decoded = cls.driver.page_source.encode('utf8', )
        # try:
        #     element_present = EC.presence_of_element_located((By.ID, 'gs_htif0'))
        #     WebDriverWait(driver, timeout).until(element_present)
        # except TimeoutException:
        #     print ("Timed out waiting for page to load")

    @classmethod
    # Exit from Forum once script was run finished.
    # def tearDownClass(cls):
    # cls.driver.quit()

    # key in search keyword and open the websit
    def test_00_Open_Google_Search_Webpage(self):
        elem = self.driver.find_element_by_id("gs_htif0")
        # elem.clear()
        search_key = "ranorex"
        elem.send_keys(search_key)
        elem = self.driver.find_element_by_name("btnK")
        elem.click()
        # self.assertEqual(elem.text, "Ranorex: Test Automation for GUI Testing", "failed")
        # self.driver.quit()
        # decoded = self.driver.page_source.encode('ascii', 'ignore')
        decoded = self.driver.page_source.encode('utf8', )

        # if below either 1 or 2 conditions are meeting, then script is stopped.
        Validation_text_1 = "Server not found"
        Validation_text_2 = "Ranorex: Test Automation for GUI Testing"

        if Validation_text_1 in decoded:
            print("error:" + Validation_text_1)
            self.driver.quit()

        elif Validation_text_2 not in decoded:
            print("error:" + Validation_text_2 + "not found in search result list")
            self.driver.quit()

        # assert "Ranorex: Test Automation for GUI Testing" not in self.driver.page_source
        # self.driver.quit()
        # elem.send_keys(Keys.RETURN
        print("Launch websit:" + Validation_text_2)
        self.driver.find_element_by_css_selector(
            'div._NId:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > h3:nth-child(1) > a:nth-child(1)').click()

        # tabUrl="http://www.google.com/?#q=";
        # term = raw_input("enter search query:");
        # webbrowser.open(tabUrl + term, new=new);

    # open Forum while the page was load properly
    def test_01_Open_Forum_Webpage(self):
        elem = self.driver.find_element_by_css_selector(
            '#language-nav > ul:nth-child(1) > li:nth-child(4) > a:nth-child(1)').click()

    # login in Forum with username / password validation
    def test_02_Login_Forum(self):
        # Go to Login Page
        elem = self.driver.find_element_by_css_selector(".icon-logout > a:nth-child(1)").click()
        # Enter user name / pass word before the script is running so that everyone can use own username / password to login.
        user_name = argv[1]
        pass_word = argv[2]
        # Enter user name / pass word from your command window so that everyone can use own username / password to login.
        # user_name = raw_input("enter user_name:");
        # pass_word = raw_input("enter pass_word:");

        elem_user = self.driver.find_element_by_id("username")
        elem_user.send_keys(user_name)
        elem_pass = self.driver.find_element_by_id("password")
        elem_pass.send_keys(pass_word)
        # Click on Login
        Login_button = self.driver.find_element_by_name("login")
        Login_button.click();

        decoded = self.driver.page_source.encode('utf8', )
        Validation_wrong_password = "You have specified an incorrect password"
        Validation_wrong_username = "You have specified an incorrect username"
        Validation_wrong_max = "You exceeded the maximum allowed number of login attempts."
        if Validation_wrong_username in decoded:
            print("error:" + Validation_wrong_username)
            user_name = raw_input("enter user_name:");
            elem_user = self.driver.find_element_by_id("username")
            elem_user.send_keys(user_name)
            elem_pass = self.driver.find_element_by_id("password")
            elem_pass.send_keys(pass_word)
            print (pass_word)
            # Click on Login
            Login_button = self.driver.find_element_by_name("login")
            Login_button.click();

        elif Validation_wrong_password in decoded:
            print("error:" + Validation_wrong_password);
            elem_user = self.driver.find_element_by_id("username")
            elem_user.send_keys(user_name)
            pass_word = raw_input("enter pass_word:");
            elem_pass = self.driver.find_element_by_id("password")
            elem_pass.send_keys(pass_word)
            Login_button = self.driver.find_element_by_name("login")
            Login_button.click();

        elif Validation_wrong_max in decoded:
            print("error:" + Validation_wrong_max);
            self.driver.quit()

        else:
            elem = self.driver.find_element_by_css_selector(".icon-logout > a:nth-child(1)")
            self.assertEqual(elem.text, "Logout [ jun ]", "failed")
            print("Pass validation " + elem.text + " login successfully")
            session_id = self.driver.session_id
            print (session_id)

            # get current all opening windows    #def test_01_get_opening_window(self):
            # links = linkGrabber.Links('http://google.com')
            # gb=links.find(limit=8,duplicates=False,pretty=True)
            # print(gb)


if __name__ == '__main__':
    if len(argv) < 3:
        print "please supply username and password"
        exit(1)
    suite = unittest.TestLoader().loadTestsFromTestCase(SimpleTestWebBrowser)
    suite.sortTestMethodsUsing = None
    unittest.TextTestRunner(verbosity=2).run(suite)
