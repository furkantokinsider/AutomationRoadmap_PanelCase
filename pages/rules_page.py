from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec

from pages.base_page import BasePage
from pages.design_page import DesignPage


class RulesPage(BasePage):
    RULES_PAGE = (By.XPATH, '//p[text() = "When to Trigger?"]')
    PAGE_RULES_BTN = (By.XPATH, '//p[contains(text(), "Page Rules")]')
    RULE_DROPBOX = (By.ID, 'conditionList0') #[id*='conditionList']
    PAGE_TYPE_OPTION = (By.CSS_SELECTOR, '.conditionList0-page-type') #[class*='page-type']
    PAGE_TYPE_DROPBOX = (By.ID, 'qa-drop-down')
    HOMEPAGE_OPTION = (By.CSS_SELECTOR, '.qa-drop-down-homepage')
    SAVE_AND_CONTINUE_BTN = (By.ID, 'save-and-next')

    def wait_for_rules_page(self):
        self.wait.until(ec.presence_of_element_located(self.RULES_PAGE))

    def click_page_rules_button(self):
        self.click_element(*self.PAGE_RULES_BTN)

    def click_rule_dropbox(self):
        self.click_element(*self.RULE_DROPBOX)

    def click_page_type_option(self):
        self.click_element(*self.PAGE_TYPE_OPTION)

    def click_page_type_dropbox(self):
        self.click_element(*self.PAGE_TYPE_DROPBOX)

    def click_homepage_option(self):
        self.click_element(*self.HOMEPAGE_OPTION)

    def click_save_and_continue(self):
        self.click_element(*self.SAVE_AND_CONTINUE_BTN)

        return DesignPage(self.driver)
