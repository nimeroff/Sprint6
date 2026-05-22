import pytest
import allure
from pages.home_page import HomePage
from utils.data import HomePageFAQ
from locators import HomePageLocators


#@allure.epic('Эпик_Upgrade Main page / ui usability')
#@allure.parent_suite('Parent_suite_Домашняя страница')
@allure.suite('Suite_FAQ')
class TestFAQPage:
    @allure.feature('Фича_Аккордион с вопрос/ответ на Домашней страницы')
    @allure.story('Стори_При нажатии на вопрос в разделе "Вопросы о важном" раскрывается ответ.')
    @allure.title('При нажатии на вопрос раскрывается ответ ')
    @allure.description('Проверка что при нажатии на поле вопроса в блоке "Вопросы о важном", '
                        'данный вопрос раскрывается и текст в нем соответствует ТЗ')
    @pytest.mark.parametrize(
        ("question,answer,expected_answer"),
        [
            (0, 0, HomePageFAQ.answer1),
            (1, 1, HomePageFAQ.answer2),
            (2, 2, HomePageFAQ.answer3),
            (3, 3, HomePageFAQ.answer4),
            (4, 4, HomePageFAQ.answer5),
            (5, 5, HomePageFAQ.answer6),
            (6, 6, HomePageFAQ.answer7),
            (7, 7, HomePageFAQ.answer8),
        ]
    )
    def test_faq_click_first_question_show_answer(self, driver, question, answer, expected_answer):
        home_page = HomePage(driver)
        home_page.go_to_site()
        #home_page.scroll_to_element(HomePageLocators.QUESTION_TEMPLATE)
        home_page.click_cookie_accept()
        home_page.find_element(HomePageLocators.QUESTION_TEMPLATE)
        home_page.click_faq_question(question_number=question)
        answer = home_page.find_element(HomePageLocators.FAQ_answer(answer_number=answer))

        assert answer.is_displayed() and answer.text == expected_answer, 'Ответ на вопрос не совпадает с ожидаемым значением '