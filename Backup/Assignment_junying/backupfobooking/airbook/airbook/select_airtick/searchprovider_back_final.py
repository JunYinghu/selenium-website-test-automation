import ConfigParser
from time import time
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait

from airbook.utils.date_cal import datecau
from airbook.utils.promo_gen_verify import promverify


class SearchProvider(object):
    def __init__(self, config_path, firefox=webdriver.Firefox()):
        self.config = ConfigParser.RawConfigParser(allow_no_value=True)
        self.config.read(config_path)
        self.driver = firefox

    def get_path(self, section_name, find_element):
        get_element = self.config.get(section_name, find_element)
        get_element_local = self.driver.find_element_by_xpath(get_element)
        return (get_element_local)

    # this function returns a tuple of string and boolean
    def get_search_result(self, diffdate, prom_cod="none"):
        test_case_screen, ret_validation, ret_status = "", "", False
        section_name = "Booking"
        find_element_path = "Search_button_xpath"
        Search_button = self.get_path(section_name, find_element_path).click()
        try:
            WebDriverWait(self.driver, 3).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/h2')))
            # print ("Please check output csv file test_result_air_book.csv ")
        except TimeoutException:
            filename = "unexpecederror-{}.png".format(int(time()))
            print(
                "Due to loading timeout expired or couldn't find wanted words,test skipped, (see {})".format(filename))
            self.driver.save_screenshot(filename)
            self.driver.back()
            return (test_case_screen, filename, False)

        decoded = self.driver.page_source.encode('utf8', )
        if 365 <= diffdate <= 730 and prom_cod == "none":
            no_seats = "Sorry, there are no more seats available."
            book_now = "Seats available! Call 0800 MARSAIR to book!"
            expectedresult = no_seats + book_now
            if no_seats not in decoded and book_now not in decoded:
                ret_validation, ret_status = expectedresult, False
                test_case_screen = "screen_case{}.png".format(int(time()))
                self.driver.save_screenshot(test_case_screen)
                print "this way is diffdate meeted and without prom_cod, failed case (cannot find no_seats,book_now)", diffdate, prom_cod
                self.driver.back()
            else:
                if no_seats in decoded:
                    ret_validation, ret_status = no_seats, True
                    test_case_screen = "screen_case{}.png".format(int(time()))
                    self.driver.save_screenshot(test_case_screen)
                    print "this way is diffdate meeted and without prom_cod, pass case (no seats)", diffdate, prom_cod
                    self.driver.back()
                if book_now in decoded:
                    ret_validation, ret_status = book_now, True
                    test_case_screen = "screen_case{}.png".format(int(time()))
                    self.driver.save_screenshot(test_case_screen)
                    print "this way is diffdate meeted and without prom_cod, pass case (book now)", diffdate, prom_cod
                    self.driver.back()
            return (test_case_screen, ret_validation, ret_status)
        if 365 <= diffdate <= 730 and prom_cod <> "none":
            if not promverify(prom_cod):
                invalid_prom_cod = "Sorry, code [" + prom_cod + "] is not valid"

                if invalid_prom_cod in decoded:
                    ret_validation, ret_status = invalid_prom_cod, True
                    test_case_screen = "screen_case{}.png".format(int(time()))
                    self.driver.save_screenshot(test_case_screen)
                    print "this way is diffdate meeted and with invalid prom_cod, pass (prom_cod is invalid)", diffdate, prom_cod
                    self.driver.back()
                else:
                    ret_validation, ret_status = invalid_prom_cod, False
                    test_case_screen = "screen_case{}.png".format(int(time()))
                    self.driver.save_screenshot(test_case_screen)
                    print "this way is diffdate meeted and with invalid prom_cod, failed (prom_cod is invalid)", diffdate, prom_cod
                    self.driver.back()
                return (test_case_screen, ret_validation, ret_status)
            else:
                no_seats = "Sorry, there are no more seats available."
                book_now = "Seats available!"
                digit_1 = prom_cod[2]
                prom_cod_dis = "Promotional code [" + prom_cod + "] used: [" + digit_1 + "0]% discount!"
                expectedresult = no_seats + book_now
                expectedresult2 = book_now + prom_cod_dis
                if no_seats not in decoded and book_now not in decoded:
                    ret_validation, ret_status = expectedresult, False
                    test_case_screen = "screen_case{}.png".format(int(time()))
                    self.driver.save_screenshot(test_case_screen)
                    print "this way is diffdate meeted and valid prom_cod, failed case (cannot find no_seat, book_now)", diffdate, prom_cod
                    self.driver.back()
                    return (test_case_screen, ret_validation, ret_status)
                else:
                    if no_seats in decoded:
                        ret_validation, ret_status = no_seats, True
                        test_case_screen = "screen_case{}.png".format(int(time()))
                        self.driver.save_screenshot(test_case_screen)
                        print "this way is diffdate meeted and with valid prom_cod, pass case (no seats)", diffdate, prom_cod
                        self.driver.back()
                        return (test_case_screen, ret_validation, ret_status)
                    if book_now in decoded and prom_cod_dis in decoded:
                        ret_validation, ret_status = expectedresult2, True
                        test_case_screen = "screen_case{}.png".format(int(time()))
                        self.driver.save_screenshot(test_case_screen)
                        print "this way is diffdate meeted and with valid prom_cod, pass case (book now + pro_dis)", diffdate, prom_cod
                        self.driver.back()
                    else:
                        ret_validation, ret_status = expectedresult2, True
                        test_case_screen = "screen_case{}.png".format(int(time()))
                        self.driver.save_screenshot(test_case_screen)
                        print "this way is diffdate meeted and with valid prom_cod, failed case (book now + pro_dis)", diffdate, prom_cod
                        self.driver.back()
                    return (test_case_screen, ret_validation, ret_status)
        else:
            not_possible = "Unfortunately, this schedule is not possible. Please try again."
            if not_possible in decoded:
                ret_validation, ret_status = not_possible, True
                test_case_screen = "screen_case{}.png".format(int(time()))
                self.driver.save_screenshot(test_case_screen)
                print "this way is diffdate not meeted and w/o prom_cod, pass case", diffdate, prom_cod
                self.driver.back()
            else:
                ret_validation, ret_status = not_possible, False
                test_case_screen = "screen_case{}.png".format(int(time()))
                self.driver.save_screenshot(test_case_screen)
                print "this way is diffdate not meeted and w/o prom_cod, failed case", diffdate, prom_cod
                self.driver.back()
            return (test_case_screen, ret_validation, ret_status)

            # def check_input_items(validationtext):
            #     if validationtext in decoded:
            #         ret_validation, ret_status = expectedresult, True
            #         test_case_screen = "screen_case{}.png".format(int(time()))
            #         self.driver.save_screenshot(test_case_screen)
            #         self.driver.back()
            #     else:
            #         ret_validation, ret_status = validationtext, False
            #         test_case_screen = "screen_case{}.png".format(int(time()))
            #         self.driver.save_screenshot(test_case_screen)
            #         # test_case_screen =self.takescreen()
            #         self.driver.back()
            #
            # if 365 <= diffdate <= 730:
            #     if prom_cod <> "none":
            #         # when promotion cod is valid
            #         if promverify(prom_cod):
            #             validation_1 = "Sorry, there are no more seats available."
            #             validation_2 = "Seats available! Call 0800 MARSAIR to book!"
            #             digit_1 = prom_cod[2]
            #             expectedresult = validation_1 + "  " + validation_2
            #             if validation_1 in decoded:
            #                 expectedresult = validation_1
            #                 ret_validation, ret_status = expectedresult, True
            #                 test_case_screen = "screen_case{}.png".format(int(time()))
            #                 self.driver.save_screenshot(test_case_screen)
            #                 self.driver.back()
            #             elif validation_2 in decoded:
            #                 validation = "Promotional code [" + prom_cod + "] used: [" + digit_1 + "0]% discount!"
            #                 if validation in decoded:
            #                     ret_validation, ret_status = validation + validation_2, True
            #                     test_case_screen = "screen_case{}.png".format(int(time()))
            #                     self.driver.save_screenshot(test_case_screen)
            #                     self.driver.back()
            #
            #                 else:
            #                     ret_validation, ret_status = validation + validation_2, False
            #                     test_case_screen = "screen_case{}.png".format(int(time()))
            #                     self.driver.save_screenshot(test_case_screen)
            #
            #                     self.driver.back()
            #             else:
            #                 ret_validation, ret_status = expectedresult, False
            #                 test_case_screen = "screen_case{}.png".format(int(time()))
            #                 self.driver.save_screenshot(test_case_screen)
            #
            #                 self.driver.back()
            #         # when  promotion code is invalid
            #         else:
            #             validation = "Sorry, code [" + prom_cod + "] is not valid"
            #             if validation in decoded:
            #                 ret_validation, ret_status = validation, True
            #                 test_case_screen = "screen_case{}.png".format(int(time()))
            #                 self.driver.save_screenshot(test_case_screen)
            #                 self.driver.back()
            #             else:
            #                 ret_validation, ret_status = validation, False
            #                 test_case_screen = "screen_case{}.png".format(int(time()))
            #                 self.driver.save_screenshot(test_case_screen)
            #             self.driver.back()
            #     else:
            #         validation_1 = "Sorry, there are no more seats available."
            #         validation_2 = "Seats available! Call 0800 MARSAIR to book!"
            #         expectedresult = validation_1 + "  " + validation_2
            #         if validation_1 in decoded:
            #             expectedresult = validation_1
            #             ret_validation, ret_status = expectedresult, True
            #             test_case_screen = "screen_case{}.png".format(int(time()))
            #             self.driver.save_screenshot(test_case_screen)
            #             self.driver.back()
            #         elif validation_2 in decoded:
            #             expectedresult = validation_2
            #             ret_validation, ret_status = expectedresult, True
            #             test_case_screen = "screen_case{}.png".format(int(time()))
            #             self.driver.save_screenshot(test_case_screen)
            #             self.driver.back()
            #         else:
            #             ret_validation, ret_status = expectedresult, False
            #             test_case_screen = "screen_case{}.png".format(int(time()))
            #             self.driver.save_screenshot(test_case_screen)
            #         self.driver.back()
            # else:
            #     validation = "Unfortunately, this schedule is not possible. Please try again."
            #     if (validation in decoded):
            #         ret_validation, ret_status = validation, True
            #         test_case_screen = "screen_case{}.png".format(int(time()))
            #         self.driver.save_screenshot(test_case_screen)
            #         self.driver.back()
            #     else:
            #         ret_validation, ret_status = validation, False
            #         test_case_screen = "screen_case{}.png".format(int(time()))
            #         self.driver.save_screenshot(test_case_screen)
            #         self.driver.back()
            #     self.driver.back()
            # return (test_case_screen, ret_validation, ret_status)

    def send_departure(self, section_name, find_element_path):
        departure_selected = Select(self.get_path(section_name, find_element_path))
        # departure_date_option = self.get_path(section_name, find_element_path)
        return (departure_selected)

    def send_return(self, section_name, find_element_path):
        return_selected = Select(self.get_path(section_name, find_element_path))
        # return_date_option = self.get_path(section_name, find_element_path)
        return (return_selected)

    def select_depature_return(self, d=0, r=0, prom_cod="none"):
        selected_d_t = "none"
        selected_r_t = "none"
        diffdate = 0
        status, expected = "none", "none"

        find_element_path = "Departure_option_xpath"
        section_name = "Booking"
        (departure_selected) = self.send_departure(section_name, find_element_path)
        # Departure_date = self.get_path(section_name, find_element_path)
        find_element_path = "Return_option_xpath"
        (return_selected) = self.send_departure(section_name, find_element_path)
        # Return_date = self.get_path(section_name, find_element_path)
        find_element_text = "Promotional_code_xpath"
        input_prom_code = self.get_path(section_name, find_element_text)
        input_prom_code.clear()
        departure_selected.select_by_index(d)
        return_selected.select_by_index(r)

        if prom_cod <> "none":
            input_prom_code.send_keys(prom_cod)
            depature_current_selected = departure_selected.first_selected_option.text  # get current selected option 's text
            return_current_selected = return_selected.first_selected_option.text  # get current selected option 's text
            diffdate = datecau(d, r)
            test_case_screen, expected, status = self.get_search_result(diffdate, prom_cod)
        else:

            depature_current_selected = departure_selected.first_selected_option.text  # get current selected option 's text
            return_current_selected = return_selected.first_selected_option.text  # get current selected option 's text
            diffdate = datecau(d, r)
            test_case_screen, expected, status = self.get_search_result(diffdate, prom_cod)
        return (
            d, r, depature_current_selected, return_current_selected, prom_cod, diffdate, test_case_screen, expected,
            status)
