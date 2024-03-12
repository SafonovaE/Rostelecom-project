import pytest
from selenium import webdriver
from pages.auth_page import AuthPage
import time


@pytest.fixture(autouse=True)
def selenium():
    selenium = webdriver.Chrome()
    yield selenium
    selenium.quit()


def test_registration_page_name_negative(selenium):
    auth_page = AuthPage(selenium)
    registration_page = auth_page.go_to_registration_page()
    assert registration_page.first_name_field is not None
    registration_page.register()
    # Проверяем, что при пустом поле выводится ошибка
    assert "Необходимо заполнить поле кириллицей" in registration_page.get_last_name_error()
    registration_page.first_name_field.send_keys("John")
    registration_page.register()
    # Проверяем, что при заполнении поля латинскими буквами выводится ошибка
    assert "Необходимо заполнить поле кириллицей" in registration_page.get_last_name_error()

def test_registration_page_name_positive(selenium):
    auth_page = AuthPage(selenium)
    registration_page = auth_page.go_to_registration_page()
    assert registration_page.first_name_field is not None
    registration_page.first_name_field.send_keys("Аркадий")
    registration_page.register()
    # Проверяем, что при корректно введенном имени ошибки нет
    assert registration_page.get_first_name_error() is None


def test_registration_page_last_name_negative(selenium):
    auth_page = AuthPage(selenium)
    registration_page = auth_page.go_to_registration_page()
    assert registration_page.last_name_field is not None
    registration_page.register()
    # Проверяем, что при пустом поле выводится ошибка
    assert "Необходимо заполнить поле кириллицей" in registration_page.get_last_name_error()
    registration_page.last_name_field.send_keys("222")
    registration_page.register()
    # Проверяем, что при заполнении поля цифрами выводится ошибка
    assert "Необходимо заполнить поле кириллицей" in registration_page.get_last_name_error()

def test_registration_page_last_name_positive(selenium):
    auth_page = AuthPage(selenium)
    registration_page = auth_page.go_to_registration_page()
    assert registration_page.last_name_field is not None
    registration_page.last_name_field.send_keys("Аркадьев")
    registration_page.register()
    # Проверяем, что при введенном имени в корректном формате ошибки нет
    assert registration_page.get_last_name_error() is None


def test_registration_page_address_negative(selenium):
    auth_page = AuthPage(selenium)
    registration_page = auth_page.go_to_registration_page()
    assert registration_page.address_field is not None
    registration_page.register()
    # Проверяем, что при пустом поле выводится ошибка
    assert "Введите телефон в формате +7ХХХХХХХХХХ или +375XXXXXXXXX, или email в формате example@email.ru" in registration_page.get_address_error()
    registration_page.address_field.send_keys("222")
    registration_page.register()
    # Проверяем, что при заполнении поля значениями в неверном формате выводится ошибка
    assert "Введите телефон в формате +7ХХХХХХХХХХ или +375XXXXXXXXX, или email в формате example@email.ru" in registration_page.get_address_error()


def test_registration_page_address_positive(selenium):
    auth_page = AuthPage(selenium)
    registration_page = auth_page.go_to_registration_page()
    assert registration_page.address_field is not None
    registration_page.address_field.send_keys("12345@test.com")
    registration_page.register()
    # Проверяем, что при корректно введенном значении ошибки нет
    assert registration_page.get_address_error() is None

def test_registration_page_password_negative(selenium):
    auth_page = AuthPage(selenium)
    registration_page = auth_page.go_to_registration_page()
    assert registration_page.password_field is not None
    registration_page.register()
    # Проверяем, что при пустом поле выводится ошибка
    assert "Длина пароля должна быть не менее 8 символов" in registration_page.get_password_error()
    registration_page.password_field.send_keys("085532")
    registration_page.register()
    # Проверяем, что при заполнении пароля менее 8 символов выводится ошибка
    assert "Длина пароля должна быть не менее 8 символов" in registration_page.get_password_error()
    time.sleep(3)

def test_registration_page_password_positive(selenium):
    auth_page = AuthPage(selenium)
    registration_page = auth_page.go_to_registration_page()
    assert registration_page.password_field is not None
    registration_page.password_field.send_keys("123f456Q8")
    registration_page.register()
    # Проверяем, что при корректно введенном значении ошибки нет
    assert registration_page.get_password_error() is None