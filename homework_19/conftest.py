import pytest
from selenium.webdriver import Chrome

from homework_19.dashboard2 import Dashboard2
from homework_19.dashboard1 import Dashboard1


@pytest.fixture(scope="session")
def driver() -> Chrome:
    # PATH should be yours for driver
    driver = Chrome("C:/Users/Admin/PycharmProjects/Voitiuk-AQA-Selenium-Python/drivers/chromedriver.exe")
    driver.maximize_window()
    driver.get("https://elektrovoz.com.ua/")

    yield driver

    driver.quit()


@pytest.fixture
def dashboard1(driver):
    yield Dashboard1(driver)


@pytest.fixture
def dashboard2(driver):
    yield Dashboard2(driver)
