from selenium.webdriver.chrome.webdriver import WebDriver

from homework_19.base_page import BasePage


class Dashboard(BasePage):
    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def save_and_return_cookies(self):
        return self._all_cookies

    def save_and_return_local_storage(self):
        return self._local_storage
