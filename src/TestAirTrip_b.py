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


class Air_Trip_booking(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.config = ConfigParser.RawConfigParser(allow_no_value=True)
        cls.config.read("airtripconfig.txt")
        cls.driver = webdriver.Firefox()
        cls.driver.get("http://junying.marsair.tw/")
        cls.driver.implicitly_wait(10)

    @classmethod
    # def teardown(cls):
    #     time.sleep(8)
    #     cls.driver.quit()

    # This is a function / method

    def get_path(self, session_name, find_element):
        Get_element = self.config.get(session_name, find_element)
        Get_element_local = self.driver.find_element_by_xpath(Get_element)
        return (Get_element_local)

    def get_search_result(self):
        session_name = "Booking"
        find_element_text = "Search_button_xpath"
        Search_button = self.get_path(session_name, find_element_text).click()

        find_element_text = "Search_result_text_xpath"
        session_name = "SearchResult"
        get_search_result = self.get_path(session_name, find_element_text)
        get_search_result_text = get_search_result.get_attribute("innerHTML")

        Validation_Text = "Seats available!"
        decoded = self.driver.page_source.encode('ascii', 'ignore')
        decoded = self.driver.page_source.encode('utf8', )

        if Validation_Text in decoded:
            find_element_text = "Search_result_text_xpath2"
            session_name = "SearchResult2"""
            get_search_result = self.get_path(session_name, find_element_text)
            get_search_result_text2 = get_search_result.get_attribute("innerHTML")
            find_element_button = "Go_back_button_xpath2"
            go_back_button2 = self.get_path(session_name, find_element_button)
            print(get_search_result_text + get_search_result_text2)
            go_back_button2.click()
        else:
            find_element_button = "Go_back_button_xpath"
            go_back_button = self.get_path(session_name, find_element_button)
            print (get_search_result_text)
            go_back_button.click()

    def select_depature_return(self, d="none", r="none", prom_cod="none"):
        find_element_text = "Departure_option_xpath"
        session_name = "Booking"
        Departure_date_selected = Select(self.get_path(session_name, find_element_text))
        Departure_date = self.get_path(session_name, find_element_text)
        # Departure_date_options = Departure_date.find_elements_by_tag_name("option")
        Departure_date_options_len = len(Departure_date.find_elements_by_tag_name("option"))
        find_element_text = "Return_option_xpath"
        Return_date_selected = Select(self.get_path(session_name, find_element_text))
        Return_date = self.get_path(session_name, find_element_text)
        # Return_date_options = Return_date.find_elements_by_tag_name("option")
        find_element_text = "Promotional_code_xpath"
        input_prom_code = self.get_path(session_name, find_element_text)
        input_prom_code.clear()

        if d <> "none" and r <> "none":
            if prom_cod <> "none":
                Departure_date_selected.select_by_index(d)
                Return_date_selected.select_by_index(r)
                input_prom_code.send_keys(prom_cod)
                selected_d = 'This is your selected departure:  '
                selected_d_t = Departure_date_selected.first_selected_option.text
                print selected_d, d, selected_d_t
                selected_r = 'This is your selected return:  '
                selected_r_t = Return_date_selected.first_selected_option.text
                print selected_r, r, selected_r_t
                prom_r = 'This is your entered promotional code:  '
                prom_r_t = prom_cod
                print prom_r, prom_r_t
                self.get_search_result()


            else:
                Departure_date_selected.select_by_index(d)
                Return_date_selected.select_by_index(r)
                selected_d = 'This is your selected Departure:  '
                selected_d_t = Departure_date_selected.first_selected_option.text
                print selected_d, d, selected_d_t
                selected_r = 'This is your selected Return:  '
                selected_r_t = Return_date_selected.first_selected_option.text
                print selected_r, r, selected_r_t
                self.get_search_result()

        #print ("invalid selection you provided")
        #self.driver.quit()

        return (Departure_date_options_len)

    def prom_cod (self):
        prom_cod_arr = []
        letter = random (letters)




    def execute_search(self):
        options_len = self.select_depature_return()
        #print options_len
        d = 0
        r = 0
        sum = 0

        while d < options_len:

            while r < options_len:
                prom_cod = "AF3-FJK-418"
                self.select_depature_return(d, r, prom_cod)
                r = r + 1
                sum = sum + 1
                prom_cod = "none"
            r = 0
            d = d + 1
        print sum

    def test_00_booking_trip_normal(self):
        self.execute_search()

    def test_01_booking_trip_promotional(self):
        # self.execute_search()
        pass


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(Air_Trip_booking)
    suite.sortTestMethodsUsing = None
    unittest.TextTestRunner(verbosity=2).run(suite)
