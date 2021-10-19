import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import page


class AutoPracticeContact(unittest.TestCase):

    def setUp(self):
        s = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=s)
        self.driver.get("http://automationpractice.com")
        self.driver.maximize_window()

    def test_complete_contact(self):
        # Validate the success of a complete contact form
        main_page = page.MainPage(self.driver)
        contact = page.ContactPage(self.driver)

        assert main_page.is_title_matches()
        main_page.click_contact_us()
        self.driver.implicitly_wait(10)

        assert contact.is_title_matches()

        contact.subject_customer()
        contact.input_correct_email()
        contact.input_message()
        contact.send_form()

        self.driver.implicitly_wait(20)

        assert contact.success()

    def test_complete_contact_webmaster(self):
        # Validate the success of a complete contact form
        main_page = page.MainPage(self.driver)
        contact = page.ContactPage(self.driver)

        assert main_page.is_title_matches()
        main_page.click_contact_us()
        self.driver.implicitly_wait(10)

        assert contact.is_title_matches()

        contact.subject_webmaster()
        contact.input_correct_email()
        contact.input_message()
        contact.send_form()

        self.driver.implicitly_wait(20)

        assert contact.success()

    def test_incorrect_mail(self):
        main_page = page.MainPage(self.driver)
        contact = page.ContactPage(self.driver)

        assert main_page.is_title_matches()
        main_page.click_contact_us()
        self.driver.implicitly_wait(10)

        assert contact.is_title_matches()

        contact.subject_customer()
        contact.input_wrong_email()
        contact.input_message()
        contact.send_form()

        self.driver.implicitly_wait(10)
        assert contact.error()

    def test_no_subject(self):
        main_page = page.MainPage(self.driver)
        contact = page.ContactPage(self.driver)

        assert main_page.is_title_matches()
        main_page.click_contact_us()
        self.driver.implicitly_wait(10)

        assert contact.is_title_matches()

        contact.input_correct_email()
        contact.input_message()
        contact.send_form()

        self.driver.implicitly_wait(10)
        assert contact.error()

    def test_no_message(self):
        main_page = page.MainPage(self.driver)
        contact = page.ContactPage(self.driver)

        assert main_page.is_title_matches()
        main_page.click_contact_us()
        self.driver.implicitly_wait(10)

        assert contact.is_title_matches()

        contact.subject_customer()
        contact.input_correct_email()
        contact.send_form()

        self.driver.implicitly_wait(10)
        assert contact.error()

    def test_attached_file(self):
        main_page = page.MainPage(self.driver)
        contact = page.ContactPage(self.driver)

        assert main_page.is_title_matches()
        main_page.click_contact_us()
        self.driver.implicitly_wait(10)

        assert contact.is_title_matches()

        contact.subject_customer()
        contact.input_correct_email()
        contact.input_message()
        contact.upload_file()
        contact.send_form()

        self.driver.implicitly_wait(10)
        assert contact.success()

    def test_multiple_errors(self):
        main_page = page.MainPage(self.driver)
        contact = page.ContactPage(self.driver)

        assert main_page.is_title_matches()
        main_page.click_contact_us()
        self.driver.implicitly_wait(10)

        assert contact.is_title_matches()

        contact.input_wrong_email()
        contact.send_form()

        self.driver.implicitly_wait(20)

        assert contact.many_errors()

    def tearDown(self) -> None:
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
