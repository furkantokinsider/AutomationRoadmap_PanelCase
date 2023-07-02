from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from pages.home_page import HomePage


class LoginPage(BasePage):
    EMAIL_TEXTBOX = (By.ID, 'email')
    PASSWORD_TEXTBOX = (By.ID, 'password')
    LOGIN_BTN = (By.ID, 'login-button')

    def fill_email_textbox(self, email):
        self.send_text(email, *self.EMAIL_TEXTBOX)

    def fill_password_textbox(self, password):
        self.send_text(password, *self.PASSWORD_TEXTBOX)

    def click_login_button(self):
        self.click_element(*self.LOGIN_BTN)

        return HomePage(self.driver)
