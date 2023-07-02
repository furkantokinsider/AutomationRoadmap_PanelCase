from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec

from pages.base_page import BasePage
from pages.segmentation_page import SegmentationPage


class ProductPage(BasePage):
    CREATE_BTN = (By.ID, 'create-mobile-campaign')
    CAMPAIGN_NAME_TEXTBOX = (By.ID, 'campaign-name')
    NEXT_BTN = (By.ID, 'accept')
    INSTORY_HEADER = (By.CLASS_NAME, 'fl-l')

    def wait_for_instory_page_to_load(self):
        self.wait.until(ec.presence_of_element_located(self.INSTORY_HEADER))

    def click_create_button(self):
        self.click_element(*self.CREATE_BTN)

    def fill_the_campaign_name_textbox(self, text):
        self.send_text(text, *self.CAMPAIGN_NAME_TEXTBOX)

    def click_next_button(self):
        self.click_element(*self.NEXT_BTN)

        return SegmentationPage(self.driver)
