from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class CampaignDetailsPage(BasePage):
    SAVE_AND_CONTINUE_BTN = (By.ID, 'save-and-next')
    ADD_NEW_VAR_BTN = (By.ID, 'add-new-variation')
    SINGLE_STORY_TEMPLATE = (By.CLASS_NAME, 'overlay')
    SELECT_BTN = (By.ID, 'btn-select')
    POP_UP_CONFIRMATION_BTN = (By.LINK_TEXT, 'OK')
    IMAGE_SLIDER = (By.XPATH, '//li[@class="flex-active-slide"]/div')
    INSERT_AFTER_ELEMENT = (By.CLASS_NAME, 'append-after animationHalf')
    SAVE_BUTTON = (By.ID, 'save')
    LANGUAGE_DROPBOX = (By.ID, 'personalization-language')
    ALL_LANGUAGES_OPTION = (By.CSS_SELECTOR, '.personalization-language-all-languages')
    START_DATE = (By.CSS_SELECTOR, '.reportrange-text')
    NEVER_ENDS_BTN = (By.CSS_SELECTOR, 'label[for="Never Ends"]')
    DISPLAY_SETTINGS_ACCORDION = (By.CLASS_NAME, 'w-1 qa-accordion')
    DISPLAY_ON_SELECTED_DAYS = (By.XPATH, '//*[contains(text(), "only on selected days")]')
    MONDAY_BTN = (By.CSS_SELECTOR, 'span[title="Monday"]')
    FRIDAY_BTN = (By.CSS_SELECTOR, 'span[title="Friday"]')
    ADVANCED_SETTINGS_ACCORDION = (By.CSS_SELECTOR, '.qa-accordion-wrapper')[2]
    PRIORITY_BTN = (By.ID, 'priority')
    PRIORITY_ONE = (By.CLASS_NAME, 'option__1 priority-1')
    TEST_STATUS = (By.CSS_SELECTOR, 'label[for="Test"]')


