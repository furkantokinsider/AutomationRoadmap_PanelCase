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

    def wait_element(self, *locator, message=''):
        return self.wait.until(ec.element_to_be_clickable(locator), message)

    def switch_to_iframe(self, *iframe_locator):
        self.wait.until(ec.frame_to_be_available_and_switch_to_it(iframe_locator))

#class SwitchFrame:
        #def __init__(self, driver, element):
            #self.driver = driver
            #self.element = element

        #def __enter__(self):
            #self.driver.switch_to.frame(self.element)

        #def __exit__(self, type, value, traceback):
            #self.driver.switch_to.parent_frame()

    #def switch_frame(self, locator):
        #return self.SwitchFrame(self.driver, self.wait_element(locator))


