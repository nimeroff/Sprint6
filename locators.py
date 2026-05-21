from selenium.webdriver.common.by import By


class BasePageLocators:
    COOKIE_BUTTON = [By.XPATH, ".//button[text()='да все привыкли']"]
    YANDEX_LOGO = [By. CLASS_NAME, 'Header_LogoYandex__3TSOI' ]
    SAMOKAT_LOGO = [By. CLASS_NAME, 'Header_LogoScooter__3lsAR']
    

class HomePageLocators:
    ORDER_BUTTON_HEADERS = [By. CLASS_NAME, 'Button_Button__ra12g']
    ORDER_STATUS_BUTTON = [By. CLASS_NAME, 'Header_Link__1TAG7']
    QUESTION_TEMPLATE = [By. CLASS_NAME, 'Home_SubHeader__zwi_E']
    ANSWER_TEMPLATE = [By.CLASS_NAME, 'Home_FAQ__3uVm4']
    ORDER_BUTTON_MIDDLE = [By. CLASS_NAME, 'Button_Button__ra12g Button_Middle__1CSJM']

    @staticmethod
    def FAQ_question_button(question_number): # возвращает локатор кнопки с вопросом FAQ
        return [By.XPATH, f".//div[@class='accordion__button' and @id='accordion__heading-{question_number}']"]

    @staticmethod
    def FAQ_answer(answer_number): # возвращает локатор дива с ответом FAQ
        return [By.XPATH, f".//div[@class='accordion__panel' and @id='accordion__panel-{answer_number}']/p"]


class OrderPageLocators:
    FIRST_NAME_INPUT = [By.XPATH, ".//input[contains(@placeholder,'Имя')]"]
    LAST_NAME_INPUT = [By.XPATH, ".//input[contains(@placeholder,'Фамилия')]"]
    ADDRESS_INPUT = [By.XPATH, ".//input[contains(@placeholder,'Адрес')]"]
    SUBWAY_FIELD = [By.XPATH, ".//input[contains(@placeholder,'метро')]"] 

    

    TELEPHONE_NUMBER_FIELD = [By.XPATH, ".//input[contains(@placeholder,'Телефон')]"]

    NEXT_BUTTON = [By.XPATH, ".//button[text()='Далее']"]
    DATE_FIELD = [By.XPATH, ".//input[contains(@placeholder,'Когда')]"]
    RENTAL_PERIOD_FIELD = [By.XPATH, ".//span[@class='Dropdown-arrow']"]
    RENTAL_PERIOD_LIST = [By.XPATH, ".//div[@class='Dropdown-option']"]
    COLOR_CHECKBOXES = [By.XPATH, ".//div[contains(text(),'Цвет')]/parent::div//input"]
    COMMENT_INPUT = [By.XPATH, ".//input[contains(@placeholder,'Комментарий для курьера')]"]
    ORDER_BUTTON = [By.XPATH, ".//button[text()='Назад']/parent::div/button[text()='Заказать']"]
    YES_BUTTON = [By.XPATH, ".//button[text()='Да']"]
    ORDER_COMPLETED_INFO = [By.XPATH, ".//div[contains(text(),'Номер заказа')]"]
    SHOW_STATUS_BUTTON = [By.XPATH, ".//button[text()='Посмотреть статус']"]


class YaScooterTrackPageLocator:
    MAIN_ORDER_NUMBER_FIELD = [By.XPATH, ".//input[@placeholder='']"]

