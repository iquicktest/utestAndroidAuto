from selenium.webdriver.common.by import By

__author__ = 'xubin'


class BaseLocators(object):
    pass

class HomePageLocators(BaseLocators):
    TXT_SEARCH = (By.ID, 'com.wholefoods.wholefoodsmarket:id/etHomeSearch')
    IMG_SEARCH = (By.ID, 'com.wholefoods.wholefoodsmarket:id/imgSearch')


class SearchResultsPageLocators(BaseLocators):
    LAB_COFFEE = (By.NAME,'Coffee-Nog Shakes')