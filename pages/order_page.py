from selenium.webdriver.common.by import By

import data
from locators.main_page_locators import MainPageLocator
from pages.base_page import BasePage


class OrderPage(BasePage):
    def enter_order_page(self, locator):
        self.get_url(data.MAIN_PAGE_URL)
        self.click_on_element(MainPageLocator.BUTTON_CONFIRM_COCKY)
        self.click_on_element(locator)
        current_url = self.driver.current_url
        return current_url

    def fill_out_order_form(self, name_locator, name, family_locator, family, address_locator, address, field_metro,
                            metro_locator, metro_name, phone_locator, phone, forward_locator, date_locator, date,
                            term_locator, duration_locator, duration_name, color_locator, color, comment_locator,
                            comment, order_button, confirm_button, confirm_status, filled_name, chosen_date):
        self.set_text_to_element(name_locator, name)
        self.set_text_to_element(family_locator, family)
        self.set_text_to_element(address_locator, address)
        self.click_on_element(field_metro)
        self.click_on_element(self.change_locator_data(metro_locator, metro_name))
        self.set_text_to_element(phone_locator, phone)
        self.click_on_element(forward_locator)
        self.set_text_to_element(date_locator, date)
        self.click_on_element(chosen_date)
        self.click_on_element(term_locator)
        self.click_on_element(self.change_locator_data(duration_locator, duration_name))
        self.click_on_element(self.change_locator_data(color_locator, color))
        self.set_text_to_element(comment_locator, comment)
        self.click_on_element(order_button)
        self.click_on_element(confirm_button)
        self.click_on_element(confirm_status)
        return self.get_text_from_element(filled_name)
