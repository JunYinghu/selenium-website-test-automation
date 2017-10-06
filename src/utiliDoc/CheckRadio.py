import time


class CheckRadio(object):
    def __init__(self, driver, config):
        self.driver = driver
        self.config = config

    def selectradio(self, section, radio_select_n, radio_select_y):
        radioselectn = self.driver.find_element_by_id(self.config.get(section, radio_select_n))
        if radioselectn.is_selected():
            radioselecty = self.driver.find_element_by_id(
                self.config.get(section, radio_select_y))
            radioselecty.click()
            #radioselect_text = radioselecty.get_attribute("innerHTML")

        else:
            radioselectn.click()
