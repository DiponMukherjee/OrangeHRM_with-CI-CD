from playwright.sync_api import expect


class Admin_AddUser_Page:
    def __init__(self, page):
        self.page = page
        self.user_role_expandCollapse = page.locator("form i").first
        self.user_role_admin =   page.get_by_role("option", name="Admin")
        self.user_role_ESS = page.get_by_role("option", name="ESS")
        self.status_expandCollapse = page.locator("form i").nth(1)
        self.status_enabled = page.get_by_role("option", name="Enabled")
        self.status_disabled = page.get_by_role("option", name="Disabled")


    def navigate_to_add_user(self):
        self.page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/admin/saveSystemUser")

    def verify_all_user_roles(self):
        self.user_role_expandCollapse.click()
        expect(self.user_role_admin).to_be_enabled()
        expect(self.user_role_admin).to_be_visible()
        expect(self.user_role_ESS).to_be_enabled()
        expect(self.user_role_ESS).to_be_visible()
        self.user_role_expandCollapse.click()


    def select_user_role_admin(self):
        self.user_role_expandCollapse.click()
        self.user_role_admin.click()

    def select_user_role_ESS(self):
        self.user_role_expandCollapse.click()
        self.user_role_ESS.click()

    def verify_all_statuses(self):
        self.status_expandCollapse.click()
        expect(self.status_enabled).to_be_enabled()
        expect(self.status_enabled).to_be_visible()
        expect(self.status_disabled).to_be_enabled()
        expect(self.status_disabled).to_be_visible()
        self.status_expandCollapse.click()

    def select_status_enabled(self):
        self.status_expandCollapse.click()
        self.status_enabled.click()

    def select_status_disabled(self):
        self.status_expandCollapse.click()
        self.status_disabled.click()

