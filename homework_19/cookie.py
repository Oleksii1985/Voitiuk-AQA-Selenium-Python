from selenium.webdriver.chrome.webdriver import WebDriver


class Cookie:
    def __init__(self, driver_cookie: WebDriver):
        self.__driver_cookie = driver_cookie

    def save_and_return_cookies(self):
        return self.__driver_cookie.get_cookies()
