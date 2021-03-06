from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self._driver = driver
        self.__web_driver_wait = WebDriverWait(self._driver, 5)

    def _wait_until_element_appears(self, locator) -> WebElement:
        return self.__web_driver_wait.until(EC.presence_of_element_located(locator))
