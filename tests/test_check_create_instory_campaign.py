import time

from tests.base_test import BaseTest
from pages.login_page import LoginPage


class MyTestCase(BaseTest):
    email = 'furkan.tok@useinsider.com'
    password = 'cidXPkrci4.qeEc'
    campaign_name = 'Furkan OPT_automation11'

    def test_check_create_instory_campaign(self):
        login_page = LoginPage(self.driver)
        login_page.fill_email_textbox(self.email)
        login_page.fill_password_textbox(self.password)
        home_page = login_page.click_login_button()

        home_page.wait_for_homepage_to_load()
        home_page.click_experience_products()
        home_page.click_optimization_products()

        product_page = home_page.click_instory()
        product_page.wait_for_instory_page_to_load()
        product_page.click_create_button()
        product_page.fill_the_campaign_name_textbox(self.campaign_name)

        segmentation_page = product_page.click_next_button()
        segmentation_page.wait_until_page_segments_visible()

        rules_page = segmentation_page.click_save_and_continue_btn()
        rules_page.wait_for_rules_page()
        rules_page.click_page_rules_button()
        rules_page.click_rule_dropbox()
        rules_page.click_page_type_option()
        rules_page.click_page_type_dropbox()
        rules_page.click_homepage_option()

        design_page = rules_page.click_save_and_continue()
        design_page.wait_for_design_page_to_load()
        design_page.add_a_new_variant()
        design_page.click_single_story()
        design_page.click_ok_button()
        design_page.click_insert_after_element()
        design_page.click_save_button()




