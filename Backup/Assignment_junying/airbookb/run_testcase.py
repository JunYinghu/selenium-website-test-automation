import ConfigParser
import csv
import unittest
import os
from selenium import webdriver

from airbook.search_airtick.searchtrip import SearchTrip
from airbook.utils.promogenverify import prom_cod_gent
from airbook.utils.promogenverify import prom_codgent_invalid
from airbook.utils.Testcase import prom_verify

# filename = "test_result_air_book.csv"
# result_title = (
# 'depature id', 'return id', 'departure date', 'return date', "promotional code", 'day diff',
# 'actual result screen', 'expected result',"book link" "status")
# options_len = 7
#
# try:
#     os.mkdir('actualresult')
# except OSError:
#     print "Folder are existing"
#
print prom_verify("KU5-ROO-555")

class AirTripbooking(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.config = ConfigParser.RawConfigParser(allow_no_value=True)
        cls.config.read('airtripconfig.txt')
        #cls.driver = webdriver.Firefox()
        #cls.provider = SearchTrip(cls.config, cls.driver)
        #cls.provider.driver.get("http://junying.marsair.tw/")

    #def teardown(cls):
    #   time.sleep(8)
    #   cls.driver.quit()

#
#     def execute_search(self):
#
#         #print options_len
#         current_depature_id = 0
#         run_case_count = 0
#         with open(filename, 'wb') as csvwriter:
#             writer = csv.writer(csvwriter, dialect='excel')
#             writer.writerow(result_title)
#             while current_depature_id < options_len:
#                 current_return_id = 0
#                 while current_return_id < options_len:
#                     values = self.provider.get_depature_return(current_depature_id, current_return_id)
#                     print values
#                     writer.writerow(values)
#                     run_case_count = run_case_count + 1
#                     p = 0
#                     while p < 2:
#                         if p == 0:
#                             input_prom_cod = prom_cod_gent()
#                             values = self.provider.get_depature_return(current_depature_id, current_return_id, input_prom_cod)
#                             writer.writerow(values)
#
#                         else:
#                             input_prom_cod = prom_codgent_invalid()
#                             values = self.provider.get_depature_return(current_depature_id, current_return_id, input_prom_cod)
#                             writer.writerow(values)
#                         p = p + 1
#                         run_case_count = run_case_count + 1
#                     current_return_id = current_return_id + 1
#                 current_depature_id = current_depature_id + 1
#             print ("Total test cases run :"), run_case_count

    def test_00_booking_trip_normal(self):
        #self.execute_search()
        pass

    def test_01_check_search_page(self):
        pass



if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(AirTripbooking)
    suite.sortTestMethodsUsing = None
    unittest.TextTestRunner(verbosity=2).run(suite)
