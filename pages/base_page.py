from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def find_element(self, *locator):
        return self.driver.find_element(*locator)

    def find_elements(self, index, *element):
        self.driver.find_elements(*element)[index].click()

    def click_element(self, *locator):
        self.find_element(*locator).click()

    def send_text(self, text, *locator):
        self.find_element(*locator).send_keys(text)

    def wait_element(self, locator):
        self.wait.until(ec.visibility_of_element_located(locator))

    def wait_and_click_to_element(self, locator, message=''):
        self.wait.until(ec.element_to_be_clickable(locator), message).click()

    class SwitchFrame:
        def __init__(self, driver, element):
            self.driver = driver
            self.element = element

        def __enter__(self):
            self.driver.switch_to.frame(self.element)

        def __exit__(self, type, value, traceback):
            self.driver.switch_to.parent_frame()

    def frame_switch(self, *locator):
        self.driver.switch_to.frame(self.driver.find_element(*locator))
