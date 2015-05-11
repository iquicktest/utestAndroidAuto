from appium import webdriver

__author__ = 'xubin'

desired_caps = {
    'appium-version': "1.0",
    'platformName': 'android',
    'platformVersion': '4.4.2',
    'deviceName': 'QAnote',
    'app': '/Users/xubin/Desktop/com.wholefoods.wholefoodsmarket.apk'
}


def before_scenario(context, scenario):
    context.driver = webdriver.Remote('http://127.0.0.1:4722/wd/hub', desired_caps)
    context.driver.implicitly_wait(60)


def after_scenario(context, scenario):
    context.driver.quit()