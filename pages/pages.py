from basePage import BasePage
from objectRepository.locators import *

__author__ = 'xubin'


class HomePage(BasePage):
    def search_content(self, content):
        self.driver.find_element(*HomePageLocators.TXT_SEARCH).send_keys(content)

    def do_search(self):
        self.driver.find_element(*HomePageLocators.IMG_SEARCH).click()
        return ResultPage(self.driver)


class ResultPage(BasePage):
    pass