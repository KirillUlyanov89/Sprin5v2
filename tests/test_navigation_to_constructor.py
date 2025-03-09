import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.locators import WebsiteLocators
import src.data as data

class TestConstructorNavigation:

    def login(self, driver):
        wait = WebDriverWait(driver, 60)
        # Входим в личный кабинет пользователя
        email_input = wait.until(EC.presence_of_element_located(WebsiteLocators.EMAIL_INPUT_FORM))
        email_input.send_keys(data.test_user_login)

        password_input = wait.until(EC.presence_of_element_located(WebsiteLocators.PASSWORD_INPUT_FORM))
        password_input.send_keys(data.test_user_password)

        login_button = wait.until(EC.element_to_be_clickable(WebsiteLocators.LOGIN_BUTTON_FORM))
        login_button.click()

        # Ожидаем переход на страницу личного кабинета
        wait.until(EC.url_to_be(data.main_page_url))

    def navigate_to_account(self, driver):
        wait = WebDriverWait(driver, 60)
        account_button = wait.until(EC.element_to_be_clickable(WebsiteLocators.ACCOUNT_BUTTON))
        account_button.click()

        # Ожидаем перехода на страницу личного кабинета
        wait.until(EC.url_to_be(data.profile_page_url))

    def test_navigation_from_account_to_constructor_via_constructor_button(self, driver_chrome):
        driver = driver_chrome
        driver.get(data.login_page_url)

        self.login(driver)
        self.navigate_to_account(driver)

        # Кликаем кнопку "Конструктор"
        wait = WebDriverWait(driver, 60)
        constructor_button = wait.until(EC.element_to_be_clickable(WebsiteLocators.CONSTRUCTOR_BUTTON))
        constructor_button.click()

        # Ожидаем переход на страницу конструктора
        wait.until(EC.url_to_be(data.main_page_url))
        constructor_header = wait.until(EC.presence_of_element_located(WebsiteLocators.CONSTRUCTOR_HEADER))
        assert constructor_header.is_displayed()

    def test_navigation_from_account_to_constructor_via_logo(self, driver_chrome):
        driver = driver_chrome
        driver.get(data.login_page_url)

        self.login(driver)
        self.navigate_to_account(driver)

        # Кликаем на логотип Stellar Burgers
        wait = WebDriverWait(driver, 60)
        logo_button = wait.until(EC.element_to_be_clickable(WebsiteLocators.SERVICE_LOGO_BUTTON))
        logo_button.click()

        # Ожидаем переход на страницу конструктора
        wait.until(EC.url_to_be(data.main_page_url))
        constructor_header = wait.until(EC.presence_of_element_located(WebsiteLocators.CONSTRUCTOR_HEADER))
        assert constructor_header.is_displayed()