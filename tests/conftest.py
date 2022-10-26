import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from pages.google_page import GooglePage

URL_GOOGLE = 'https://www.google.com/'


@pytest.fixture()
def driver():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture()
def open_google(driver):
    driver.get(URL_GOOGLE)
    return GooglePage(driver)
