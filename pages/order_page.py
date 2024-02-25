import data
from locators.main_page_locators import MainPageLocator
from locators.order_page_locators import OrderPageLocator
from pages.base_page import BasePage


class OrderPage(BasePage):
    def enter_order_page(self, locator):
        self.get_url(data.MAIN_PAGE_URL)
        self.click_on_element(MainPageLocator.BUTTON_CONFIRM_COCKY)
        self.click_on_element(locator)
        current_url = self.driver.current_url
        return current_url

    def fill_out_order_form(self, name, family, address, metro_name, phone, date, duration_name, color, comment):
        self.set_text_to_element(OrderPageLocator.FIELD_NAME, name)
        self.set_text_to_element(OrderPageLocator.FIELD_FAMILY, family)
        self.set_text_to_element(OrderPageLocator.FIELD_ADDRESS, address)
        self.click_on_element(OrderPageLocator.FIELD_METRO)
        self.click_on_element(self.change_locator_data(OrderPageLocator.METRO_NAME, metro_name))
        self.set_text_to_element(OrderPageLocator.FIELD_PHONE, phone)
        self.click_on_element(OrderPageLocator.FORWARD_BUTTON)
        self.set_text_to_element(OrderPageLocator.FIELD_DATE, date)
        self.click_on_element(OrderPageLocator.CHOSEN_DATE)
        self.click_on_element(OrderPageLocator.FIELD_TERM)
        self.click_on_element(self.change_locator_data(OrderPageLocator.DURATION_LIST, duration_name))
        self.click_on_element(self.change_locator_data(OrderPageLocator.COLOR_CHOOSE, color))
        self.set_text_to_element(OrderPageLocator.FIELD_COMMENT, comment)
        self.click_on_element(OrderPageLocator.LIST_ORDER_BUTTON)
        self.click_on_element(OrderPageLocator.ORDER_CONFIRMATION_BUTTON)
        self.click_on_element(OrderPageLocator.CHECK_STATUS_BUTTON)
        return self.get_text_from_element(OrderPageLocator.FILLED_NAME)
