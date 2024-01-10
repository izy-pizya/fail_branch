from conftest import *
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestTabs:
    def test_go_to_personal_account(self, driver, go_to_personal_account):
        return len(driver.find_elements(*TestLocators.accept_button)) > 0

    def test_transition_from_personal_account_to_the_constructor(self, driver, go_to_personal_account):
        driver.find_element(*TestLocators.constructor_button).click()
        assert driver.find_element(*TestLocators.assemble_the_burger).text == "Соберите бургер"

    def test_transition_from_personal_account_by_logo(self, driver, go_to_personal_account):
        driver.find_element(*TestLocators.logo_button).click()
        WebDriverWait(driver, 3).until(EC.url_contains("site"))
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'
