from pages.base_page import BasePage
from pages.locators import RegistrationLocators
from selenium.common.exceptions import NoSuchElementException

import time
import os


class RegistrationPage(BasePage):

    def __init__(self, driver, timeout=10):
        super().__init__(driver, timeout)
        self.first_name_field = driver.find_element(*RegistrationLocators.FIRST_NAME_FIELD)
        self.last_name_field = driver.find_element(*RegistrationLocators.LAST_NAME_FIELD)
        self.address_field = driver.find_element(*RegistrationLocators.ADDRESS_FIELD)
        self.password_field = driver.find_element(*RegistrationLocators.PASSWORD_FIELD)
        self.registration_button = driver.find_element(*RegistrationLocators.REGISTER_BUTTON_FIELD)


    def register(self):
        self.registration_button.click()

    def get_name_error(self):
        try:
            return self.driver.find_element(*RegistrationLocators.FIRST_NAME_ERROR).text
        except NoSuchElementException:
            return None

    def get_last_name_error(self):
        try:
            return self.driver.find_element(*RegistrationLocators.LAST_NAME_ERROR).text
        except NoSuchElementException:
            return None

    def get_address_error(self):
        try:
            return self.driver.find_element(*RegistrationLocators.ADDRESS_ERROR).text
        except NoSuchElementException:
            return None

    def get_password_error(self):
        try:
            return self.driver.find_element(*RegistrationLocators.PASSWORD_ERROR).text
        except NoSuchElementException:
            return None