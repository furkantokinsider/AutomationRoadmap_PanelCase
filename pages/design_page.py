from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec

from pages.base_page import BasePage


class DesignPage(BasePage):
    DESIGN_PAGE_TEXT = (By.XPATH, '//p[text() = "What to Show?"]')
    ADD_NEW_VAR_BTN = (By.ID, 'add-new-variation')
    SELECT_BTN = (By.CLASS_NAME, 'btn-select')
    OK_BTN = (By.LINK_TEXT, 'OK')
    IFRAME = (By.ID, 'ins-skeleton-partner-iframe')
    TOP_HEADER = (By.CLASS_NAME, 'top-header')
    INSERT_AFTER_THE_ELEMENT = (By.XPATH, "//li[text() = 'Insert after the element']")
    SAVE_BTN = (By.ID, 'save')
    SAVE_AND_CONTINUE_BTN = (By.ID, 'save-and-next')

    def wait_for_design_page_to_load(self):
        self.wait.until(ec.presence_of_element_located(self.DESIGN_PAGE_TEXT))

    def add_a_new_variant(self):
        self.click_element(*self.ADD_NEW_VAR_BTN)

    def click_single_story(self):
        self.click_element(*self.SELECT_BTN)

    def click_ok_button(self):
        self.click_element(*self.OK_BTN)

    def click_insert_after_element(self):
        self.frame_switch(*self.IFRAME)
        self.find_element(*self.TOP_HEADER).click()
        self.driver.switch_to.default_content()
        self.wait_and_click_to_element(self.INSERT_AFTER_THE_ELEMENT, "12312312")

    def click_save_button(self):
        self.wait_and_click_to_element(self.SAVE_BTN, "")

    def click_save_and_continue_button(self):
        self.wait_and_click_to_element(self.SAVE_AND_CONTINUE_BTN, "")
