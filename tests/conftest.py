import pytest
from selenium import webdriver
import chromedriver_autoinstaller


@pytest.fixture(scope='function')
def driver_chrome():
    # Автоматическая установка ChromeDriver
    chromedriver_autoinstaller.install()

    # Настройка параметров браузера
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--start-maximized')

    # Создание экземпляра драйвера
    driver = webdriver.Chrome(options=chrome_options)

    yield driver  # Передача драйвера в тест

    driver.quit()  # Завершение работы драйвера после теста