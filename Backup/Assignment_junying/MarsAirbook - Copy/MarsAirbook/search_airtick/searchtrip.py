from selenium.webdriver.support.select import Select

from MarsAirbook.search_result.returnsearchresult import ReturnResult
from MarsAirbook.utils.datediffcal import day_diff_cal
from MarsAirbook.utils.getpath import GetElementPath


class SearchTrip(GetElementPath):
    def __init__(self, config, driver):
        GetElementPath.__init__(self, config, driver)

    def select_departure_return(self, section_name, find_element_path):
        selected_option = Select(self.get_path(section_name, find_element_path))
        return selected_option

    def get_depature_return(self, current_depature_id=0, current_return_id=0, input_prom_cod="none"):
        sr = ReturnResult(self.config, self.driver)
        selected_d_t = "none"
        selected_r_t = "none"
        book_link = ''
        daydiff = 0
        status, expected = "none", "none"

        find_element_path = "Departure_option_xpath"
        section_name = "Booking"
        departure_selected = self.select_departure_return(section_name, find_element_path)
        find_element_path = "Return_option_xpath"
        return_selected = self.select_departure_return(section_name, find_element_path)

        find_element_text = "Promotional_code_xpath"
        input_prom_code = self.get_path(section_name, find_element_text)
        input_prom_code.clear()
        departure_selected.select_by_index(current_depature_id)
        return_selected.select_by_index(current_return_id)

        if input_prom_cod != "none":
            input_prom_code.send_keys(input_prom_cod)
            # get current selected option 's text
            current_depature = departure_selected.first_selected_option.text
            # get current selected option 's text
            current_return = return_selected.first_selected_option.text
            daydiff = day_diff_cal(current_depature_id, current_return_id)
            test_case_screen, expected, status = sr.get_search_result(daydiff, input_prom_cod, current_depature_id,
                                                                      current_return_id)
        else:
            current_depature = departure_selected.first_selected_option.text
            current_return = return_selected.first_selected_option.text
            daydiff = day_diff_cal(current_depature_id, current_return_id)
            test_case_screen, expected, status = sr.get_search_result(daydiff, input_prom_cod, current_depature_id,
                                                                      current_return_id)
        return (
            current_depature_id, current_return_id, current_depature, current_return, input_prom_cod, daydiff,
            test_case_screen, expected,
            status)
