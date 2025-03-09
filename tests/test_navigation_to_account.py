import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.locators import WebsiteLocators
import src.data as data

class TestAccountNavigation:

    def test_navigate_to_account_page(self, driver_chrome):
        driver = driver_chrome
        driver.get(data.login_page_url)
        wait = WebDriverWait(driver, 60)

        # Вводим email для входа в поле
        email_input = wait.until(EC.presence_of_element_located(WebsiteLocators.EMAIL_INPUT_FORM))
        email_input.send_keys(data.test_user_login)

        # Вводим пароль для входа в поле
        password_input = wait.until(EC.presence_of_element_located(WebsiteLocators.PASSWORD_INPUT_FORM))
        password_input.send_keys(data.test_user_password)

        # Нажимаем кнопку "Войти"
        login_button = wait.until(EC.element_to_be_clickable(WebsiteLocators.LOGIN_BUTTON_FORM))
        login_button.click()

        # Ожидаем перехода на главную страницу
        wait.until(EC.url_to_be(data.main_page_url))

        # Кликаем кнопку "Личный Кабинет"
        account_button = wait.until(EC.element_to_be_clickable(WebsiteLocators.ACCOUNT_BUTTON))
        account_button.click()

        # Ожидаем перехода на страницу личного кабинета
        wait.until(EC.url_to_be(data.profile_page_url))

        # Проверяем, что кнопка "Выход" отображается на странице личного кабинета
        logout_button = wait.until(EC.presence_of_element_located(WebsiteLocators.LOGOUT_BUTTON))
        assert logout_button.is_displayed()