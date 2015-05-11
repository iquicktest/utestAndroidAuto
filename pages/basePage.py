from selenium.common.exceptions import NoSuchElementException

__author__ = 'xubin'


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver

    def is_element_exist(self, locators):
        try:
            self.driver.find_element(*locators)
        except NoSuchElementException:
            return False
        return True
