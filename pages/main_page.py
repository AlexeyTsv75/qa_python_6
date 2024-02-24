import data
from locators.main_page_locators import MainPageLocator
from pages.base_page import BasePage


class MainPage(BasePage):

    def click_to_question_and_get_answer_text(self, num):
        self.get_url(data.MAIN_PAGE_URL)
        self.click_on_element(MainPageLocator.BUTTON_CONFIRM_COCKY)
        self.click_on_element(self.change_locator_data(MainPageLocator.QUESTION_LOCATOR, num))
        return self.get_text_from_element(self.change_locator_data(MainPageLocator.ANSWER_LOCATOR, num))
