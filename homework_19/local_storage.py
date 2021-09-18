from selenium.webdriver.chrome.webdriver import WebDriver


class LocalStorage:
    def __init__(self, driver_local_storage: WebDriver):
        self.__driver_local_storage = driver_local_storage

    def save_and_return_local_storage(self):
        return self.__driver_local_storage.execute_script("return window.localStorage")
