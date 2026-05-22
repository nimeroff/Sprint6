import allure
from pages.base_page import BasePage
from locators import BasePageLocators
from selenium.webdriver.support.wait import WebDriverWait
from locators import HomePageLocators as Locators
from selenium.webdriver.support import expected_conditions as EC


class HomePage(BasePage):
    @allure.step('Нажать на кнопку заказа вверху страницы')
    def click_top_order_button(self):
        return self.find_element(Locators.ORDER_BUTTON_HEADERS).click()

    @allure.step('Нажать на кнопку заказа внизу страницы')
    def click_bottom_order_button(self):
        return self.find_element(Locators.ORDER_BUTTON_MIDDLE).click()

    @allure.step('Нажать на вопрос в FAQ')
    def click_faq_question(self, question_number: int):
        elems = self.find_element(Locators.FAQ_BUTTONS, 10)
        return elems[question_number].click()
    
    @allure.step('Переключиться на вкладку браузера')
    def switch_window(self, window_number: int = 1):
        return self.driver.switch_to.window(self.driver.window_handles[window_number])

    def wait_url_until_not_about_blank(self, time=10):
        return WebDriverWait(self.driver, time).until_not(EC.url_to_be('about:blank'))
    
    @allure.step('Перейти на страницу яндекса')
    def click_yandex_button(self):
        return self.find_element(BasePageLocators.YANDEX_LOGO).click()

    @allure.step('Клик по логотипу Самоката')
    def click_scooter_logo(self):
        #self.click_to_element(BasePageLocators.SAMOKAT_LOGO)
        self.find_element(BasePageLocators.SAMOKAT_LOGO).click()
        return self.current_url

    @allure.step('Переход по логотипу Яндекса')
    def go_to_yandex_from_logo(self):
        #self.click_to_element(BasePageLocators.YANDEX_LOGO)
        self.find_element(BasePageLocators.YANDEX_LOGO).click()
        self.switch_to_tab(1)

    @allure.step('Принять куки')
    def click_cookie_accept(self):
        return self.find_element(BasePageLocators.COOKIE_BUTTON).click()
    
    @allure.step('Скролл до элемента с локатором {locator}')
    def scroll_to_element(self, locator):
        element = self.wait_for_element_visible(locator)
        self.driver.execute_script(
            "arguments[0].scrollIntoView(true);", element)
        
    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                      message=f"Can't find element by locator {locator}")
    