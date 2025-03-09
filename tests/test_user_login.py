import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.locators import WebsiteLocators
import src.data as data

class TestConstructorNavigation:

    def login(self, driver, email, password):
        wait = WebDriverWait(driver, 60)

        # Вводим email для входа в поле
        email_input = wait.until(EC.presence_of_element_located(WebsiteLocators.EMAIL_INPUT_FORM))
        email_input.send_keys(email)

        # Вводим пароль для входа в поле
        password_input = wait.until(EC.presence_of_element_located(WebsiteLocators.PASSWORD_INPUT_FORM))
        password_input.send_keys(password)

        # Нажимаем кнопку "Войти"
        login_button = wait.until(EC.element_to_be_clickable(WebsiteLocators.LOGIN_BUTTON_FORM))
        login_button.click()

    def assert_order_button_is_visible(self, driver):
        wait = WebDriverWait(driver, 60)
        # Ожидаем, что кнопка "Оформить заказ" появится на главной странице
        make_order_button = wait.until(EC.presence_of_element_located(WebsiteLocators.MAKE_ORDER_BUTTON))
        assert make_order_button.is_displayed()

    def test_login_via_account_button(self, driver_chrome):
        driver = driver_chrome
        driver.get(data.main_page_url)

        # Ожидаем и кликаем кнопку "Войти в аккаунт"
        wait = WebDriverWait(driver, 60)
        account_button = wait.until(EC.element_to_be_clickable(WebsiteLocators.LOGIN_INTO_ACCOUNT_BUTTON))
        account_button.click()

        # Ожидаем переход на страницу входа
        wait.until(EC.url_to_be(data.login_page_url))

        self.login(driver, data.test_user_login, data.test_user_password)
        self.assert_order_button_is_visible(driver)

    def test_login_via_account_button_in_header(self, driver_chrome):
        driver = driver_chrome
        driver.get(data.main_page_url)

        # Ожидаем и кликаем кнопку "Личный Кабинет"
        wait = WebDriverWait(driver, 60)
        account_button = wait.until(EC.element_to_be_clickable(WebsiteLocators.ACCOUNT_BUTTON))
        account_button.click()

        # Ожидаем переход на страницу входа
        wait.until(EC.url_to_be(data.login_page_url))

        self.login(driver, data.test_user_login, data.test_user_password)
        self.assert_order_button_is_visible(driver)

    def test_login_via_registration_form(self, driver_chrome):
        driver = driver_chrome
        driver.get(data.register_page_url)

        wait = WebDriverWait(driver, 60)
        # Нажимаем кнопку-ссылку "Войти"
        login_text_link = wait.until(EC.element_to_be_clickable(WebsiteLocators.LOGIN_TEXT_LINK))
        login_text_link.click()

        # Ожидаем переход на страницу входа
        wait.until(EC.url_to_be(data.login_page_url))

        self.login(driver, data.test_user_login, data.test_user_password)
        self.assert_order_button_is_visible(driver)

    def test_login_via_forgot_password_form(self, driver_chrome):
        driver = driver_chrome
        driver.get(data.forgot_password_page_url)

        wait = WebDriverWait(driver, 60)
        login_text_link = wait.until(EC.element_to_be_clickable(WebsiteLocators.LOGIN_TEXT_LINK))
        login_text_link.click()

        # Ожидаем переход на страницу входа
        wait.until(EC.url_to_be(data.login_page_url))

        self.login(driver, data.test_user_login, data.test_user_password)
        self.assert_order_button_is_visible(driver)