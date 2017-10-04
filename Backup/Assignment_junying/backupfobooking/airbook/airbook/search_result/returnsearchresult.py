from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from airbook.utils.promo_gen_verify import promverify

no_seats = "Sorry, there are no more seats available."
book_now = "Seats available! Call 0800 MARSAIR to book!"
not_possible = "Unfortunately, this schedule is not possible. Please try again."

class ReturnResult(object):
    def __init__(self, config, driver):
        self.config = config
        self.driver = driver

    def get_path(self, section_name, find_element):
        get_element = self.config.get(section_name, find_element)
        get_element_local = self.driver.find_element_by_xpath(get_element)
        return (get_element_local)

    # this function returns a tuple of string and boolean
    def get_search_result(self, diffdate, prom_cod="none", d=0, r=0):
        test_case_screen, ret_validation, ret_status = "", "", False
        section_name = "Booking"
        find_element_path = "Search_button_xpath"
        Search_button = self.get_path(section_name, find_element_path).click()
        d = str(d)
        r = str(r)
        actual_screen = "actualresult\case-screen-" + d + "-" + r + ".png"

        try:
            WebDriverWait(self.driver, 3).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/h2')))

        except TimeoutException:
            actual_screen = "actualresult\unexpected-error-" + d + "-" + r + ".png"

            print(
                "Due to loading timeout expired or couldn't find wanted words,test skipped, (see {})".format(
                    actual_screen))
            self.driver.save_screenshot(actual_screen)
            self.driver.back()
            return (actual_screen, "unexpectederror", False)

        decoded = self.driver.page_source.encode('utf8', )
        if 365 <= diffdate <= 730 and prom_cod == "none":
            global no_seats, book_now
            # no_seats = "Sorry, there are no more seats available."
            # book_now = "Seats available! Call 0800 MARSAIR to book!"
            expectedresult = no_seats + book_now
            if no_seats not in decoded and book_now not in decoded:
                ret_validation, ret_status = expectedresult, False
                self.driver.save_screenshot(actual_screen)
                print "this way is diffdate meeted and without prom_cod, failed case (cannot find no_seats,book_now)", diffdate, prom_cod
                self.driver.back()
            else:
                if no_seats in decoded:
                    ret_validation, ret_status = no_seats, True
                    self.driver.save_screenshot(actual_screen)
                    print "this way is diffdate meeted and without prom_cod, pass case (no seats)", diffdate, prom_cod
                    self.driver.back()
                if book_now in decoded:
                    ret_validation, ret_status = book_now, True

                    self.driver.save_screenshot(actual_screen)
                    print "this way is diffdate meeted and without prom_cod, pass case (book now)", diffdate, prom_cod
                    self.driver.back()
            return (actual_screen, ret_validation, ret_status)
        if 365 <= diffdate <= 730 and prom_cod <> "none":
            if not promverify(prom_cod):
                invalid_prom_cod = "Sorry, code [" + prom_cod + "] is not valid"

                if invalid_prom_cod in decoded:
                    ret_validation, ret_status = invalid_prom_cod, True
                    self.driver.save_screenshot(actual_screen)
                    print "this way is diffdate meeted and with invalid prom_cod, pass (prom_cod is invalid)", diffdate, prom_cod
                    self.driver.back()
                else:
                    ret_validation, ret_status = invalid_prom_cod, False
                    self.driver.save_screenshot(actual_screen)
                    print "this way is diffdate meeted and with invalid prom_cod, failed (prom_cod is invalid)", diffdate, prom_cod
                    self.driver.back()
                return (actual_screen, ret_validation, ret_status)
            else:
                # no_seats = "Sorry, there are no more seats available."
                # book_now = "Seats available!"
                digit_1 = prom_cod[2]
                prom_cod_dis = "Promotional code [" + prom_cod + "] used: [" + digit_1 + "0]% discount!"
                expectedresult = no_seats + book_now
                expectedresult2 = book_now + prom_cod_dis
                if no_seats not in decoded and book_now not in decoded:
                    ret_validation, ret_status = expectedresult, False
                    self.driver.save_screenshot(actual_screen)
                    print "this way is diffdate meeted and valid prom_cod, failed case (cannot find no_seat, book_now)", diffdate, prom_cod
                    self.driver.back()
                    return (actual_screen, ret_validation, ret_status)
                else:
                    if no_seats in decoded:
                        ret_validation, ret_status = no_seats, True
                        self.driver.save_screenshot(actual_screen)
                        print "this way is diffdate meeted and with valid prom_cod, pass case (no seats)", diffdate, prom_cod
                        self.driver.back()
                        return (actual_screen, ret_validation, ret_status)
                    if book_now in decoded and prom_cod_dis in decoded:
                        ret_validation, ret_status = expectedresult2, True
                        self.driver.save_screenshot(actual_screen)
                        print "this way is diffdate meeted and with valid prom_cod, pass case (book now + pro_dis)", diffdate, prom_cod
                        self.driver.back()
                    else:
                        ret_validation, ret_status = expectedresult2, True
                        self.driver.save_screenshot(actual_screen)
                        print "this way is diffdate meeted and with valid prom_cod, failed case (book now + pro_dis)", diffdate, prom_cod
                        self.driver.back()
                    return (actual_screen, ret_validation, ret_status)
        else:
            #not_possible = "Unfortunately, this schedule is not possible. Please try again."
            if not_possible in decoded:
                ret_validation, ret_status = not_possible, True
                self.driver.save_screenshot(actual_screen)
                print "this way is diffdate not meeted and w/o prom_cod, pass case", diffdate, prom_cod
                self.driver.back()
            else:
                ret_validation, ret_status = not_possible, False
                self.driver.save_screenshot(actual_screen)
                print "this way is diffdate not meeted and w/o prom_cod, failed case", diffdate, prom_cod
                self.driver.back()
            return (actual_screen, ret_validation, ret_status)
