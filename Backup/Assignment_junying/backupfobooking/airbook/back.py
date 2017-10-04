import ConfigParser
import sys
import unittest

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait

from airbook.utils.date_cal import datecau
from airbook.utils.promo_gen_verify import promcodgent


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
    def get_path(self, session_name, find_element):
        get_element = self.config.get(session_name, find_element)
        get_element_local = self.driver.find_element_by_xpath(get_element)
        return (get_element_local)

    def get_search_result(self, diffdate, prom_cod="none"):
        session_name = "Booking"
        find_element_text = "Search_button_xpath"
        Search_button = self.get_path(session_name, find_element_text).click()
        try:
            WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/h2')))
            print ("you may start to verify result")
        except TimeoutException:
            print("Due to loading timeout expired or could not find the element,Close browser,script stops running ")
            self.driver.quit()
            sys.exit()

        if diffdate < 365:
            validation = "Unfortunately, this schedule is not possible. Please try again."
            if (validation in self.driver.page_source):
                flag = 1
                status = "failed"
                expectedresult = validation
                self.driver.back()

        elif diffdate > 365:
            if prom_cod <> "none":
                if prom_cod is invalidate:
                    validation = "Sorry, code [", prom_cod, "] is not valid"
                    flag = 4
                    status = "pass"
                    expectedresult = validation
                    self.driver.back()

                else:
                    validation = "Promotional code [", prom_cod, "] used: [", prom_cod, "]0% discount!"
                    flag = 4
                    status = "pass"
                    expectedresult = validation
                    self.driver.back()
            else:
                validation_1 = "Sorry, there are no more seats available."
                validation_2 = "Seats available! Call 0800 MARSAIR to book!"
                if (validation_1 in self.driver.page.source or validation_2 in self.driver.page.source):
                    flag = 2
                    status = "pass"
                    expectedresult = validation_1 + validation_2
                    self.driver.back()

                    # session_name = "SearchResult"
                    # find_element_text_1 = "Search_result_text_xpath"
                    # # find_result_text_1 = self.get_path(session_name, find_element_text_1)
                    # # get_result_text_1 = find_result_text_1.get_attribute("innerHTML")
                    #
                    # find_element_text_2 = "Search_result_text_xpath2"
                    # # find_result_text_2 = self.get_path(session_name, find_element_text_2)
                    # # get_result_text_2 = find_result_text_2.get_attribute("innerHTML")
                    #
                    # find_element_text_3 = "Search_result_text_xpath3"
                    # # find_result_text_3 = self.get_path(session_name, find_element_text_3)
                    # # get_result_text_3 = find_result_text_3.get_attribute("innerHTML")
                    #
                    # find_element_text_2= "Search_result_text_css_2"
                    #
                    # flag =1
                    #
                    # print "++++++++++++++++this is the way of result +++++++++++++", flag
                    #
                    # if flag == 1:
                    #     find_result_text_1 = self.get_path(session_name, find_element_text_1)
                    #     get_result_text_1 = find_result_text_1.get_attribute("innerHTML")
                    #     find_element_button = "Go_back_button_xpath"
                    #     go_back_button = self.get_path(session_name, find_element_button)
                    #     actualresult = get_result_text_1
                    #     print (actualresult)
                    #     go_back_button.click()
                    #
                    # if flag == 2:
                    #     find_result_text_2 = self.get_path(session_name, find_element_text_2)
                    #     get_result_text_2 = find_result_text_2.get_attribute("innerHTML")
                    #     find_element_button = "Go_back_button_xpath2"
                    #     go_back_button2 = self.get_path(session_name, find_element_button)
                    #     actualresult = get_result_text_2
                    #     print (actualresult)
                    #     go_back_button2.click()
                    # if flag == 3:
                    #     find_result_text_3 = self.get_path(session_name, find_element_text_3)
                    #     get_result_text_3 = find_result_text_3.get_attribute("innerHTML")
                    #     find_element_button = "Go_back_button_xpath3"
                    #     go_back_button3 = self.get_path(session_name, find_element_button)
                    #     actualresult = get_result_text_3
                    #     print (actualresult)
                    #     go_back_button2.click()


                    # find_element_button = "Go_back_button_xpath2"
                    #
                    # go_back_button2 = self.get_path(session_name, find_element_button)
                    # ActualResult = get_search_result_text + get_search_result_text2
                    # go_back_button2.click()
                    #
                    # # case 3
                    # find_element_text = "Search_result_text_xpath3"
                    # session_name = "SearchResult"
                    # get_search_result = self.get_path(session_name, find_element_text)
                    # get_search_result_text3 = get_search_result.get_attribute("innerHTML")
                    # find_element_button = "Go_back_button_xpath3"
                    # go_back_button3 = self.get_path(session_name, find_element_button)
                    # print(get_search_result_text + get_search_result_text3)
                    # go_back_button3.click()
                    #
                    # validation_text = "Seats available!"
                    # validation_prom_cod = "Sorry, code"
                    # validation_prom_cod = "Promotional code"
                    # decoded = self.driver.page_source.encode('utf8', )
                    #
                    # if validation_text in decoded and validation_prom_cod not in decoded:
                    #     find_element_text = "Search_result_text_xpath2"
                    #     session_name = "SearchResult"
                    #     get_search_result = self.get_path(session_name, find_element_text)
                    #     get_search_result_text2 = get_search_result.get_attribute("innerHTML")
                    #     find_element_button = "Go_back_button_xpath2"
                    #     go_back_button2 = self.get_path(session_name, find_element_button)
                    #     ActualResult = get_search_result_text + get_search_result_text2
                    #     go_back_button2.click()
                    #     # def writetocvs(status):
                    #     #     with open("testresult.csv", "w") as fillin
                    #     #         fieldnames = ['ActualResult', 'ExpectedResult', "Status"]
                    #     #         writer = csv.DictWriter(fillin, fieldnames=fieldnames)
                    #     #         writer.writeheader()
                    #     #         writer.writerow({"ActualResult": ActualResult, "ExpectedResult": selected_r_t, "Status": status}):Status
                    #
                    # elif validation_prom_cod in decoded or validation_prom_cod in decoded:
                    #     find_element_text = "Search_result_text_xpath3"
                    #     session_name = "SearchResult"
                    #     get_search_result = self.get_path(session_name, find_element_text)
                    #     get_search_result_text3 = get_search_result.get_attribute("innerHTML")
                    #     find_element_button = "Go_back_button_xpath3"
                    #     go_back_button3 = self.get_path(session_name, find_element_button)
                    #     print(get_search_result_text + get_search_result_text3)
                    #     go_back_button3.click()
                    #
                    # else:
                    #     find_element_button = "Go_back_button_xpath"
                    #     go_back_button = self.get_path(session_name, find_element_button)
                    #     print (get_search_result_text)
                    #     go_back_button.click()

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
                diffdate = datecau(d, r)
                print ("+++++++this is to check diff date++++++++++"), datecau(d, r)
                self.get_search_result(diffdate, prom_cod)
            else:
                Departure_date_selected.select_by_index(d)
                Return_date_selected.select_by_index(r)
                selected_d = 'This is your selected Departure:  '
                selected_d_t = Departure_date_selected.first_selected_option.text
                print selected_d, d, selected_d_t
                selected_r = 'This is your selected Return:  '
                selected_r_t = Return_date_selected.first_selected_option.text
                print selected_r, r, selected_r_t
                #datecau(d, r)
                diffdate = datecau(d, r)
                print ("+++++++this is to check diff date++++++++++"), datecau(d, r)
                self.get_search_result(diffdate, prom_cod)
        return (Departure_date_options_len)

    def execute_search(self):
        options_len = self.select_depature_return()
        # print options_len
        d = 0
        r = 0
        sum = 0
        while d < options_len:
            while r < options_len:
                self.select_depature_return(d, r)
                p = 0
                while p < 2:
                    prom_cod = promcodgent()
                    print ("hello, this is a code"), prom_cod
                    self.select_depature_return(d, r, prom_cod)
                    prom_cod = " "
                    p = p + 1
                    prom_cod = "dsfsdfewfsfsfwe"
                    self.select_depature_return(d, r, prom_cod)
                    prom_cod = " "
                    p = p + 1
                    sum = sum + 2
                r = r + 1
            p = 0
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
