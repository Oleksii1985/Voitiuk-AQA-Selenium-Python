import pytest
from selenium.webdriver import Chrome

from pages.dashboard import Dashboard


@pytest.fixture(scope="session")
def driver() -> Chrome:
    driver = Chrome("C:/Users/Admin/PycharmProjects/Voitiuk-AQA-Selenium-Python/drivers/chromedriver.exe")
    driver.maximize_window()
    driver.get("https://elektrovoz.com.ua/")
    yield driver

    driver.quit()


@pytest.fixture
def dashboard(driver) -> Dashboard:
    yield Dashboard(driver)
