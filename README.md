# Stellar Burgers - 5 спринт автоматизированного тестирования на Python

## Описание проекта

Проект предназначен для автоматизированного тестирования веб-сайта Stellar Burgers. В рамках проекта проводятся тесты на регистрацию пользователя, вход в систему, выход из профиля и навигацию по разделам сайта.

## Структура проекта

- **`src/`**: Папка, содержащая настройку тестов.
    - `helpers.py`: Функции для генерации случайных данных, таких как имя, email и пароли.
    - `locators.py`: Локаторы для элементов на веб-странице, используемые в тестах.
    - `data.py`: Переменные для тестов.
- **`tests/`**: Папка, содержащая все тестовые файлы и настройки.
    - `test_navigation_in_constructor_sections.py`: Проверяет переход по разделам "Булки", "Соусы", "Начинки" в конструкторе.
    - `test_navigation_to_account.py`: Проверяет переход в личный кабинет пользователя.
    - `test_navigation_to_constructor.py`: Проверяет переход в конструктор по кнопке "Конструктор" и логотипу Stellar Burgers.
    - `test_user_login.py`: Проверяет различные способы входа в профиль.
    - `test_user_logout.py`: Проверяет функциональность выхода из профиля.
    - `test_user_registration.py`: Проверяет регистрацию пользователя.
- **`conftest.py`**: Фикстуры и настройки для тестов, включая URL страниц и тестового пользователя.
- **`requirements.txt`**: Файл с зависимостями проекта.

## Установка

1. Клонируйте репозиторий:
    ```bash
    git clone https://github.com/lnlydrvr/Sprint_3.git
    ```
    
2. Установите зависимости:
    ```bash
    pip install -r requirements.txt
    ```

## Запуск тестов

1. Убедитесь, что у вас установлен веб-драйвер для браузера (например, ChromeDriver для Google Chrome).

2. Запустите тесты с помощью `pytest`:
    ```bash
    pytest
    ```

## Тесты

### `test_user_registration.py`

- **test_successful_registration**: Проверяет успешную регистрацию пользователя с корректным именем, email и паролем.
- **test_registration_with_invalid_password**: Проверяет отображение ошибки при попытке регистрации с некорректным паролем.

### `test_user_login.py`

- **test_login_via_login_button**: Проверяет вход по кнопке "Войти в аккаунт" на главной странице.
- **test_login_via_account_button_in_header**: Проверяет вход через кнопку "Личный кабинет".
- **test_login_via_registration_form**: Проверяет вход через кнопку в форме регистрации.
- **test_login_via_forgot_password_form**: Проверяет вход через кнопку в форме восстановления пароля.

### `test_user_logout.py`

- **test_logout_from_account**: Проверяет функциональность выхода из личного кабинета.

### `test_navigation_to_account.py`

- **test_navigate_to_account_page**: Проверяет переход в личный кабинет по клику на кнопку "Личный кабинет" после входа в систему.

### `test_navigation_to_constructor.py`

- **test_navigation_from_account_to_constructor_via_constructor_button**: Проверяет переход в конструктор по кнопке "Конструктор".
- **test_navigation_from_account_to_constructor_via_logo**: Проверяет переход в конструктор по клику на логотип Stellar Burgers.

### `test_navigation_in_constructor_sections.py`

- **test_navigation_to_sections**: Проверяет переходы между разделами "Булки", "Соусы", "Начинки" в конструкторе.
