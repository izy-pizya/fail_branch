
cls_login_button = '//button[@class="button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg"]'  # кнопка войти

cls_registration_button = '//a[@class="Auth_link__1fOlj"]'  # кнопка "Зарегистрироваться"

cls_registration_name_button = '//input[@class="text input__textfield text_type_main-default"]'  # поле для ввода почты при авторизации и поле для ввода имени при регистрации

cls_registration_password_button = '//input[@type="password"]' # поле для ввода пароля на вкладке регистрации

cls_button_for_regestr = '//a[@class="Auth_link__1fOlj"]'  # кнопка регистрация

user_password_or_registration_mail = '//*[@id="root"]/div/main/div/form/fieldset[2]/div/div/input'  # Либо поле пароль на вкладке авторизации, либо поле ввода для майла при регистрации

accept_button = '//button[@class="button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa"]'  # Кнопка подтверждения регистрации

personal_area_button = '/html/body/div/div/header/nav/a/p'  # Личный кабинет

password_recovery_button = '//*[@id="root"]/div/main/div/div/p[2]/a'  # Кнопка восстановления пароля

password_recovery_button_mail = '//*[@id="root"]/div/main/div/form/fieldset/div/div/input' # Поле восстановление пароля (почта)

letter_mail = '//*[@id="root"]/div/main/div/form/fieldset[2]/div/div/label' # Поле почтового кода

personal_account = '//*[@id="root"]/div/header/nav/a/p'  # Личный кабинет

constructor_button = '//*[@id="root"]/div/header/nav/ul/li[1]/a/p'  # кнопка "Конструктор"

logo_button = '//div[@class="AppHeader_header__logo__2D0X2"]'  # логотип бургерной

logout_button = '//button[@class="Account_button__14Yp3 text text_type_main-medium text_color_inactive"]' # кнопка выхода из аккаунта в личном кабинете

rolls_button = '//*[@id="root"]/div/main/section[1]/div[1]/div[1]/span' # вкладка булок в консруктуре

sauce_button = '//*[@id="root"]/div/main/section[1]/div[1]/div[2]/span' # вкладка соусов в консруктуре

fillings_button = '//*[@id="root"]/div/main/section[1]/div[1]/div[3]/span' #вкладка начинок в консруктуре

error_password_text = '//p[@class="input__error text_type_main-default"]' # сообщение об ошибке в пароле (недостаточно символов)

profile_button = '//a[@class="Account_link__2ETsJ text text_type_main-medium text_color_inactive Account_link_active__2opc9"]' # кнопка "профиль" в личном кабинете

assemble_the_burger = '//h1[@class="text text_type_main-large mb-5 mt-10"]' # Надпись на главной страние "Соберите бургер"

selected_element = '//div[@class="tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect"]/span' # выделенный элемент в конструкторе