import time
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.support.wait import WebDriverWait

from common.page_object import PageObject
from pages.locators import SigninLocators, TopBarLocators


class SigninPage(PageObject):


    @property
    def username(self):
        return self.find_element(SigninLocators.USERNAME).text

    @username.setter
    def username(self, username):
        self.send_keys(SigninLocators.USERNAME, username)

    @property
    def password(self):
        return self.find_element(SigninLocators.PASSWORD).text

    @password.setter
    def password(self, password):
        self.send_keys(SigninLocators.PASSWORD, password)

    def log_in(self):
        self.click_element(SigninLocators.LOGIN_BTN)
        WebDriverWait(self._webdriver, 10, 1).until(presence_of_element_located(TopBarLocators.ACCOUNT_SETTINGS))

    def create_new_account(self):
        self.click_element(SigninLocators.CREATE_NEW_LINK)