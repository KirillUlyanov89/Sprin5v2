import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.locators import WebsiteLocators
import src.data as data

class TestSectionsNavigation:

    def test_navigation_to_sections_sauces(self, driver_chrome):
        driver = driver_chrome
        driver.get(data.main_page_url)
        wait = WebDriverWait(driver, 60)

        sauces_section_inactive = wait.until(EC.element_to_be_clickable(WebsiteLocators.SAUCES_SECTION_INACTIVE))
        sauces_section_inactive.click()
        sauces_section_active = wait.until(EC.visibility_of_element_located(WebsiteLocators.SAUCES_SECTION_ACTIVE))
        assert 'current' in sauces_section_active.get_attribute('class')

    def test_navigation_to_sections_buns(self, driver_chrome):
        driver = driver_chrome
        driver.get(data.main_page_url)
        wait = WebDriverWait(driver, 60)

        sauces_section_inactive = wait.until(EC.element_to_be_clickable(WebsiteLocators.SAUCES_SECTION_INACTIVE))
        sauces_section_inactive.click()
        wait.until(EC.visibility_of_element_located(WebsiteLocators.SAUCES_SECTION_ACTIVE))

        buns_section_inactive = wait.until(EC.element_to_be_clickable(WebsiteLocators.BUNS_SECTION_INACTIVE))
        buns_section_inactive.click()
        buns_section_active = wait.until(EC.visibility_of_element_located(WebsiteLocators.BUNS_SECTION_ACTIVE))
        assert 'current' in buns_section_active.get_attribute('class')

    def test_navigation_to_sections_stuffings(self, driver_chrome):
        driver = driver_chrome
        driver.get(data.main_page_url)
        wait = WebDriverWait(driver, 60)

        stuffings_section_inactive = wait.until(EC.element_to_be_clickable(WebsiteLocators.STUFFINGS_SECTION_INACTIVE))
        stuffings_section_inactive.click()
        stuffings_section_active = wait.until(
            EC.visibility_of_element_located(WebsiteLocators.STUFFINGS_SECTION_ACTIVE))
        assert 'current' in stuffings_section_active.get_attribute('class')