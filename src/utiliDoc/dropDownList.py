import time

from selenium.webdriver.support.ui import Select

from editGlobalSetting import editGlobalSetting


class dropDownList(object):
    def __init__(self, driver, config):
        self.driver = driver
        self.config = config
        self.editGlobalSetting = editGlobalSetting(driver, config)

    def getdopdownlist(self, section, id):
        option = self.driver.find_element_by_id(self.config.get(section, id))
        single_options_list = option.find_elements_by_tag_name('option')
        with open('resource/Time_zone_option.csv', 'w') as fout:
            fout.write('"","","","Index","Options_list"\n')
            for i, x in enumerate(single_options_list):
                fout.write('"","","","{}","{}"\n'.format(i, x.get_attribute("innerHTML").encode('utf-8')))
        # print "lksjdfklajsdlfjdsl",  len(single_options_list)
        return len(single_options_list)

    def getalldropdownList(self):
        section = "Board"
        language = "location_board_drop_id_language"
        language_optioLen = self.getdopdownlist(section, language)
        board_style = "location_board_drop_id_style"
        board_style_optioLen = self.getdopdownlist(section, board_style)
        timezone = "location_board_drop_id_timezone"
        timezone_optioLen = self.getdopdownlist(section, timezone)
        dateformat = "location_board_drop_id_dateformat"
        dateformat_optioLen = self.getdopdownlist(section, dateformat)
        return language_optioLen, board_style_optioLen, timezone_optioLen, dateformat_optioLen

    def selectsingledroplist(self, i, j, p, z):
        time.sleep(10)
        language = Select(self.driver.find_element_by_id(self.config.get('Board', 'location_board_drop_id_language')))
        language.select_by_index(i)
        board_style = Select(
            self.driver.find_element_by_id(self.config.get('Board', 'location_board_drop_id_style')))
        board_style.select_by_index(j)
        time_zone = Select(
            self.driver.find_element_by_id(self.config.get('Board', 'location_board_drop_id_timezone')))
        time_zone.select_by_index(p)
        dateformat = Select(
            self.driver.find_element_by_id(self.config.get('Board', 'location_board_drop_id_dateformat')))
        dateformat.select_by_index(z)
        if z == 7:
            input_date = self.driver.find_element_by_id(
                self.config.get('Board', 'location_board_drop_id_dateformat_input'))
            input_date.clear()
            input_date.send_keys("12/10/2017")
            # print "Custom 12/10/2017"
        submit = self.driver.find_element_by_name(self.config.get('Board', 'location_board_btn_name_submit'))
        submit.click()
        print i, j, p, z
        # selected_option_element = time_zone.first_selected_option
        # print selected_option_element.text

    def selectdropList(self):
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
                        self.editGlobalSetting.updateRadio()
                        self.selectsingledroplist(i, j, p, z)
                        run_case_count = run_case_count + 1
                        z = z + 1
                    p = p + 1
                j = j + 1
            i = i + 1
        print run_case_count