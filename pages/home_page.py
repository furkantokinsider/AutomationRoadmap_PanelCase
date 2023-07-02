from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec

from pages.base_page import BasePage
from pages.product_page import ProductPage


class HomePage(BasePage):
    EXPERIENCE_PRODUCTS = (By.CLASS_NAME, 'in-sidebar-wrapper__groups')
    TITLE = (By.CSS_SELECTOR, 'p[title="seleniumautomation"]')
    OPTIMIZATION_PRODUCTS = (By.XPATH, '//span[text()="Optimize"]')
    INSTORY_PRODUCT = (By.XPATH, '//span[text()="InStory"]')

    def wait_for_homepage_to_load(self):
        self.wait.until(ec.presence_of_element_located(self.TITLE))

    def click_experience_products(self):
        self.find_elements(2, *self.EXPERIENCE_PRODUCTS)

    def click_optimization_products(self):
        self.click_element(*self.OPTIMIZATION_PRODUCTS)

    def click_instory(self):
        self.click_element(*self.INSTORY_PRODUCT)

        return ProductPage(self.driver)

