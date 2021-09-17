from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from pages.base_page import BasePage


class Dashboard(BasePage):
    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def choose_product_list(self, name) -> None:
        locator = (By.XPATH, "//input[@placeholder='Что вы ищете?']")
        element = self._wait_until_element_appears(locator)
        element.send_keys(f"{name}")
        element.send_keys(Keys.ENTER)

    def click_product(self) -> None:
        locator = (By.XPATH, "//div[@class='product_preview__name']/a[@data-product='9948']")
        element = self._wait_until_element_appears(locator)
        element.click()
