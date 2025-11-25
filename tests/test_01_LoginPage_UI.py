from pages.LoginPage import LoginPage
from playwright.sync_api import Page

def test_all_links(page:Page, base_url):

#Define the page object
    login_page = LoginPage(page)

#Go to the URL
    login_page.navigate_to_url(base_url)

#Verify Facebook, Linked in, Twitter, Youtube  Link
    login_page.verify_facebook_link()
    login_page.verify_linked_in_link()
    login_page.verify_twitter_link()
    login_page.verify_youtube_link()

#Verify Forget Password Button
    login_page.verify_forget_password_link()


