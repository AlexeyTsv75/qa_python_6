import pytest
import data
from pages.order_page import OrderPage
from locators.order_page_locators import OrderPageLocator


class TestOrderPage:
    @pytest.mark.parametrize('locator', [OrderPageLocator.UPPER_ORDER_BUTTON, OrderPageLocator.LOWER_ORDER_BUTTON])
    def test_order_buttons_click(self, driver, locator):
        order_page = OrderPage(driver)
        assert (order_page.enter_order_page(locator) == data.MAIN_PAGE_URL
                + data.ORDER_PAGE_URL)

    @pytest.mark.parametrize('name, family, address, metro_name, phone, date, duration_name, color, comment',
                             [
                                 [data.UserSet.NAME_1, data.UserSet.FAMILY_1, data.UserSet.ADDRESS_1,
                                  data.UserSet.METRO_1, data.UserSet.PHONE_1, data.UserSet.DATE_1,
                                  data.UserSet.TERM_1, data.UserSet.COLOR_1, data.UserSet.COMMENT_1],
                                 [data.UserSet.NAME_2, data.UserSet.FAMILY_2, data.UserSet.ADDRESS_2,
                                  data.UserSet.METRO_2, data.UserSet.PHONE_2, data.UserSet.DATE_2,
                                  data.UserSet.TERM_2, data.UserSet.COLOR_2, data.UserSet.COMMENT_2]
                             ]
                             )
    def test_order_flow_success(self, driver, name, family, address, metro_name, phone, date, duration_name, color,
                                comment):
        order_page = OrderPage(driver)
        order_page.get_url(order_page.enter_order_page(OrderPageLocator.UPPER_ORDER_BUTTON))
        result = order_page.fill_out_order_form(name, family, address, metro_name, phone, date, duration_name, color,
                                                comment)
        expected_result = name
        assert order_page.check_answer(result, expected_result)
