from selenium.webdriver.chrome.webdriver import WebDriver


class Cookie:
    def __init__(self, driver: WebDriver):
        self.__driver = driver

    def save_and_return_cookies(self):
        all_cookies = self.__driver.get_cookies()
        return all_cookies
