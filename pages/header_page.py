import data
from locators.additional_locator import AdditionalLocator
from locators.header_page_locator import HeaderPageLocator
from locators.main_page_locators import MainPageLocator
from pages.base_page import BasePage


class HeaderPage(BasePage):
    def click_samokat_logo_and_move_to_main_page(self):
        self.get_url(data.MAIN_PAGE_URL+data.ORDER_PAGE_URL)
        self.click_on_element(HeaderPageLocator.SAMOKAT_LOGO)
        return self.get_text_from_element(MainPageLocator.SAMOKAT_WORD)

    def click_yandex_logo_and_move_to_dzen_page(self):
        self.get_url(data.MAIN_PAGE_URL + data.ORDER_PAGE_URL)
        self.click_on_element(HeaderPageLocator.YANDEX_LOGO)
        window_after = self.driver.window_handles[1]
        self.driver.switch_to.window(window_after)
        if self.find_element_with_wait(AdditionalLocator.DZEN_INSTALL_YANDEX).get_attribute('title') == 'Установить':
            self.click_on_element(AdditionalLocator.CLOSE_INSTALL_YANDEX)

        elf = self.find_element_with_wait(AdditionalLocator.DZEN_HEADER).get_attribute('id')

        return elf
