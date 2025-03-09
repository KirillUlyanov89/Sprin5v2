import pytest
import chromedriver_autoinstaller
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.helpers import generate_name, generate_login, generate_valid_password, generate_invalid_password
from src.locators import WebsiteLocators
import src.data as data

# Автоматическая установка ChromeDriver
chromedriver_autoinstaller.install()

@pytest.fixture
def driver_chrome():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

class TestUserRegistration:

    def fill_registration_form(self, driver, name, email, password):
        wait = WebDriverWait(driver, 60)

        # Вводим имя для регистрации
        name_input = wait.until(EC.presence_of_element_located(WebsiteLocators.NAME_INPUT_FORM))
        name_input.send_keys(name)

        # Вводим email для регистрации
        email_input = wait.until(EC.presence_of_element_located(WebsiteLocators.EMAIL_INPUT_FORM))
        email_input.send_keys(email)

        # Вводим пароль для регистрации
        password_input = wait.until(EC.presence_of_element_located(WebsiteLocators.PASSWORD_INPUT_FORM))
        password_input.send_keys(password)

    def test_successful_registration(self, driver_chrome):
        driver = driver_chrome
        driver.get(data.register_page_url)

        # Генерируем необходимые данные и заполняем форму
        self.fill_registration_form(driver, generate_name(), generate_login(), generate_valid_password())

        # Нажимаем кнопку "Зарегистрироваться"
        wait = WebDriverWait(driver, 60)
        registration_button = wait.until(EC.element_to_be_clickable(WebsiteLocators.REGISTRATION_BUTTON_FORM))
        registration_button.click()

        # Ожидаем, что появится кнопка "Войти" на странице входа
        login_button = wait.until(EC.presence_of_element_located(WebsiteLocators.LOGIN_BUTTON_FORM))
        assert login_button.is_displayed()

    def test_registration_with_invalid_password(self, driver_chrome):
        driver = driver_chrome
        driver.get(data.register_page_url)

        # Генерируем необходимые данные и заполняем форму с некорректным паролем
        self.fill_registration_form(driver, generate_name(), generate_login(), generate_invalid_password())

        # Нажимаем кнопку "Зарегистрироваться"
        wait = WebDriverWait(driver, 60)
        registration_button = wait.until(EC.element_to_be_clickable(WebsiteLocators.REGISTRATION_BUTTON_FORM))
        registration_button.click()

        # Ожидаем появления сообщения об ошибке пароля
        password_error_message = wait.until(EC.presence_of_element_located(WebsiteLocators.PASSWORD_ERROR_MESSAGE))
        assert password_error_message.is_displayed()