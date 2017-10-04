import ConfigParser
import sys
import time
import unittest

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait

from utiliDoc.EditPost import EditPost


class SimpleTestWebBrowser(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with open('resource/sid.txt', 'r') as outfile:
            sid = outfile.read()
        cls.config = ConfigParser.RawConfigParser(allow_no_value=True)
        cls.config.read('resource/config.txt')
        cls.driver = webdriver.Firefox()

        cls.editpost = EditPost(cls.driver, cls.config)
        cls.editpost.driver.get("https://www.ranorex.com/forum/index.php?sid=" + sid)
        # cls.driver.get("https://www.ranorex.com/forum/index.php?sid=" + sid)

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
        # control_panel = self.driver.find_element_by_css_selector(".icon-ucp > a:nth-child(1)")

        control_panel.click()
        board_preferences = self.driver.find_element_by_css_selector(
            self.config.get('Forum', 'location_forum_css_btn_boardpreferences'))
        board_preferences.click()
        # print "user is in User Control Panel > Board Preferences"

    def test_01_edit_global_settings(self):
        time.sleep(10)
        section = 'Board'
        radio_select_n = "location_board_video_id_user_email_n"
        radio_select_y = "location_board_video_id_user_email_y"
        self.editpost.selectradio(section, radio_select_n, radio_select_y)
        radio_select_n = "location_board_video_id_admin_email_n"
        radio_select_y = "location_board_video_id_admin_email_y"
        self.editpost.selectradio(section, radio_select_n, radio_select_y)
        radio_select_n = 'location_board_video_id_private_msg_n'
        radio_select_y = 'location_board_video_id_private_msg_y'
        self.editpost.selectradio(section, radio_select_n, radio_select_y)
        radio_select_n = 'location_board_video_id_hide_online_n'
        radio_select_y = 'location_board_video_id_hide_online_y'
        self.editpost.selectradio(section, radio_select_n, radio_select_y)
        radio_select_n = 'location_board_video_id_notify_msg_n'
        radio_select_y = 'location_board_video_id_notify_msg_y'
        self.editpost.selectradio(section, radio_select_n, radio_select_y)
        radio_select_n = 'location_board_video_id_pop_win_n'
        radio_select_y = 'location_board_video_id_pop_win_y'
        self.editpost.selectradio(section, radio_select_n, radio_select_y)

        # Get drop down list options and output into a csv file
        time_zone_option = self.driver.find_element_by_id(self.config.get('Board', 'location_board_drop_id_timezone'))
        time_zone_options_list = time_zone_option.find_elements_by_tag_name('option')
        with open('resource/Time_zone_option.csv', 'w') as fout:
            fout.write('"","","","Index","Options_list"\n')
            for i, x in enumerate(time_zone_options_list):
                fout.write('"","","","{}","{}"\n'.format(i, x.get_attribute("innerHTML")))
                # print " element #{} has text {} ".format(i, x.get_attribute("innerHTML"))

        # get drop down list count
        # option_count = len(time_zone_option.find_elements_by_tag_name('option'))
        # print "=== option_count = {}".format(option_count)

        time_zone = Select(self.driver.find_element_by_id(self.config.get('Board', 'location_board_drop_id_timezone')))
        # time_zone_select = self.driver.find_element_by_id(self.config.get('Board', 'location_board_drop_id_timezone'))
        # time_zone_count = len(time_zone_select.find_elements_by_tag_name('option'))

        # time_zone_rang = [0, time_zone_count - 1]
        # i = random.choice(time_zone_rang)
        # print i
        time_zone.select_by_index(20)

        radio_select_y = 'location_board_video_id_sum_time_y'
        radio_select_n = 'location_board_video_id_sum_time_n'
        self.editpost.selectradio(section, radio_select_n, radio_select_y)
        submit = self.driver.find_element_by_name(self.config.get('Board', 'location_board_btn_name_submit'))
        submit.click()

    def test_02_edit_posting(self):
        time.sleep(10)
        edit_post = self.driver.find_element_by_xpath(self.config.get('editpost', 'edit_post_link_text'))
        edit_post.click()
        self.editpost.update()
        submit_edit_post = self.driver.find_element_by_name(self.config.get('editpost', 'location_submit'))
        submit_edit_post.click()


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(SimpleTestWebBrowser)
    suite.sortTestMethodsUsing = None
    unittest.TextTestRunner(verbosity=2).run(suite)
