from homework_19.cookie import Cookie
from selenium.webdriver.chrome.webdriver import WebDriver


class Dashboard1(Cookie):
    def __init__(self, driver: WebDriver):
        super().__init__(driver)
