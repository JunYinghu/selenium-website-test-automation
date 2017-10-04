import csv
from selenium.webdriver.support.ui import Select

def selectdepaturereturn(self, d="none", r="none", prom_cod="none"):
    find_element_text = "Departure_option_xpath"
    session_name = "Booking"
    Departure_date_selected = Select(self.get_path(session_name, find_element_text))
    Departure_date = self.get_path(session_name, find_element_text)
    # Departure_date_options = Departure_date.find_elements_by_tag_name("option")
    Departure_date_options_len = len(Departure_date.find_elements_by_tag_name("option"))
    find_element_text = "Return_option_xpath"
    Return_date_selected = Select(self.get_path(session_name, find_element_text))
    Return_date = self.get_path(session_name, find_element_text)
    # Return_date_options = Return_date.find_elements_by_tag_name("option")
    find_element_text = "Promotional_code_xpath"
    input_prom_code = self.get_path(session_name, find_element_text)
    input_prom_code.clear()

    if d <> "none" and r <> "none":
        if prom_cod <> "none":
            Departure_date_selected.select_by_index(d)
            Return_date_selected.select_by_index(r)
            input_prom_code.send_keys(prom_cod)
            selected_d = 'This is your selected departure:  '
            selected_d_t = Departure_date_selected.first_selected_option.text
            print selected_d, d, selected_d_t
            selected_r = 'This is your selected return:  '
            selected_r_t = Return_date_selected.first_selected_option.text
            print selected_r, r, selected_r_t
            prom_r = 'This is your entered promotional code:  '
            prom_cod
            print prom_r, prom_cod
            self.get_search_result()
            return (Departure_date_options_len)

            with open("test_result_air_book.csv", "w") as fillin:
                fieldnames = ['Selected_Depature', 'Selected_Return', "Promotional"]
                writer = csv.DictWriter(fillin, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerow(
                    {"Selected_Depature": selected_d_t, "Selected_Return": selected_r_t, "Promotional": prom_cod})

        else:
            Departure_date_selected.select_by_index(d)
            Return_date_selected.select_by_index(r)
            selected_d = 'This is your selected Departure:  '
            selected_d_t = Departure_date_selected.first_selected_option.text
            print selected_d, d, selected_d_t
            selected_r = 'This is your selected Return:  '
            selected_r_t = Return_date_selected.first_selected_option.text
            print selected_r, r, selected_r_t
            self.get_search_result()

    # print ("invalid selection you provided")
    # self.driver.quit()
