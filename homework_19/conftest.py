import pytest
from selenium.webdriver import Chrome

from homework_19.dashboard import Dashboard


@pytest.fixture(scope="session")
def driver() -> Chrome:
    driver = Chrome("../drivers/chromedriver.exe")
    driver.maximize_window()
    driver.get("https://elektrovoz.com.ua/")

    yield driver

    driver.quit()


@pytest.fixture
def dashboard(driver):
    yield Dashboard(driver)
