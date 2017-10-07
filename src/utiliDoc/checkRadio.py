class checkRadio(object):
    def __init__(self, driver, config):
        self.driver = driver
        self.config = config

    # this fun is to indentify the current radio button status and toggle it
    def selectradio(self, section, radio_select_n, radio_select_y):
        radioselectn = self.driver.find_element_by_id(self.config.get(section, radio_select_n))
        if radioselectn.is_selected():
            radioselect = self.driver.find_element_by_id(
                self.config.get(section, radio_select_y))
            radioselect.click()
            # radioselect_text = radioselecty.get_attribute("innerHTML")

        else:
            radioselectn.click()
