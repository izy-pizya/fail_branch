import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import XPATH

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture
def driver():
    o = Options()
    o.add_experimental_option("detach", True)
    o.add_experimental_option('excludeSwitches', ['enable-logging'])
    o.page_load_strategy = 'eager'
    driver = webdriver.Chrome(options=o)
    driver.get('https://stellarburgers.nomoreparties.site/')
    WebDriverWait(driver, 10).until(EC.visibility_of_all_elements_located((By.XPATH, XPATH.logo_button)))
    driver.maximize_window()
    yield driver
    driver.quit()



@pytest.fixture()
def go_to_personal_account(driver):
    WebDriverWait(driver, 10).until(EC.visibility_of_all_elements_located((By.XPATH, XPATH.cls_login_button)))
    personal_account = driver.find_element(By.XPATH, XPATH.personal_account)
    WebDriverWait(driver, 10).until(EC.visibility_of_all_elements_located((By.XPATH, XPATH.cls_login_button)))
    #personal_account = driver.find_element(By.XPATH, XPATH.Locators.personal_account)
    personal_account.click()
    yield

