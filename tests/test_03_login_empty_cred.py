from pages.LoginPage import LoginPage
from playwright.sync_api import Page

def test_empty_cred_login(page:Page):
#Defining Page Object
    login_page = LoginPage(page)

#Navigate to the Login Page
    login_page.navigate_to_url()

#Click on the Login Button
    login_page.click_login()

#Verify Empty Cred Error Message
    login_page.verify_empty_cred_error_texts()