from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from locators.google_page_locators import GooglePageLocators
from pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

from pages.searching_page import SearchingPage


class GooglePage(BasePage):

    locators = GooglePageLocators

    def get_search(self, text):
        try:
            search_input = WebDriverWait(self.driver, 15)\
                .until(EC.visibility_of_element_located(self.locators.SEARCH_INPUT))
            search_input.send_keys(text)
            search_input.send_keys(Keys.ENTER)
        except TimeoutException:
            assert False, 'Нет поля для ввода или неверный локатор'

    def click_on_string_in_search_result(self, link):
        link_locator = (By.PARTIAL_LINK_TEXT, link.lower())
        try:
            WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located(link_locator)).click()
        except TimeoutException:
            assert False, 'Нет ссылки в результатах поиска'

    def search_and_open_searching_page(self, link):
        self.get_search(link)
        self.click_on_string_in_search_result(link)
        return SearchingPage(self.driver)
