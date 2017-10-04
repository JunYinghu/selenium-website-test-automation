import ConfigParser
from time import time

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from airbook.utils.takescreen import CommUtils

from airbook.utils.date_cal import datecau
from airbook.utils.promverify import promverify


# cu = CommUtils()
# cu.takescreen()

class SearchProvider(object):
    def __init__(self, config_path):
        self.config = ConfigParser.RawConfigParser(allow_no_value=True)
        self.config.read(config_path)
        self.driver = webdriver.Firefox()

    def get_path(self, section_name, find_element):
        get_element = self.config.get(section_name, find_element)
        get_element_local = self.driver.find_element_by_xpath(get_element)
        return (get_element_local)

    # this function returns a tuple of string and boolean
    def get_search_result(self, diffdate, prom_cod="none"):
        print "There are diffdate and prom_cod", diffdate,prom_cod
        test_case_screen, ret_validation, ret_status = "", "", False
        section_name = "Booking"
        find_element_text = "Search_button_xpath"
        Search_button = self.get_path(section_name, find_element_text).click()
        try:
            WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/h2')))
            print ("you may start to verify search result going to output csv file test_result_air_book.csv ")
        except TimeoutException:
            filename = "Weird_error-{}.png".format(int(time()))
            print(
                "Due to loading timeout expired or could not find the element,test skipped, (see {})".format(filename))
            self.driver.save_screenshot(filename)
            self.driver.back()
            return (test_case_screen, filename, False)
        decoded = self.driver.page_source.encode('utf8', )

        # trips  for 2 years are reachable
        #print ("++++++++++++++++++kkdiff date++++++++++++++++++ "), diffdate
        def check_input_items(decoded, validationtext,validationtext2="none"):
                if validationtext in decoded:
                    ret_validation, ret_status = validationtext, True
                    test_case_screen = "screen_case{}.png".format(int(time()))
                    self.driver.save_screenshot(test_case_screen)
                    self.driver.back()
                if validationtext2 in decoded:
                    ret_validation, ret_status = validationtext, True
                    test_case_screen = "screen_case{}.png".format(int(time()))
                    self.driver.save_screenshot(test_case_screen)
                    self.driver.back()
                else:
                    ret_validation, ret_status = validationtext, False
                    test_case_screen = "failed_case{}.png".format(int(time()))
                    self.driver.save_screenshot(test_case_screen)
                    # test_case_screen =self.takescreen()
                    self.driver.back()
                return (test_case_screen,ret_validation,ret_status)

        if 365 <= diffdate <= 730:
            if prom_cod <> "none":
                print "This is for scheduled trip with pro_code",diffdate,prom_cod
                # when promotion cod is valid
                if promverify(prom_cod):
                    validation_1 = "Sorry, there are no more seats available."
                    validation_2 = "Seats available! Call 0800 MARSAIR to book!"
                    digit_1 = prom_cod[2]
                    expectedresult = validation_1 + "  " + validation_2
                    if validation_1 in decoded:
                        print "This is for scheduled trip with pro_code and no seats", diffdate, prom_cod
                        #expectedresult = validation_1
                        ret_validation, ret_status = validation_1, True
                        test_case_screen = "screen_case{}.png".format(int(time()))
                        self.driver.save_screenshot(test_case_screen)
                        self.driver.back()
                    if validation_2 in decoded:
                        print "This is for scheduled trip with pro_code and  discount", diffdate, prom_cod
                        validation = "Promotional code [" + prom_cod + "] used: [" + digit_1 + "0]% discount!"
                        (test_case_screen, ret_validation, ret_status) = check_input_items(validation)

                    else:
                        print "This is for scheduled trip with pro_code, but cannot get expected result", diffdate, prom_cod
                        ret_validation, ret_status = expectedresult, False
                        test_case_screen = "failed_case{}.png".format(int(time()))
                        self.driver.save_screenshot(test_case_screen)
                        # test_case_screen =self.takescreen()
                        self.driver.back()
                # when  promotion code is invalid
                else:
                    validation = "Sorry, code [" + prom_cod + "] is not valid"
                    (test_case_screen, ret_validation, ret_status) = check_input_items(validation)
                    self.driver.back()
            else:
                validation_1 = "Sorry, there are no more seats available."
                validation_2 = "Seats available! Call 0800 MARSAIR to book!"
                print ("_________this is for scheduled diff date with pro_cod empty ___________"), diffdate,prom_cod
                (test_case_screen, ret_validation, ret_status) = check_input_items(validation_1,validation_2)
            self.driver.back()
        else:
            validation = "Unfortunately, this schedule is not possible. Please try again."
            print ("_________this is for Unfortunately schedule diff date ___________"), diffdate
            (test_case_screen, ret_validation, ret_status) = check_input_items(validation)
        self.driver.back()
        return (test_case_screen, ret_validation, ret_status)

    def select_depature_return(self, d=0, r=0, prom_cod="none"):
        selected_d_t = "none"
        selected_r_t = "none"
        diffdate = 0
        status, expected = "none", "none"
        find_element_text = "Departure_option_xpath"
        section_name = "Booking"
        Departure_date_selected = Select(self.get_path(section_name, find_element_text))
        Departure_date = self.get_path(section_name, find_element_text)
        # Departure_date_options = Departure_date.find_elements_by_tag_name("option")
        Departure_date_options_len = len(Departure_date.find_elements_by_tag_name("option"))
        find_element_text = "Return_option_xpath"
        Return_date_selected = Select(self.get_path(section_name, find_element_text))
        Return_date = self.get_path(section_name, find_element_text)
        # Return_date_options = Return_date.find_elements_by_tag_name("option")
        find_element_text = "Promotional_code_xpath"
        input_prom_code = self.get_path(section_name, find_element_text)
        input_prom_code.clear()
        Departure_date_selected.select_by_index(d)
        Return_date_selected.select_by_index(r)

        if prom_cod <> "none":
            # Departure_date_selected.select_by_index(d)
            # Return_date_selected.select_by_index(r)
            input_prom_code.send_keys(prom_cod)
            #selected_d = 'This is your selected departure:  '
            selected_d_t = Departure_date_selected.first_selected_option.text
            # print selected_d, d, selected_d_t
            #selected_r = 'This is your selected return:  '
            selected_r_t = Return_date_selected.first_selected_option.text
            # print selected_r, r, selected_r_t
            # prom_r = 'This is your entered promotional code:  '
            # print prom_r, prom_cod
            diffdate = datecau(d, r)
            #print ("+++++++this is to check diff date++++++++++"), diffdate
            test_case_screen, expected, status = self.get_search_result(diffdate, prom_cod)
            #print self.get_search_result(diffdate, prom_cod)
        else:
            # Departure_date_selected.select_by_index(d)
            # Return_date_selected.select_by_index(r)
            # selected_d = 'This is your selected Departure:  '
            selected_d_t = Departure_date_selected.first_selected_option.text
            # print selected_d, d, selected_d_t
            # selected_r = 'This is your selected Return:  '
            selected_r_t = Return_date_selected.first_selected_option.text
            # print selected_r, r, selected_r_t
            diffdate = datecau(d, r)
            # print ("+++++++this is to check diff date++++++++++"), diffdate
            # SearchResult.getsearchresult(diffdate,prom_cod)
            test_case_screen, expected, status = self.get_search_result(diffdate, prom_cod)
            # print ("+++++++this is to check expected, status++++++++++"), expected, status

        return (d, r, selected_d_t, selected_r_t, prom_cod, diffdate, test_case_screen, expected, status)
