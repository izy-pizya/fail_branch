from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from conftest import *
from selenium.webdriver.common.by import By
import XPATH
from conftest import *


class TestProduct:
    # go to sauce
    def test_go_to_sauce(self, driver):
        WebDriverWait(driver, 10).until(EC.visibility_of_all_elements_located((By.XPATH, XPATH.sauce_button)))
        sauce_button = driver.find_element(By.XPATH, XPATH.sauce_button)
        sauce_button.click()
        assert driver.find_element(By.XPATH, XPATH.selected_element).text == 'Соусы'

    # go to fillings
    def test_go_to_fillings(self, driver):
        WebDriverWait(driver, 10).until(EC.visibility_of_all_elements_located((By.XPATH, XPATH.fillings_button)))
        fillings_button = driver.find_element(By.XPATH, XPATH.fillings_button)
        fillings_button.click()
        assert driver.find_element(By.XPATH, XPATH.selected_element).text == 'Начинки'

    # go to fillings
    def test_go_to_rolls(self, driver):
        WebDriverWait(driver, 10).until(EC.visibility_of_all_elements_located((By.XPATH, XPATH.fillings_button)))
        fillings_button = driver.find_element(By.XPATH, XPATH.fillings_button)
        fillings_button.click()
        (WebDriverWait(driver, 10).until(EC.visibility_of_all_elements_located((By.XPATH, XPATH.rolls_button))))
        rolls_button = driver.find_element(By.XPATH, XPATH.rolls_button)
        rolls_button.click()
        assert driver.find_element(By.XPATH, XPATH.selected_element).text == 'Булки'

