import re
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pages.base_page import BasePage
from locators import OrderPageLocators as Locators
import allure


class OrderPage(BasePage):
    @allure.step('Ввод имени')
    def input_last_name(self, first_name: str):
        return self.find_element(Locators.FIRST_NAME_INPUT).send_keys(first_name)

    @allure.step('Ввод фамилии')
    def input_first_name(self, last_name: str):
        return self.find_element(Locators.LAST_NAME_INPUT).send_keys(last_name)

    @allure.step('Ввод адреса')
    def input_address(self, address: str):
        return self.find_element(Locators.ADDRESS_INPUT).send_keys(address)

    @allure.step('Выбор метро')
    def choose_subway(self, subway_name: str):
        self.find_element(Locators.SUBWAY_FIELD).click()
        return self.find_element(Locators.SUBWAY_HINT_BUTTON(subway_name)).click()

    @allure.step('Ввод номера телефона')
    def input_telephone_number(self, telephone_number: str):
        return self.find_element(Locators.TELEPHONE_NUMBER_FIELD).send_keys(telephone_number)

    @allure.step('Перейти на следующий этап заказа')
    def go_next(self):
        return self.find_element(Locators.NEXT_BUTTON).click()

    @allure.step('Ввод даты')
    def input_date(self, date: str):
        date_input = self.find_element(locator=Locators.DATE_FIELD)
        date_input.click()
        date_input.clear()
        date_input.send_keys(date)
        date_input.send_keys(Keys.ENTER)


    @allure.step('Выбор периода аренды')
    def choose_rental_period(self, option: int):
        choose_click= self.find_element(Locators.RENTAL_PERIOD_FIELD).click()
        return self.find_element([By.XPATH, f".//div[@class='Dropdown-option' and text()='{option}']"]).click()

    @allure.step('Выбор цвета')
    def choose_color(self, option: str):
        return self.find_elements([By.XPATH, f".//label[@for='{option}']"]).click()

    @allure.step('Комментарий для курьера')
    def input_comment(self, comment_text):
        return self.find_element(Locators.COMMENT_INPUT).send_keys(comment_text)

    @allure.step('Нажать "Заказать"')
    def click_order(self):
        order_button =  self.find_element(Locators.ORDER_BUTTON)
        #self.scroll_to_element(Locators.ORDER_BUTTON)
        return order_button.click()

    @allure.step('Подтвердить заказ')
    def click_accept_order(self):
        return self.find_element(Locators.YES_BUTTON).click()


    @allure.step('Заполнить данные на этапе "Для кого самокат"')
    def fill_user_data(self, data_set: dict):
        self.input_first_name(data_set['first_name'])
        self.input_last_name(data_set['last_name'])
        self.input_address(data_set['address'])
        self.choose_subway(data_set['subway_name'])
        self.input_telephone_number(data_set['telepthone_number'])

    @allure.step('Заполнить данные на этапе "Про аренду"')
    def fill_rent_data(self, data_set: dict):
        self.input_date(data_set['date'])
        self.choose_rental_period(data_set['rental_period'])
        for option in data_set['color']:
            self.choose_color(option)
        self.input_comment(data_set['comment_for_courier'])

    @allure.step('Проверяем наличие окна с информацией о заказе')
    def check_order_status_window(self):
        try:
            self.wait_for_element_visible(Locators.STATUS_WINDOW)
            return True
        except:
            return False

    @allure.step('Скролл до элемента с локатором {locator}')
    def scroll_to_element(self, locator):
        element = self.wait_for_element_visible(locator)
        self.driver.execute_script(
            "arguments[0].scrollIntoView(true);", element)