
class AdminPage:
    def __init__(self, page):
        self.page = page
        self.add_user_button = page.get_by_role("button", name=" Add")

    def click_add_user_button(self):
        self.add_user_button.click()

