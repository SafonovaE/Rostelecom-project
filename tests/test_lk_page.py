import pytest
from selenium import webdriver
from pages.auth_page import AuthPage
from pages.lk_page import LkPage
from tests.settings import valid_email, valid_password
from pages.locators import LkLocators
from pages.locators import AuthLocators


@pytest.fixture(autouse=True)
def selenium():
    selenium = webdriver.Chrome()
    yield selenium
    selenium.quit()


# Тест проверяет наличие трех ссылок в шапке сайта
def test_lk_header(selenium):
    auth_page = AuthPage(selenium)
    auth_page.auth_by_email(valid_email, valid_password)
    lk_page = LkPage(selenium)
    assert lk_page.rt_link is not None
    assert lk_page.lk_link is not None
    assert lk_page.logout_link is not None


# Тест проверяет наличие контактов на странице
def test_lk_contacts(selenium):
    auth_page = AuthPage(selenium)
    auth_page.auth_by_email(valid_email, valid_password)
    lk_page = LkPage(selenium)
    assert lk_page.contacts_link is not None


# Тест проверяет наличие секции Учетные данные на странице
def test_user_data_section(selenium):
    auth_page = AuthPage(selenium)
    auth_page.auth_by_email(valid_email, valid_password)
    assert selenium.find_element(*LkLocators.USER_DATA_HEADER) is not None


# Тест проверяет наличие секции Личные кабинеты на странице
def test_current_cabinets_section(selenium):
    auth_page = AuthPage(selenium)
    auth_page.auth_by_email(valid_email, valid_password)
    assert selenium.find_element(*LkLocators.CURRENT_CABINETS_HEADER) is not None


# Тест проверяет наличие секции История действий на странице
def test_user_history_section(selenium):
    auth_page = AuthPage(selenium)
    auth_page.auth_by_email(valid_email, valid_password)
    assert selenium.find_element(*LkLocators.USER_HISTORY_HEADER) is not None


# Тест проверяет переход на страницу истории действий по кнопке "Показать все"
def test_lk_show_all_history(selenium):
    auth_page = AuthPage(selenium)
    auth_page.auth_by_email(valid_email, valid_password)
    lk_page = LkPage(selenium)
    lk_page.go_to_show_all_page()
    assert selenium.find_element(*LkLocators.USER_HISTORY_TITLE) is not None


# Тест проверяет, что при нажатии на кнопку Выйти открывается страница авторизации
def test_logout(selenium):
    auth_page = AuthPage(selenium)
    auth_page.auth_by_email(valid_email, valid_password)
    lk_page = LkPage(selenium)
    lk_page.logout()
    assert selenium.find_element(*AuthLocators.LOGIN_BUTTON) is not None
