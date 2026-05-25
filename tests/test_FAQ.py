import pytest
import allure
from pages.home_page import HomePage
from utils.data import HomePageFAQ, HomePageFAQUESTION
from locators import HomePageLocators
import time

@allure.epic('Эпик_Upgrade Main page / ui usability')
@allure.parent_suite('Parent_suite_Домашняя страница')
@allure.suite('Suite_FAQ')
class TestFAQPage:
    @allure.feature('Фича_Аккордион с вопрос/ответ на Домашней страницы')
    @allure.story('Стори_При нажатии на вопрос в разделе "Вопросы о важном" раскрывается ответ.')
    @allure.title('При нажатии на вопрос раскрывается ответ ')
    @allure.description('Проверка что при нажатии на поле вопроса в блоке "Вопросы о важном", '
                        'данный вопрос раскрывается и текст в нем соответствует ТЗ')
    @pytest.mark.parametrize(
        ("answer_number, expected_answer"),
        [
            (0, HomePageFAQ.answer1),
            (1, HomePageFAQ.answer2),
            (2, HomePageFAQ.answer3),
            (3, HomePageFAQ.answer4),
            (4, HomePageFAQ.answer5),
            (5, HomePageFAQ.answer6),
            (6, HomePageFAQ.answer7),
            (7, HomePageFAQ.answer8),
        ]
    )
    def test_faq_click_first_question_show_answer(self, driver, answer_number, expected_answer):
        home_page = HomePage(driver)
        home_page.go_to_site()
        #home_page.scroll_to_element(HomePageLocators.QUESTION_TEMPLATE)
        home_page.click_accept_order()
        #home_page.find_element(HomePageLocators.QUESTION_TEMPLATE)
        home_locator = HomePageLocators.FAQ_question_button(question_number=answer_number)
        home_page.scroll_to_element(home_locator)
        button = home_page.find_elements(home_locator)

        #print("=== ИНФОРМАЦИЯ ОБ ЭЛЕМЕНТЕ ===")
        #print(f"Отображается: {button.is_displayed()}")
        #print(f"Текст (.text): '{button.text}'")
        #print(f"Атрибут value: '{button.get_attribute('value')}'")
        #print(f"Атрибут innerHTML: '{button.get_attribute('innerHTML')}'")
        #print(f"Атрибут outerHTML: '{button.get_attribute('outerHTML')}'")

        button.click()
        answer = home_page.find_elements(HomePageLocators.FAQ_answer(answer_number=answer_number))
        assert answer.is_displayed() and answer.text == expected_answer, 'Ответ на вопрос не совпадает с ожидаемым значением '