import pytest
from selenium import webdriver
from pages.auth_page import AuthPage
from tests.settings import valid_email, valid_password
from pages.locators import LkLocators
from pages.locators import AuthLocators


@pytest.fixture(autouse=True)
def selenium():
    selenium = webdriver.Chrome()
    yield selenium
    selenium.quit()

# Негативный тест авторизации по email
def test_auth_page_by_email_negative(selenium):
    auth_page = AuthPage(selenium)
    auth_page.auth_by_email('', '')
    assert "Введите адрес, указанный при регистрации" in auth_page.get_email_error()

# Позитивный тест авторизации по email
def test_auth_page_by_email_positive(selenium):
    auth_page = AuthPage(selenium)
    auth_page.auth_by_email(valid_email, valid_password)
    assert selenium.find_element(*LkLocators.CURRENT_CABINETS_HEADER) is not None

# Тест проверяет наличие таба авторизации по телефону
def test_auth_page_has_by_phone_link(selenium):
    AuthPage(selenium)
    assert selenium.find_element(*AuthLocators.PHONE_LINK) is not None

# Тест проверяет наличие таба авторизации по логину
def test_auth_page_has_by_login_link(selenium):
    AuthPage(selenium)
    assert selenium.find_element(*AuthLocators.LOGIN_LINK) is not None

# Тест проверяет наличие таба авторизации по лицевому счету
def test_auth_page_has_by_ls_link(selenium):
    AuthPage(selenium)
    assert selenium.find_element(*AuthLocators.LS_LINK) is not None