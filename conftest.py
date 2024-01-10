from XPATH import TestLocators


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
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture()
def go_to_personal_account(driver):
    driver.find_element(*TestLocators.personal_area_button).click()

