import allure
from utils.urls import Urls
from pages.home_page import HomePage


@allure.suite('Тестирование переходов с логотипа')
class TestHomePage:

    @allure.title('При нажатии на лого "Яндекс" происходит редирект на страницу "ЯндексДзен"')
    @allure.description('Проверка что, на домашней странице в header по кнопке "Яндекс" '
                        'происходит корреткный редирект на страницу "ЯндексДзен".')
    def test_click_yandex_button_go_to_yandex(self, driver):
        home_page = HomePage(driver)
        home_page.go_to_site()
        home_page.click_cookie_accept()
        home_page.click_yandex_button()
        home_page.switch_window(1)
        home_page.wait_url_until_not_about_blank()
        current_url = home_page.current_url()
        assert Urls.dzen_page in current_url

    @allure.title('Проверка перехода по логотипу Самоката')
    @allure.description('Переход на главную страницу Самоката '
                        'при клике на слово Самокат в логотипе')
    def test_redirect_scooter_logo(self, driver):
        home_page = HomePage(driver)
        home_page.go_to_site()
        home_page.click_cookie_accept()
        home_page.click_scooter_logo()
        home_page.wait_url_until_not_about_blank()
        current_url = home_page.current_url()
        assert Urls.main_page in current_url