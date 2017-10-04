import ConfigParser
import csv
import os
import unittest

from selenium import webdriver

from MarsAirbook.search_airtick.searchtrip import SearchTrip
from MarsAirbook.utils.promogenverify import prom_cod_gent
from MarsAirbook.utils.promogenverify import prom_codgent_invalid

filename = "test_result_air_book.csv"
result_title = (
    'depature id', 'return id', 'departure date', 'return date', "promotional code", 'day diff',
    'actual result screen', 'expected result', "status")
options_len = xrange(0, 7)

try:
    os.mkdir('actualresult')
except OSError:
    print "Folder are existing"


class AirTripbooking(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.config = ConfigParser.RawConfigParser(allow_no_value=True)
        cls.config.read('airtripconfig.txt')
        cls.driver = webdriver.Firefox()
        cls.provider = SearchTrip(cls.config, cls.driver)
        cls.provider.driver.get("http://junying.marsair.tw/")
        # cls.driver.get("http://junying.marsair.tw/")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def execute_search(self):
        run_case_count = 0
        with open(filename, 'wb') as csvwriter:
            writer = csv.writer(csvwriter, dialect='excel')
            writer.writerow(result_title)
            for current_depature_id in options_len:
                for current_return_id in options_len:
                    values = self.provider.get_depature_return(current_depature_id, current_return_id)
                    # print values
                    writer.writerow(values)
                    run_case_count = run_case_count + 1
                    p = 0
                    while p < 2:
                        if p == 0:
                            input_prom_cod = prom_cod_gent()
                            values = self.provider.get_depature_return(current_depature_id, current_return_id,
                                                                       input_prom_cod)
                            # print values
                            writer.writerow(values)
                        else:
                            input_prom_cod = prom_codgent_invalid()
                            values = self.provider.get_depature_return(current_depature_id, current_return_id,
                                                                       input_prom_cod)
                            # print values
                            writer.writerow(values)
                        p = p + 1
                        run_case_count = run_case_count + 1
            print ("Total test cases run :"), run_case_count

    def test_00_booking_trip_normal(self):
        self.execute_search()


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(AirTripbooking)
    suite.sortTestMethodsUsing = None
    unittest.TextTestRunner(verbosity=2).run(suite)
