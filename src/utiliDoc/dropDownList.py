import time

from selenium.webdriver.support.ui import Select

from editRadio import editRadio


class dropDownList(object):
    def __init__(self, driver, config):
        self.driver = driver
        self.config = config
        self.editGlobalRadio = editRadio(driver, config)

    # get single dropdown list options and save option text into a csv file
    # return length of dropdown list
    def getdropdownlist(self, section, id):
        option = self.driver.find_element_by_id(self.config.get(section, id))
        single_options_list = option.find_elements_by_tag_name('option')

        # save option text into a csv file
        with open('resource/dropdown_' + id + '.csv', 'w') as fout:
            fout.write('"","","","Index","Options_list"\n')
            for i, x in enumerate(single_options_list):
                fout.write('"","","","{}","{}"\n'.format(i, x.get_attribute("innerHTML").encode('utf-8')))

        # Return length of dropdown list
        return len(single_options_list)

    # get all dropdown list
    # return length for each of them
    def getalldropdownList(self):
        section = "Board"
        language = "location_board_drop_id_language"
        language_optioLen = self.getdropdownlist(section, language)
        board_style = "location_board_drop_id_style"
        board_style_optioLen = self.getdropdownlist(section, board_style)
        timezone = "location_board_drop_id_timezone"
        timezone_optioLen = self.getdropdownlist(section, timezone)
        dateformat = "location_board_drop_id_dateformat"
        dateformat_optioLen = self.getdropdownlist(section, dateformat)
        return language_optioLen, board_style_optioLen, timezone_optioLen, dateformat_optioLen

    # get index and select the option
    # then save the changes
    def selectoption(self, i, j, p, z):
        time.sleep(10)
        language = Select(self.driver.find_element_by_id(self.config.get('Board', 'location_board_drop_id_language')))
        language.select_by_index(i)
        language_elem = language.first_selected_option
        board_style = Select(
            self.driver.find_element_by_id(self.config.get('Board', 'location_board_drop_id_style')))
        board_style.select_by_index(j)
        board_style_elem = board_style.first_selected_option
        time_zone = Select(
            self.driver.find_element_by_id(self.config.get('Board', 'location_board_drop_id_timezone')))
        time_zone.select_by_index(p)
        time_zone_elem = time_zone.first_selected_option
        dateformat = Select(
            self.driver.find_element_by_id(self.config.get('Board', 'location_board_drop_id_dateformat')))
        dateformat.select_by_index(z)
        dateformat_elem = dateformat.first_selected_option
        if z == 7:
            input_date = self.driver.find_element_by_id(
                self.config.get('Board', 'location_board_drop_id_dateformat_input'))
            input_date.clear()
            input_date.send_keys("12/10/2017")

            print i, language_elem.text, j, board_style_elem.text, p, time_zone_elem.text, z, 'Custom 12/10/2017'
        else:
            print i, language_elem.text, j, board_style_elem.text, p, time_zone_elem.text, z, dateformat_elem.text
        submit = self.driver.find_element_by_name(self.config.get('Board', 'location_board_btn_name_submit'))
        submit.click()

    # making a  'While' loop and pass the index to fun selectoption
    # perform fun selectoption and updateRadio
    def dropdownloopselect(self):
        language_optioLen, board_style_optioLen, timezone_optioLen, dateformat_optioLen = self.getalldropdownList()
        i = 0
        run_case_count = 0
        while i < language_optioLen:
            j = 0
            while j < board_style_optioLen:
                p = 0
                while p < timezone_optioLen:
                    z = 0
                    while z < dateformat_optioLen:
                        self.editGlobalRadio.updateRadio()
                        self.selectoption(i, j, p, z)
                        run_case_count = run_case_count + 1
                        print run_case_count
                        z = z + 1
                    p = p + 1
                j = j + 1
            i = i + 1
