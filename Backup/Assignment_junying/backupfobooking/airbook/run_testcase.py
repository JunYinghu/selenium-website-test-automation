import ConfigParser
import csv
import unittest
import os
from selenium import webdriver

from airbook.select_airtick.searchprovider import SearchProvider
from airbook.utils.promo_gen_verify import promcodgent
from airbook.utils.promo_gen_verify import promcodgentinvalid

filename = "test_result_air_book.csv"
result_title = (
'selected depature_id', 'selected returning_id', 'depature_date', 'returing_date', "promcode", 'diff_day',
'actual_result_screen', 'expected_result', "status")

try:
    os.mkdir('actualresult')
except OSError:
    print "create folder"
    pass

class AirTripbooking(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.config = ConfigParser.RawConfigParser(allow_no_value=True)
        cls.config.read('airtripconfig.txt')
        cls.driver = webdriver.Firefox()
        cls.provider = SearchProvider(cls.config, cls.driver)
        cls.provider.driver.get("http://junying.marsair.tw/")


    # # def teardown(cls):
    # #     time.sleep(8)
    # #     cls.driver.quit()

    def execute_search(self):
        options_len = 7
        print options_len
        d = 0
        run_case_count = 0
        with open(filename, 'wb') as csvwriter:
            writer = csv.writer(csvwriter, dialect='excel')
            writer.writerow(result_title)
            while d < options_len:
                r = 0
                while r < options_len:
                    values = self.provider.select_depature_return(d, r)
                    print values
                    # with open (filename, 'wb') as csvwriter:
                    #     writer = csv.writer(csvwriter, dialect='excel')
                    writer.writerow(values)
                    run_case_count = run_case_count + 1
                    p = 0
                    while p < 2:
                        if p == 0:
                            prom_cod = promcodgent()
                            # print ("hello, this is a code"), prom_cod
                            values = self.provider.select_depature_return(d, r, prom_cod)
                            # with open(filename, 'wb') as csvwriter:
                            #     writer = csv.writer(csvwriter, dialect='excel')
                            writer.writerow(values)

                        else:
                            prom_cod = promcodgentinvalid()
                            values = self.provider.select_depature_return(d, r, prom_cod)
                            # with open(filename, 'wb') as csvwriter:
                            #     writer = csv.writer(csvwriter, dialect='excel')
                            writer.writerow(values)
                        p = p + 1
                        run_case_count = run_case_count + 1
                    r = r + 1
                d = d + 1

            print ("Total test cases run :"), run_case_count

    def test_00_booking_trip_normal(self):
        self.execute_search()

    def test_01_check_search_page(self):
        pass


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(AirTripbooking)
    suite.sortTestMethodsUsing = None
    unittest.TextTestRunner(verbosity=2).run(suite)
