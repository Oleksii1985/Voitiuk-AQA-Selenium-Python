from selenium.webdriver.chrome.webdriver import WebDriver

from homework_19.local_storage import LocalStorage


class Dashboard2(LocalStorage):
    def __init__(self, driver: WebDriver):
        super().__init__(driver)
