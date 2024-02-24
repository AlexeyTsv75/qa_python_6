import data
from pages.header_page import HeaderPage


class TestHeaderPage:
    def test_click_samokat_logo_move_to_main_page(self, driver):
        header_page = HeaderPage(driver)
        result = header_page.click_samokat_logo_and_move_to_main_page()
        assert data.SAMOKAT in result

    def test_click_yandex_logo_and_move_to_dzen_page(self, driver):
        header_page = HeaderPage(driver)
        result = header_page.click_yandex_logo_and_move_to_dzen_page()
        expected_result = data.DZEN_HEADER
        assert header_page.check_answer(result, expected_result)
