from playwright.sync_api import expect

class LoginPage:
    def __init__(self, page):
        self.page = page
        self.Linked_In_Link = page.get_by_role("link").first
        self.Facebook_Link = page.get_by_role("link").nth(1)
        self.Twitter_Link = page.get_by_role("link").nth(2)
        self.YouTube_Link = page.get_by_role("link").nth(3)
        self.username_field = page.get_by_role("textbox", name="Username")
        self.password_field = page.get_by_role("textbox", name="Password")
        self.Login_Button = page.get_by_role("button", name="Login")
        self.Forget_Password_Button = page.get_by_text("Forgot your password?")
        self.invalid_cred_message = page.get_by_role("alert")
        self.empty_cred_username_text = page.get_by_text("Required").first
        self.empty_cred_password_text = page.get_by_text("Required").nth(1)

    def navigate_to_url(self, base_url):
        self.page.goto(f"{base_url}/auth/login")

    def verify_facebook_link(self):
        assert self.Facebook_Link.is_enabled()
        assert self.Facebook_Link.is_visible()

    def verify_twitter_link(self):
        assert self.Twitter_Link.is_enabled()
        assert self.Twitter_Link.is_visible()

    def verify_youtube_link(self):
        assert self.YouTube_Link.is_enabled()
        assert self.YouTube_Link.is_visible()

    def verify_linked_in_link(self):
        assert self.Linked_In_Link.is_enabled()
        assert self.Linked_In_Link.is_visible()

    def verify_forget_password_link(self):
        assert self.Forget_Password_Button.is_enabled()
        assert self.Forget_Password_Button.is_visible()

    def enter_username_password(self, username, password):
        self.username_field.clear()
        self.username_field.fill(username)
        self.password_field.clear()
        self.password_field.fill(password)

    def click_login(self):
        self.Login_Button.click()

    def verify_invalid_cred_error_texts(self):
        assert self.invalid_cred_message.text_content() == "Invalid credentials"

    def verify_empty_cred_error_texts(self):
        expect(self.empty_cred_username_text).to_contain_text("Required")
        expect(self.empty_cred_password_text).to_contain_text("Required")
