from selenium.webdriver.chrome.webdriver import WebDriver


class BasePage:
    def __init__(self, driver: WebDriver):
        self.__driver = driver
        self._all_cookies = self.__driver.get_cookies()
        self._local_storage = self.__driver.execute_script("return window.localStorage")
