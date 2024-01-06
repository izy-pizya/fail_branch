import time

import pytest

import conftest
from conftest import *
from selenium.webdriver.common.by import By
import XPATH


class TestTabs:
    def test_go_to_personal_account(self, driver, go_to_personal_account):
        accept_button = WebDriverWait(driver, 10).until(EC.visibility_of_all_elements_located((By.XPATH, XPATH.accept_button)))
        #accept_button = driver.find_elements(By.XPATH, XPATH.accept_button)
        return len(accept_button) > 0       # у меня лен переставал работать, сутки спустя заработал

    def test_transition_from_personal_account_to_the_constructor(self, driver, go_to_personal_account):
        WebDriverWait(driver, 10).until(EC.visibility_of_all_elements_located((By.XPATH, XPATH.accept_button)))
        constructor_button = driver.find_element(By.XPATH, XPATH.constructor_button)
        constructor_button.click()
        assert driver.find_element(By.XPATH, XPATH.assemble_the_burger).text == "Соберите бургер"

    def test_transition_from_personal_account_by_logo(self, driver, go_to_personal_account):
        WebDriverWait(driver, 10).until(EC.visibility_of_all_elements_located((By.XPATH, XPATH.accept_button)))
        logo_button = driver.find_element(By.XPATH, XPATH.logo_button)
        logo_button.click()
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'
