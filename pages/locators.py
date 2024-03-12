from selenium.webdriver.common.by import By


class AuthLocators:
    REGISTER_BUTTON = (By.ID, "kc-register")
    EMAIL_FIELD = (By.ID, "username")
    EMAIL_ERROR = (By.CSS_SELECTOR, 'div.rt-input-container:has(input[id="username"]) span.rt-input-container__meta--error')
    EMAIL_LINK = (By.ID, "t-btn-tab-mail")
    PASSWORD_FIELD = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "kc-login")
    PHONE_LINK = (By.ID, "t-btn-tab-phone")
    LOGIN_LINK = (By.ID, "t-btn-tab-login")
    LS_LINK = (By.ID, "t-btn-tab-ls")


class RegistrationLocators:
    FIRST_NAME_FIELD = (By.NAME, "firstName")
    FIRST_NAME_ERROR = (By.CSS_SELECTOR, 'div.rt-input-container:has(input[name="firstName"]) span.rt-input-container__meta--error')
    REGISTER_BUTTON_FIELD = (By.NAME, "register")
    LAST_NAME_FIELD = (By.NAME, "lastName")
    LAST_NAME_ERROR = (By.CSS_SELECTOR, 'div.rt-input-container:has(input[name="lastName"]) span.rt-input-container__meta--error')
    ADDRESS_FIELD = (By.ID, "address")
    ADDRESS_ERROR = (By.CSS_SELECTOR, 'div.rt-input-container:has(input[id="address"]) span.rt-input-container__meta--error')
    PASSWORD_FIELD = (By.ID, "password")
    PASSWORD_ERROR = (By.CSS_SELECTOR, 'div.rt-input-container:has(input[id="password"]) span.rt-input-container__meta--error')

class LkLocators:
    RT_LINK = (By.ID, "rt-btn")
    LK_LINK = (By.ID, "lk-btn")
    LOGOUT_LINK = (By.ID, "logout-btn")
    CONTACTS_LINK = (By.XPATH, "//div[contains(., 'Служба поддержки')]")
    USER_DATA_HEADER = (By.XPATH, "//h3[text()='Учетные данные']")
    CURRENT_CABINETS_HEADER = (By.XPATH, "//h3[text()='Личные кабинеты']")
    USER_HISTORY_HEADER = (By.XPATH, "//h3[text()='История действий']")
    SHOW_ALL_BUTTON = (By.XPATH, "//button[contains(., 'Посмотреть все')]")
    USER_HISTORY_TITLE = (By.XPATH, "//h1[contains(., 'Здесь отображаются последние действия в ваших кабинетах')]")
