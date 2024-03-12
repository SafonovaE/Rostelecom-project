from pages.base_page import BasePage
from pages.locators import AuthLocators
from pages.registration_page import RegistrationPage
from selenium.common.exceptions import NoSuchElementException
import os


class AuthPage(BasePage):

    def __init__(self, driver, timeout=10):
        super().__init__(driver, timeout)
        url = os.getenv("AUTH_PAGE_URL") or "https://b2c.passport.rt.ru/"
        driver.get(url)
        self.email_link = driver.find_element(*AuthLocators.EMAIL_LINK)
        self.email_field = driver.find_element(*AuthLocators.EMAIL_FIELD)
        self.password_field = driver.find_element(*AuthLocators.PASSWORD_FIELD)

    def go_to_registration_page(self):
        self.driver.find_element(*AuthLocators.REGISTER_BUTTON).click()
        return RegistrationPage(self.driver)

    def go_to_auth_by_email_page(self):
        self.email_link.click()
        return self

    def auth_by_email(self, email, password):
        self.go_to_auth_by_email_page()
        self.email_field.send_keys(email)
        self.password_field.send_keys(password)
        self.driver.find_element(*AuthLocators.LOGIN_BUTTON).click()
        return None

    def get_email_error(self):
        try:
            return self.driver.find_element(*AuthLocators.EMAIL_ERROR).text
        except NoSuchElementException:
            return None

