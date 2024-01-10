from conftest import *


class TestProduct:
    # go to sauce
    def test_go_to_sauce(self, driver):
        sauce_button = driver.find_element(*TestLocators.sauce_button)
        sauce_button.click()
        assert driver.find_element(*TestLocators.selected_element).text == 'Соусы'

    # go to fillings
    def test_go_to_fillings(self, driver):
        fillings_button = driver.find_element(*TestLocators.fillings_button)
        fillings_button.click()
        assert driver.find_element(*TestLocators.selected_element).text == 'Начинки'

    # go to fillings
    def test_go_to_rolls(self, driver):
        fillings_button = driver.find_element(*TestLocators.fillings_button)
        fillings_button.click()
        rolls_button = driver.find_element(*TestLocators.rolls_button)
        rolls_button.click()
        assert driver.find_element(*TestLocators.selected_element).text == 'Булки'

