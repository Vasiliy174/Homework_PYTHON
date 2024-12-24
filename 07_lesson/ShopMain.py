from selenium.webdriver.common.by import By
from selenium import webdriver

class ShopmMainPage:
    def __init__(self, browser):
        self.browser = browser
        self.browser.get('')

    def registration_fields(self):
        self._name = (By.ID, "user-name")
        self._pass = (By.ID, "password")
        self._log_button =(By.ID, "login-button")
        self.browser.find_element(*self._name).send_keys("standart_user")
        self.browser.find_element(*self._pass).send_keys("secret_sauce")
        self.browser.find_element(*self._log_button).click()

    def buy_issue(self):
        self.Sause_Labs_Backpack = (By.ID "add-to-cart-labs-backpack")
