from datetime import datetime
import re
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from MarsAirbook.utils.getpath import GetElementPath
from MarsAirbook.utils.promogenverify import prom_verify

no_seats = "Sorry, there are no more seats available."
# book_now = "Seats available! Call 0800 MARSAIR to book!"
book_now = "Seats available!"
not_possible = "Unfortunately, this schedule is not possible. Please try again."
book_link = "Book a ticket to the red planet now!"

screen = "actualresult\case-screen-"
Search_result_check = '/html/body/div[1]/div/h2'


class ReturnResult(GetElementPath):
    def __init__(self, config, driver):
        GetElementPath.__init__(self, config, driver)

    def check_book_link(self, book_link, current_page_content):
        print book_link,
        if book_link not in current_page_content:
            book_link = "not found"
        else:
            book_link = "found"
        return book_link
        # assert book_link in current_page_content

    # this function returns a tuple of string and boolean
    def get_search_result(self, daydiff, input_prom_cod="none", current_depature_id=0, current_return_id=0):
        actual_screen, ret_validation, status = "", "", False
        section_name = "Booking"
        find_element_path = "Search_button_xpath"
        self.get_path(section_name, find_element_path).click()
        d = str(current_depature_id)
        r = str(current_return_id)
        actual_screen = screen + d + "-" + r + "-{}.png".format(datetime.now().strftime("%y%m%d_%H%M%S"))
        try:
            WebDriverWait(self.driver, 3).until(EC.presence_of_element_located((By.XPATH, Search_result_check)))

        except TimeoutException:
            actual_screen = "actualresult\unexpected-error-" + d + "-" + r + "-{}.png".format(
                datetime.now().strftime("%y%m%d_%H%M%S"))
            print(
                "Due to loading timeout or Search Result is not found , (see {})".format(
                    actual_screen))
            self.driver.save_screenshot(actual_screen)
            self.driver.back()
            return actual_screen, "unexpectederror", False

        current_page_content = self.driver.page_source.encode('utf8', )
        if (365 <= daydiff) and (input_prom_cod == "none"):
            expectedresult = no_seats + book_now
            if (no_seats not in current_page_content) and (book_now not in current_page_content):
                ret_validation, status = expectedresult, False
                self.driver.save_screenshot(actual_screen)
                print self.check_book_link(book_link, current_page_content)
                # print "daydiff meeted and without prom_cod, failed (no_seats, book_now)",  daydiff, input_prom_cod
                self.driver.back()
            else:
                if no_seats in current_page_content:
                    ret_validation, status = no_seats, True
                    self.driver.save_screenshot(actual_screen)
                    print self.check_book_link(book_link, current_page_content)
                    # print "daydiff meeted and without prom_cod, pass (no seats)", daydiff, input_prom_cod
                    self.driver.back()
                    return actual_screen, ret_validation, status
                if book_now in current_page_content:
                    ret_validation, status = book_now, True
                    self.driver.save_screenshot(actual_screen)
                    print self.check_book_link(book_link, current_page_content)
                    # print "daydiff meeted and without prom_cod, pass (book now)", daydiff, input_prom_cod
                    self.driver.back()
                    return actual_screen, ret_validation, status
            return actual_screen, ret_validation, status
        if (365 <= daydiff) and (input_prom_cod != "none") and (no_seats in current_page_content):
            ret_validation, status = no_seats, True
            self.driver.save_screenshot(actual_screen)
            print self.check_book_link(book_link, current_page_content)
            # print "valid daydiff & invalid prom_cod, pass (no_seat)", daydiff, input_prom_cod
            self.driver.back()
            return actual_screen, ret_validation, status
        if (365 <= daydiff) and (input_prom_cod != "none") and (book_now in current_page_content):
            invalid_prom_cod_text = "Sorry, code " + input_prom_cod + " is not valid"

            pattern = '<p>(.+?)</p><p.*?>(.+?)<tt>(.+?)</tt>(.+?)</p><p>(.+?)</p>'
            ret = re.search(pattern, current_page_content)
            matching_string = ' '.join([x.strip() for x in ret.groups()][1:-1:]) if ret else ''
            if ret:
                print "#####", ret.groups()

            invalid_prom_cod=matching_string
            #invalid_prom_cod = "is not valid"
            print invalid_prom_cod
            if not prom_verify(input_prom_cod):
                print "invalid ", current_page_content
                if invalid_prom_cod in current_page_content:
                    ret_validation, status = invalid_prom_cod_text, True
                    self.driver.save_screenshot(actual_screen)
                    print self.check_book_link(book_link, current_page_content)
                    # print "daydiff meeted and with invalid prom_cod, pass", daydiff, input_prom_cod
                    self.driver.back()
                    return actual_screen, ret_validation, status
                else:
                    ret_validation, status = invalid_prom_cod_text, False
                    self.driver.save_screenshot(actual_screen)
                    print self.check_book_link(book_link, current_page_content)
                    # print "daydiff meeted and with invalid prom_cod, failed", daydiff, input_prom_cod
                    self.driver.back()
                    return actual_screen, ret_validation, status
            else:
                digit_1 = input_prom_cod[2]
                prom_cod_dis_text = "Promotional code " + input_prom_cod + " used: " + digit_1 + "0% discount!"
                prom_cod_dis = digit_1 + "0% discount"
                expectedresult2 = book_now + prom_cod_dis_text
                # print current_page_content
                if prom_cod_dis in current_page_content:
                    ret_validation, status = expectedresult2, True
                    self.driver.save_screenshot(actual_screen)
                    print self.check_book_link(book_link, current_page_content)
                    # print "valid daydiff & prom_cod,pass (book now + pro_dis)", daydiff, input_prom_cod
                    self.driver.back()
                    return actual_screen, ret_validation, status
                else:
                    ret_validation, status = "Discount is not calculated", False
                    self.driver.save_screenshot(actual_screen)
                    print self.check_book_link(book_link, current_page_content)
                    # print "valid daydiff & prom_cod, pass (no_seat)", daydiff, input_prom_cod
                    self.driver.back()
                    return actual_screen, ret_validation, status
            return actual_screen, ret_validation, status
        if 365 > daydiff:
            if not_possible in current_page_content:
                ret_validation, status = not_possible, True
                self.driver.save_screenshot(actual_screen)
                print self.check_book_link(book_link, current_page_content)
                # print "daydiff not meeted and w/o prom_cod, pass case", daydiff, input_prom_cod
                self.driver.back()
            else:
                ret_validation, status = not_possible, False
                self.driver.save_screenshot(actual_screen)
                print self.check_book_link(book_link, current_page_content)
                # print "daydiff not meeted and w/o prom_cod, failed", daydiff, input_prom_cod
                self.driver.back()
            return actual_screen, ret_validation, status
