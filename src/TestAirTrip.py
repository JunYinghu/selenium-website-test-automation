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
import string
from random import randint
import csv


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

        validation_text = "Seats available!"
        validation_prom_cod = "Sorry, code"
        validation_prom_cod = "Promotional code"
        decoded = self.driver.page_source.encode('ascii', 'ignore')
        decoded = self.driver.page_source.encode('utf8', )

        if validation_text in decoded and validation_prom_cod not in decoded:
            find_element_text = "Search_result_text_xpath2"
            session_name = "SearchResult2"
            get_search_result = self.get_path(session_name, find_element_text)
            get_search_result_text2 = get_search_result.get_attribute("innerHTML")
            find_element_button = "Go_back_button_xpath2"
            go_back_button2 = self.get_path(session_name, find_element_button)
            print(get_search_result_text + get_search_result_text2)
            go_back_button2.click()


        elif validation_prom_cod in decoded or validation_prom_cod in decoded:
            find_element_text = "Search_result_text_xpath3"
            session_name = "SearchResult3"
            get_search_result = self.get_path(session_name, find_element_text)
            get_search_result_text3 = get_search_result.get_attribute("innerHTML")
            find_element_button = "Go_back_button_xpath3"
            go_back_button3 = self.get_path(session_name, find_element_button)
            print(get_search_result_text + get_search_result_text3)
            go_back_button3.click()

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
                prom_cod
                print prom_r, prom_cod
                self.get_search_result()

                with open("test_result_air_book.csv", "w") as fillin:
                    fieldnames = ['Selected_Depature', 'Selected_Return',"Promotional"]
                    writer = csv.DictWriter(fillin, fieldnames=fieldnames)
                    writer.writeheader()
                    writer.writerow({"Selected_Depature": selected_d_t, "Selected_Return": selected_r_t, "Promotional":prom_cod})

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

        # print ("invalid selection you provided")
        # self.driver.quit()
        return (Departure_date_options_len)

    def prom_cod(self):
        prom_cod = ''
        prom_cod_arr = []
        letter_1 = random.choice(string.ascii_letters)
        prom_cod_arr.append(letter_1)
        letter_2 = random.choice(string.ascii_letters)
        prom_cod_arr.append(letter_2)
        prom_cod_arr.append("-")
        letter_3 = random.choice(string.ascii_letters)
        prom_cod_arr.append(letter_3)
        letter_4 = random.choice(string.ascii_letters)
        prom_cod_arr.append(letter_4)
        letter_5 = random.choice(string.ascii_letters)
        prom_cod_arr.append(letter_5)
        prom_cod_arr.append("-")
        digit_1 = randint(0, 9)
        digit_2 = randint(0, 9)
        digit_3 = randint(0, 9)
        # digit_1 = 7
        # digit_2 = 7
        # digit_3 = 7
        print ("this are digit :"), digit_1, digit_2, digit_3
        if digit_1 + digit_2 + digit_3 < 10:
            digit_4 = digit_1 + digit_2 + digit_3
            # print digit_4
        else:
            t = digit_1 + digit_2 + digit_3
            digit_4 = (abs(t) % (10 ** 1)) / (10 ** (1 - 1))
            # print ("______digit_4"), digit_4
        digit_1 = str(digit_1)
        prom_cod_arr.insert(2, digit_1)
        digit_2 = str(digit_2)
        prom_cod_arr.insert(10, digit_2)
        digit_3 = str(digit_3)
        prom_cod_arr.insert(11, digit_3)
        digit_4 = str(digit_4)
        prom_cod_arr.append(digit_4)
        # print ("this are digit :"), digit_1, digit_2, digit_3,digit_4
        pro_cod = ''.join(prom_cod_arr)
        # print ("This is final code:"), pro_cod
        return (pro_cod)

    def execute_search(self):
        options_len = self.select_depature_return()
        # print options_len
        d = 0
        r = 0
        sum = 0

        while d < options_len:

            while r < options_len:
                prom_cod = self.prom_cod()
                print prom_cod
                self.select_depature_return(d, r, prom_cod)
                r = r + 1
                sum = sum + 1
                prom_cod = " "
            r = 0
            d = d + 1
        print sum

    def test_00_booking_trip_normal(self):
        self.execute_search()
        # self.prom_cod()

    def test_01_booking_trip_promotional(self):
        # self.execute_search()
        pass


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(Air_Trip_booking)
    suite.sortTestMethodsUsing = None
    unittest.TextTestRunner(verbosity=2).run(suite)
