from selenium.webdriver.chrome.webdriver import WebDriver

from homework_19.cookie import Cookie
from homework_19.local_storage import LocalStorage


class BasePage:
    def __init__(self, driver: WebDriver, driver_cookie: WebDriver, driver_local_storage: WebDriver):
        self.__driver = driver
        self.__cookie = Cookie(driver_cookie)
        self.__local_storage = LocalStorage(driver_local_storage)

    @property
    def cookies(self) -> Cookie:
        return self.__cookie

    @property
    def local_storage(self) -> LocalStorage:
        return self.__local_storage
