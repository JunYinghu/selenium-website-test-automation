import unittest

from airbook.search_result.search_result_writer import SearchResultWriter
from airbook.select_airtick.searchprovider import SearchProvider
from airbook.utils.promo_gen_verify import promcodgent
from airbook.utils.promo_gen_verify import promcodgentinvalid


# from airbook.search_result.writecsv import writecsv

class AirTripbooking(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.provider = SearchProvider('airtripconfig.txt')
        cls.provider.driver.get("http://junying.marsair.tw/")

    # # def teardown(cls):
    # #     time.sleep(8)
    # #     cls.driver.quit()

    def execute_search(self):
        writer = SearchResultWriter('test_result_air_book.csv')
        # (options_len) = self.select_depature_return()
        options_len = 7
        print options_len
        d = 0
        sum = 0
        while d < options_len:
            r = 0
            while r < options_len:
                values = self.provider.select_depature_return(d, r)
                writer.write(*values)
                sum = sum + 1
                p = 0
                while p < 2:
                    if p == 0:
                        prom_cod = promcodgent()
                        # print ("hello, this is a code"), prom_cod
                        values = self.provider.select_depature_return(d, r, prom_cod)
                        writer.write(*values)

                    else:
                        prom_cod = promcodgentinvalid()
                        values = self.provider.select_depature_return(d, r, prom_cod)
                        writer.write(*values)
                    p = p + 1
                    sum = sum + 1
                r = r + 1
            d = d + 1

        writer.close()
        print sum

    def test_00_booking_trip_normal(self):
        self.execute_search()
        pass
        # self.prom_cod()

    def test_01_check_search_page(self):
        d = 1
        r = 1
        status = 2017
        expectedresult = 2018
        # writecsv(d,r,status,expectedresult)
        # self.execute_search()
        pass


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(AirTripbooking)
    suite.sortTestMethodsUsing = None
    unittest.TextTestRunner(verbosity=2).run(suite)
