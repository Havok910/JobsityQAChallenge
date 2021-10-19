from locator import *
from element import BasePageElement
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys


class BasePage(object):
    # Constructor
    def __init__(self, driver):
        self.driver = driver


class SearchTextElement(BasePageElement):
    locator = "search_query"


class MainPage(BasePage):

    def is_title_matches(self):
        return "My Store" in self.driver.title

    def click_search_button(self):
        element = self.driver.find_element(*MainPageLocators.SEARCH_BUTTON)
        element.click()

    def click_contact_us(self):
        element = self.driver.find_element(*MainPageLocators.CONTACT_US)
        element.click()


class SearchResultsPage(BasePage):

    def is_results_found(self):
        return "0 results have been found" not in self.driver.page_source


class ContactPage(BasePage):

    def is_title_matches(self):
        return "Contact us - My Store" in self.driver.title


    def subject_customer(self):
        subject = self.driver.find_element(*ContactLocators.SUBJECT)
        select = Select(subject)
        select.select_by_visible_text('Customer service')


    def subject_webmaster(self):
        subject = self.driver.find_element(*ContactLocators.SUBJECT)
        select = Select(subject)
        select.select_by_visible_text('Webmaster')

    def input_correct_email(self):
        element = self.driver.find_element(*ContactLocators.EMAIL)
        element.send_keys('remote@jobs.com')

    def input_wrong_email(self):
        element = self.driver.find_element(*ContactLocators.EMAIL)
        element.send_keys('remotejobs')

    def input_order_reference(self):
        order_ref = ContactReferenceElement
        order_ref = '9999'

    def upload_file(self):
        element = self.driver.find_element(*ContactLocators.ATTACH_FILE)
        element.send_keys('C:\\Users\\2018072\\Documents\\Zero Bank QA Challenge\\Bug-004.png')


    def input_message(self):
        element = self.driver.find_element(*ContactLocators.MESSAGE)
        element.send_keys("This is an automated test.")


    def send_form(self):
        element = self.driver.find_element(*ContactLocators.SEND)
        element.click()

    def success(self):
        return "Your message has been successfully sent to our team." in self.driver.page_source

    def error(self):
        return "There is 1 error" in self.driver.page_source

    def many_errors(self):
        return "There are 2 errors" in self.driver.page_source


class ContactSubjectElement(BasePageElement):
    locator = 'id_contact'


class ContactEmailElement(BasePageElement):
    locator = 'from'


class ContactReferenceElement(BasePageElement):
    locator = 'id_order'


class ContactUploadElement(BasePageElement):
    locator = 'fileUpload'


class ContactMessageElement(BasePageElement):
    locator = 'message'


class ContactSendElement(BasePageElement):
    locator = 'submitMessage'



