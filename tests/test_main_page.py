import pytest
from pages.main_page import MainPage
from locators.main_page_locators import MainPageLocator
from data import FaqAnswers


class TestMainPage:

    @pytest.mark.parametrize("x_num, expected_result",
                             [(0, FaqAnswers.FAQ_ANSWER_0),
                              (1, FaqAnswers.FAQ_ANSWER_1),
                              (2, FaqAnswers.FAQ_ANSWER_2),
                              (3, FaqAnswers.FAQ_ANSWER_3),
                              (4, FaqAnswers.FAQ_ANSWER_4),
                              (5, FaqAnswers.FAQ_ANSWER_5),
                              (6, FaqAnswers.FAQ_ANSWER_6),
                              (7, FaqAnswers.FAQ_ANSWER_7)
                              ]
                             )
    def test_questions(self, driver, x_num, expected_result):
        main_page = MainPage(driver)
        result = main_page.click_to_question_and_get_answer_text(MainPageLocator.QUESTION_LOCATOR,
                                                                 MainPageLocator.ANSWER_LOCATOR, x_num)
        assert main_page.check_answer(result, expected_result)
