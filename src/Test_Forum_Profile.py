import ConfigParser
import random
import sys
import time
import unittest

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait

from CheckRadio import CheckRadio
from EditPost import EditPost


class SimpleTestWebBrowser(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.config = ConfigParser.RawConfigParser(allow_no_value=True)
        cls.config.read('config.txt')
        cls.driver = webdriver.Firefox()
        # sid = ''
        with open('sid.txt', 'r') as outfile:
            sid = outfile.read()
        # cls.driver.get("https://www.ranorex.com/forum/index.php?sid=" + sid)

        cls.checkradio = CheckRadio(cls.driver, cls.config)
        cls.editpost = EditPost(cls.driver, cls.config)
        cls.checkradio.driver.get("https://www.ranorex.com/forum/index.php?sid=" + sid)
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
        time.sleep(8)
        # cls.driver.quit()

    def test_00_open_user_control_panel(self):
        elem = self.driver.find_element_by_css_selector(
            self.config.get('Forum', 'location_forum_css_btn_useruontropuanel'))
        elem.click()
        elem = self.driver.find_element_by_css_selector(
            self.config.get('Forum', 'location_forum_css_btn_boardpreferences'))
        elem.click()
        print "user is in User Control Panel > Board Preferences"

    def test_01_edit_global_settings(self):
        section = 'Board'
        radio_select_n = "location_board_video_id_user_email_n"
        radio_select_y = "location_board_video_id_user_email_y"
        self.checkradio.validradio(section, radio_select_n, radio_select_y)
        radio_select_n = "location_board_video_id_admin_email_n"
        radio_select_y = "location_board_video_id_admin_email_y"
        self.checkradio.validradio(section, radio_select_n, radio_select_y)
        radio_select_n = 'location_board_video_id_private_msg_n'
        radio_select_y = 'location_board_video_id_private_msg_y'
        self.checkradio.validradio(section, radio_select_n, radio_select_y)
        radio_select_n = 'location_board_video_id_hide_online_n'
        radio_select_y = 'location_board_video_id_hide_online_y'
        self.checkradio.validradio(section, radio_select_n, radio_select_y)
        radio_select_n = 'location_board_video_id_notify_msg_n'
        radio_select_y = 'location_board_video_id_notify_msg_y'
        self.checkradio.validradio(section, radio_select_n, radio_select_y)
        radio_select_n = 'location_board_video_id_pop_win_n'
        radio_select_y = 'location_board_video_id_pop_win_y'
        self.checkradio.validradio(section, radio_select_n, radio_select_y)

        # Get drop down list options and output into a csv file
        timezoneoptions = self.driver.find_element_by_id(self.config.get('Board', 'location_board_drop_id_timezone'))
        elements = timezoneoptions.find_elements_by_tag_name('option')
        with open('Timezoneoption.csv', 'w') as fout:
            fout.write('"","","","index","text"\n')
            for i, x in enumerate(elements):
                fout.write('"","","","{}","{}"\n'.format(i, x.get_attribute("innerHTML")))
                print " element #{} has text {} ".format(i, x.get_attribute("innerHTML"))

        # get drop down list count
        option_count = len(timezoneoptions.find_elements_by_tag_name('option'))
        print "=== option_count = {}".format(option_count)
        # timezoneoptions.select_by_index(0)

        time_zone = Select(self.driver.find_element_by_id(self.config.get('Board', 'location_board_drop_id_timezone')))
        time_zone_select = self.driver.find_element_by_id(self.config.get('Board', 'location_board_drop_id_timezone'))
        time_zone_count = len(time_zone_select.find_elements_by_tag_name('option'))

        time_zone_rang = [0, time_zone_count - 1]
        i = random.choice(time_zone_rang)
        print i
        time_zone.select_by_index(i)

        radio_select_y = 'location_board_video_id_sum_time_y'
        radio_select_n = 'location_board_video_id_sum_time_n'
        self.checkradio.validradio(section, radio_select_n, radio_select_y)
        submit = self.driver.find_element_by_name(self.config.get('Board', 'location_board_btn_name_submit'))
        submit.click()

    def test_02_edit_posting(self):
        time.sleep(10)
        editpost = self.driver.find_element_by_xpath(self.config.get('editpost', 'edit_post_link_text'))
        editpost.click()
        self.editpost.update()
        submiteditpost = self.driver.find_element_by_name(self.config.get('editpost', 'location_submit'))
        submiteditpost.click()


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(SimpleTestWebBrowser)
    suite.sortTestMethodsUsing = None
    unittest.TextTestRunner(verbosity=2).run(suite)
