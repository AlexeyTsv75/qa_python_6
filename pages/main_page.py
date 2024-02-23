import data
from locators.main_page_locators import MainPageLocator
from pages.base_page import BasePage



class MainPage(BasePage):

    def click_to_question_and_get_answer_text(self, locator_q, locator_a, num):
        self.get_url(data.MAIN_PAGE_URL)
        self.click_on_element(MainPageLocator.BUTTON_CONFIRM_COCKY)
        self.click_on_element(self.change_locator_data(locator_q, num))
        return self.get_text_from_element(self.change_locator_data(locator_a, num))

    def check_answer(self, result, expected):
        return result == expected
