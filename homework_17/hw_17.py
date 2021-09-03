"""
Создать тест в котором происходит инициализация драйвера. Перейдите на любой выбранный вами ресурс.
Нажмите на копку либо введите текст в поле ввода.
В этом же тесте попробуйте реализовать скролинг в окне где есть скрол бар.
"""
import time

from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement


def test_check_input_and_scroll():
    # in chrome_driver_path should be your XPath to chromedriver!!!
    chrome_driver_path = Chrome("C:/Users/Admin/PycharmProjects/Voitiuk-AQA-Selenium-Python/drivers/chromedriver.exe")

    search_input_field_locator = "//input[@placeholder='Что вы ищете?']"
    result_link_locator = "//div[@class='product_preview__name']/a[@data-product='9948']"

    chrome_driver_path.get("https://elektrovoz.com.ua/")
    chrome_driver_path.maximize_window()

    search_input_field: WebElement = chrome_driver_path.find_element_by_xpath(search_input_field_locator)
    search_input_field.send_keys("розетки")
    time.sleep(3)
    search_input_field.send_keys(Keys.ENTER)
    time.sleep(3)
    chrome_driver_path.execute_script("window.scrollTo(0, 600)")
    time.sleep(3)
    first_link: WebElement = chrome_driver_path.find_element_by_xpath(result_link_locator)
    first_link.click()
    time.sleep(3)

    chrome_driver_path.quit()
