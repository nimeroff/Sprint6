import pytest
import allure
from utils.urlss import CUrls
from pages.home_page import HomePage
from pages.order_page import OrderPage
from locators import HomePageLocators
from utils.datas import OrderPageData as order_data


@allure.parent_suite('Parent_suite_Создание заказа')
class TestYaScooterOrderPage:

    @allure.suite('Suite_Полный путь создания заказа')
    @allure.feature('Фича_Полный путь создания заказа')
    @allure.title('Оформление заказа и переход на страницу с заказом')
    @allure.description('Проверка что при успешном оформлении заказа, заказ отображается на странице "Статус заказа" ')
    @pytest.mark.parametrize('data_set', ['data_set1', 'data_set2'])
    def test_order_page_create_order_and_go_order_status(self, driver, data_set):
        home_page = HomePage(driver)
        home_page.click_cookie_accept()
        home_page.click_top_order_button()
        order_page = OrderPage(driver)
        order_page.go_to_site(CUrls.order_page)
        order_page.fill_user_data(order_data.data_sets[data_set])
        order_page.go_next()
        order_page.fill_rent_data(order_data.data_sets[data_set])
        order_page.click_order()
        order_page.click_accept_order()
        assert order_page.check_order_status_window() ("Окно с информацией о заказе не появилось")


    @allure.suite('Suite_Полный путь создания заказа')
    @allure.feature('Фича_Полный путь создания заказа')
    @allure.title('Оформление заказа и переход на страницу с заказом')
    @allure.description('Проверка что при успешном оформлении заказа, заказ отображается на странице "Статус заказа" ')
    @pytest.mark.parametrize('data_set', ['data_set1', 'data_set2'])
    def test_order_page_create_order_and_go_order_status(self, driver, data_set):
        home_page = HomePage(driver)
        home_page.click_cookie_accept()
        home_page.click_bottom_order_button()
        order_page = OrderPage(driver)
        order_page.go_to_site(CUrls.order_page)
        order_page.fill_user_data(order_data.data_sets[data_set])
        order_page.go_next()
        order_page.fill_rent_data(order_data.data_sets[data_set])
        order_page.click_order()
        order_page.click_accept_order()
        assert order_page.check_order_status_window() ("Окно с информацией о заказе не появилось")