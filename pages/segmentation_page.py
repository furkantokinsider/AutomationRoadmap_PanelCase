from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec

from pages.base_page import BasePage
from pages.rules_page import RulesPage


class SegmentationPage(BasePage):
    SEGMENTS_PAGE = (By.XPATH, '//p[text()="Whom to Target?"]')
    SAVE_AND_CONTINUE_BTN = (By.ID, 'save-and-next')

    def wait_until_page_segments_visible(self):
        self.wait.until(ec.presence_of_element_located(self.SEGMENTS_PAGE))

    def click_save_and_continue_btn(self):
        self.click_element(*self.SAVE_AND_CONTINUE_BTN)

        return RulesPage(self.driver)
