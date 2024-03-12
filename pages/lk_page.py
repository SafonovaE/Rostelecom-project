from pages.base_page import BasePage
from pages.locators import LkLocators


class LkPage(BasePage):

    def __init__(self, driver, timeout=10):
        super().__init__(driver, timeout)
        self.rt_link = driver.find_element(*LkLocators.RT_LINK)
        self.lk_link = driver.find_element(*LkLocators.LK_LINK)
        self.logout_link = driver.find_element(*LkLocators.LOGOUT_LINK)
        self.contacts_link =driver.find_element(*LkLocators.CONTACTS_LINK)
        self.show_all_history = driver.find_element(*LkLocators.SHOW_ALL_BUTTON)

    def go_to_show_all_page(self):
        self.show_all_history.click()


    def logout(self):
        self.logout_link.click()