from selenium.webdriver.common.by import By


class TestLocators:

    cls_login_button = (By.XPATH, '(//button[@class="button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg"])')  # кнопка войти

    cls_registration_button = (By.XPATH, '//a[@href="/register"]')  # кнопка "Зарегистрироваться"

    cls_registration_name_button = (By.XPATH, "(//input[@name= 'name'])[1]")  # поле для ввода почты при авторизации и поле для ввода имени при регистрации

    cls_registration_password_button = (By.XPATH, '//input[@type="password"]') # поле для ввода пароля на вкладке регистрации

    cls_button_for_regestr = (By.XPATH, '//a[@class="Auth_link__1fOlj"]')  # кнопка регистрация

    user_password = (By.XPATH, '//input[@type="password"]') # Поле для ввода пароля

    registration_mail = (By.XPATH, "(//input[@name= 'name'])[2]")  # поле ввода для майла при регистрации

    accept_button = (By.XPATH, '//button[@class="button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa"]')  # Кнопка подтверждения регистрации

    personal_area_button = (By.XPATH, '//p[text()="Личный Кабинет"]')  # Личный кабинет

    password_recovery_button = (By.XPATH, '//a[@href="/forgot-password"]')  # Кнопка восстановления пароля

    password_recovery_button_mail = (By.XPATH, '//input[@class="text input__textfield text_type_main-default"]') # Поле восстановление пароля (почта)

    letter_mail = (By.XPATH, '//input[@type="text"]') # Поле почтового кода

    constructor_button = (By.XPATH, '//p[text()="Конструктор"]')  # кнопка "Конструктор"

    logo_button = (By.XPATH, '//div[@class="AppHeader_header__logo__2D0X2"]')  # логотип бургерной

    logout_button = (By.XPATH, '//button[@class="Account_button__14Yp3 text text_type_main-medium text_color_inactive"]') # кнопка выхода из аккаунта в личном кабинете

    rolls_button = (By.XPATH, '//span[text()="Булки"]') # вкладка булок в консруктуре

    sauce_button = (By.XPATH, '//span[text()="Соусы"]') # вкладка соусов в консруктуре

    fillings_button = (By.XPATH, '//span[text()="Начинки"]') #вкладка начинок в консруктуре

    error_password_text = (By.XPATH, '//p[@class="input__error text_type_main-default"]') # сообщение об ошибке в пароле (недостаточно символов)

    profile_button = (By.XPATH, '//a[@class="Account_link__2ETsJ text text_type_main-medium text_color_inactive Account_link_active__2opc9"]') # кнопка "профиль" в личном кабинете

    assemble_the_burger = (By.XPATH, '//h1[@class="text text_type_main-large mb-5 mt-10"]') # Надпись на главной страние "Соберите бургер"

    selected_element = (By.XPATH, '//div[@class="tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect"]/span')  # выделенный элемент в конструкторе
