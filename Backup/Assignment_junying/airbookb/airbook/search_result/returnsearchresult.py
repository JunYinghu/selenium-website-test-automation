from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from datetime import datetime
from airbook.utils.getpath import GetElementPath
from airbook.utils.promogenverify import prom_verify

no_seats = "Sorry, there are no more seats available."
book_now = "Seats available! Call now on 0800 MARSAIR to book!"
not_possible = "Unfortunately, this schedule is not possible. Please try again."
# book_link = "Book a ticket to the red planet now!"


class ReturnResult(GetElementPath):
    def __init__(self, config, driver):
        GetElementPath.__init__(self, config, driver)

    # this function returns a tuple of string and boolean
    def get_search_result(self, diffdate, input_prom_cod="none", current_depature_id=0, current_return_id=0):

        test_case_screen, ret_validation, status = "", "", False
        section_name = "Booking"
        find_element_path = "Search_button_xpath"
        self.get_path(section_name, find_element_path).click()
        d = str(current_depature_id)
        r = str(current_return_id)
        actual_screen = "actualresult\case-screen-" + d + "-" + r + "{}.png"
        try:
            WebDriverWait(self.driver, 3).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/h2')))

        except TimeoutException:
            actual_screen = "actualresult\unexpected-error-" + d + "-" + r + "{}.png".format(datetime.now())

            print(
                "Due to loading timeout or couldn't find wanted words,skipped, (see {})".format(
                    actual_screen))
            self.driver.save_screenshot(actual_screen)
            self.driver.back()
            return actual_screen, "unexpectederror", False
        decoded = self.driver.page_source.encode('utf8', )
        # if 365 <= diffdate <= 730 and input_prom_cod == "none":
        if 365 <= diffdate and input_prom_cod == "none":
            expectedresult = no_seats + book_now
            if (no_seats not in decoded) and (book_now not in decoded):
                ret_validation, status = expectedresult, False
                self.driver.save_screenshot(actual_screen)
                print "daydiff meeted and without prom_cod, failed (cannot find no_seats,book_now)", diffdate, input_prom_cod
                self.driver.back()

            else:
                if no_seats in decoded:
                    ret_validation, status = no_seats, True
                    self.driver.save_screenshot(actual_screen)
                    print "daydiff meeted and without prom_cod, pass (no seats)", diffdate, input_prom_cod
                    self.driver.back()
                    return actual_screen, ret_validation, status
                if book_now in decoded:
                    ret_validation, status = book_now, True
                    self.driver.save_screenshot(actual_screen)
                    print "daydiff meeted and without prom_cod, pass (book now)", diffdate, input_prom_cod
                    self.driver.back()
                    return actual_screen, ret_validation, status
            return actual_screen, ret_validation, status

        # if 365 <= diffdate <= 730 and input_prom_cod != "none":
        if 365 <= diffdate and input_prom_cod != "none":
            invalid_prom_cod = "Sorry, code [" + input_prom_cod + "] is not valid"
            if no_seats in decoded:
                ret_validation, status = no_seats, True
                self.driver.save_screenshot(actual_screen)
                print "valid daydiff & invalid prom_cod, pass (no_seat)", diffdate, input_prom_cod
                self.driver.back()
                return actual_screen, ret_validation, status
            if book_now in decoded:

                if not prom_verify(input_prom_cod):
                    if invalid_prom_cod in decoded:
                        ret_validation, status = invalid_prom_cod, True
                        self.driver.save_screenshot(actual_screen)
                        print "daydiff meeted and with invalid prom_cod, pass", diffdate, input_prom_cod
                        self.driver.back()
                        return actual_screen, ret_validation, status
                    else:
                        ret_validation, status = invalid_prom_cod, False
                        self.driver.save_screenshot(actual_screen)
                        print "daydiff meeted and with invalid prom_cod, failed", diffdate, input_prom_cod
                        self.driver.back()
                        return actual_screen, ret_validation, status
                else:
                    digit_1 = input_prom_cod[2]
                    prom_cod_dis = "Promotional code [" + input_prom_cod + "] used: [" + digit_1 + "0]% discount!"
                    expectedresult2 = book_now + prom_cod_dis

                    if prom_cod_dis in decoded:
                        ret_validation, status = expectedresult2, True
                        self.driver.save_screenshot(actual_screen)
                        print "valid daydiff & prom_cod,pass (book now + pro_dis)", diffdate, input_prom_cod
                        self.driver.back()
                        return actual_screen, ret_validation, status
                    else:
                        ret_validation, status = no_seats, False
                        self.driver.save_screenshot(actual_screen)
                        print "valid daydiff & prom_cod, pass (no_seat)", diffdate, input_prom_cod
                        self.driver.back()
                        return actual_screen, ret_validation, status
            else:
                ret_validation, status = no_seats, False
                self.driver.save_screenshot(actual_screen)
                print "valid daydiff & prom_cod, failed (cannot find expected text)", diffdate, input_prom_cod

                self.driver.back()
                return actual_screen, ret_validation, status
        else:
            if not_possible in decoded:
                ret_validation, status = not_possible, True
                self.driver.save_screenshot(actual_screen)
                print "daydiff not meeted and w/o prom_cod, pass case", diffdate, input_prom_cod

                self.driver.back()
            else:
                ret_validation, status = not_possible, False
                self.driver.save_screenshot(actual_screen)
                print "daydiff not meeted and w/o prom_cod, failed", diffdate, input_prom_cod

                self.driver.back()
            return actual_screen, ret_validation, status