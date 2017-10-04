class GetElementPath(object):
    def __init__(self, config, driver):
        self.config = config
        self.driver = driver

    def get_path(self, section_name, find_element):
        get_element = self.config.get(section_name, find_element)
        get_element_local = self.driver.find_element_by_xpath(get_element)
        return get_element_local
