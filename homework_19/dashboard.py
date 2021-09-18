from selenium.webdriver.chrome.webdriver import WebDriver

from .base_page import BasePage


class Dashboard(BasePage):
    def __init__(self, driver: WebDriver):
        super().__init__(driver, driver, driver)
