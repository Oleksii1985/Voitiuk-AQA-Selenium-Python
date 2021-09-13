from selenium.webdriver.chrome.webdriver import WebDriver


class LocalStorage:
    def __init__(self, driver: WebDriver):
        self.__driver = driver

    def save_and_return_local_storage(self):
        local_storage = self.__driver.execute_script("return window.localStorage")
        return local_storage
