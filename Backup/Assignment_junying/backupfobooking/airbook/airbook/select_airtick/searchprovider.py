from selenium.webdriver.support.select import Select
from airbook.search_result.returnsearchresult import ReturnResult
from airbook.utils.date_cal import datecau


class SearchProvider(object):
    def __init__(self, config, driver):
        self.config = config
        self.driver = driver
    def get_path(self, section_name, find_element):
        get_element = self.config.get(section_name, find_element)
        get_element_local = self.driver.find_element_by_xpath(get_element)
        return (get_element_local)

    def select_departure_return(self, section_name, find_element_path):
         selected_option = Select(self.get_path(section_name, find_element_path))
         return (selected_option)

    def select_depature_return(self, d=0, r=0, prom_cod="none"):
        sr = ReturnResult(self.config, self.driver)
        selected_d_t = "none"
        selected_r_t = "none"
        diffdate = 0
        status, expected = "none", "none"

        find_element_path = "Departure_option_xpath"
        section_name = "Booking"
        departure_selected = self.select_departure_return(section_name, find_element_path)
        find_element_path = "Return_option_xpath"
        return_selected = self.select_departure_return(section_name, find_element_path)

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
            test_case_screen, expected, status = sr.get_search_result(diffdate, prom_cod, d, r)
        else:

            depature_current_selected = departure_selected.first_selected_option.text  # get current selected option 's text
            return_current_selected = return_selected.first_selected_option.text  # get current selected option 's text
            diffdate = datecau(d, r)
            test_case_screen, expected, status = sr.get_search_result(diffdate, prom_cod, d, r)
        return (
            d, r, depature_current_selected, return_current_selected, prom_cod, diffdate, test_case_screen, expected,
            status)
