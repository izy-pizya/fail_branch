
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from conftest import *
from faker import Faker


class TestLogin:
    # Registration
    def test_registration(self, driver):
        fake = Faker()
        driver.find_element(*TestLocators.cls_login_button).click()
        driver.find_element(*TestLocators.cls_registration_button).click()
        driver.find_element(*TestLocators.cls_registration_name_button).send_keys(fake.email())
        driver.find_element(*TestLocators.registration_mail).send_keys(fake.email())
        driver.find_element(*TestLocators.cls_registration_password_button).send_keys('123456')
        driver.find_element(*TestLocators.accept_button).click()
        WebDriverWait(driver, 3).until(EC.url_contains("site/login"))
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login'

    def test_sign_in(self, driver):
        driver.find_element(*TestLocators.cls_login_button).click()
        driver.find_element(*TestLocators.cls_registration_name_button).send_keys('sobaka@ya.ru')
        driver.find_element(*TestLocators.user_password).send_keys('123456')
        driver.find_element(*TestLocators.accept_button).click()
        driver.find_element(*TestLocators.personal_area_button).click()
        return len(driver.find_element(*TestLocators.profile_button)) > 0

    def test_error_password(self, driver):
        driver.find_element(*TestLocators.cls_login_button).click()
        driver.find_element(*TestLocators.cls_registration_name_button).send_keys('sobaka@ya.ru')
        driver.find_element(*TestLocators.user_password).send_keys('12345')
        accept_button = driver.find_element(*TestLocators.accept_button)
        accept_button.click()
        assert (driver.find_element(*TestLocators.error_password_text)).text == 'Некорректный пароль'

    def test_personal_area_log_in(self, driver):
        driver.find_element(*TestLocators.personal_area_button).click()
        driver.find_element(*TestLocators.cls_registration_name_button).send_keys('sobaka@ya.ru')
        driver.find_element(*TestLocators.user_password).send_keys('123456')
        driver.find_element(*TestLocators.accept_button).click()
        driver.find_element(*TestLocators.personal_area_button).click()
        return len(driver.find_element(*TestLocators.profile_button)) > 0

    def test_sign_in_after_registration(self, driver):
        driver.find_element(*TestLocators.cls_login_button).click()
        driver.find_element(*TestLocators.cls_registration_button).click()
        driver.find_element(*TestLocators.cls_button_for_regestr).click()
        driver.find_element(*TestLocators.cls_registration_name_button).send_keys('sobaka@ya.ru')
        driver.find_element(*TestLocators.user_password).send_keys('123456')
        driver.find_element(*TestLocators.accept_button).click()
        driver.find_element(*TestLocators.personal_area_button).click()
        return len(driver.find_element(*TestLocators.profile_button)) > 0

    def test_sign_in_by_password_recovery_button(self, driver):
        driver.find_element(*TestLocators.cls_login_button).click()
        driver.find_element(*TestLocators.password_recovery_button).click()
        driver.find_element(*TestLocators.cls_button_for_regestr).click()
        driver.find_element(*TestLocators.cls_registration_name_button).send_keys('sobaka@ya.ru')
        driver.find_element(*TestLocators.user_password).send_keys('123456')
        driver.find_element(*TestLocators.accept_button).click()
        driver.find_element(*TestLocators.personal_area_button).click()
        return len(driver.find_element(*TestLocators.profile_button)) > 0

    def test_logout(self, driver, go_to_personal_account):
        driver.find_element(*TestLocators.cls_registration_name_button).send_keys('sobaka@ya.ru')
        driver.find_element(*TestLocators.user_password).send_keys('123456')
        driver.find_element(*TestLocators.accept_button).click()
        driver.find_element(*TestLocators.personal_area_button).click()
        driver.find_element(*TestLocators.logout_button).click()
        accept_button = driver.find_element(*TestLocators.accept_button)
        return len(accept_button) > 0
