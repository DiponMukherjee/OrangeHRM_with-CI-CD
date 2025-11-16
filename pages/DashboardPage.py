from playwright.sync_api import expect

class DashboardPage:
    def __init__(self, page):
        self.page = page
        self.dashboard_text=page.get_by_role("heading", name="Dashboard")
        self.logout_button = page.get_by_role("menuitem", name="Logout")
        self.profile_button = page.get_by_role("banner").get_by_role("img", name="profile picture")
        self.sidepanel_admin_button = page.get_by_role("link", name="Admin")
        self.sidepanel_pim_button = page.get_by_role("link", name="PIM")
        self.sidepanel_leave_button = page.get_by_role("link", name="Leave")
        self.sidepanel_time_button = page.get_by_role("link", name="Time")
        self.sidepanel_recruitment_button = page.get_by_role("link", name="Recruitment")
        self.sidepanel_myinfo_button= page.get_by_role("link", name="My Info")
        self.sidepanel_performance_button = page.get_by_role("link", name="Performance")
        self.sidepanel_dashboard_button = page.get_by_role("link", name="Dashboard")
        self.sidepanel_directory_button = page.get_by_role("link", name="Dashboard")
        self.sidepanel_maintenance_button = page.get_by_role("link", name="Maintenance")
        self.sidepanel_claim_button = page.get_by_role("link", name="Claim")
        self.sidepanel_buzz_button = page.get_by_role("link", name="Buzz")
        self.help_button = page.get_by_role("button", name="")

    def navigate_to_dashboard_page(self):
        self.page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index")

    def verify_dashboard_text(self):
        assert self.dashboard_text.text_content() == "Dashboard"

    def verify_logout_help_profile_button(self):
        expect(self.profile_button).to_be_visible()
        self.profile_button.click()
        expect(self.logout_button).to_be_enabled()
        expect(self.help_button).to_be_enabled()

    def verify_all_sidepanel_button(self):
        expect(self.sidepanel_admin_button).to_be_enabled()
        expect(self.sidepanel_admin_button).to_be_visible()

        expect(self.sidepanel_pim_button).to_be_enabled()
        expect(self.sidepanel_pim_button).to_be_visible()

        expect(self.sidepanel_leave_button).to_be_enabled()
        expect(self.sidepanel_leave_button).to_be_visible()

        expect(self.sidepanel_time_button).to_be_enabled()
        expect(self.sidepanel_time_button).to_be_visible()

        expect(self.sidepanel_recruitment_button).to_be_enabled()
        expect(self.sidepanel_recruitment_button).to_be_visible()

        expect(self.sidepanel_myinfo_button).to_be_enabled()
        expect(self.sidepanel_myinfo_button).to_be_visible()

        expect(self.sidepanel_performance_button).to_be_enabled()
        expect(self.sidepanel_performance_button).to_be_visible()

        expect(self.sidepanel_dashboard_button).to_be_enabled()
        expect(self.sidepanel_dashboard_button).to_be_visible()

        expect(self.sidepanel_directory_button).to_be_enabled()
        expect(self.sidepanel_directory_button).to_be_visible()

        expect(self.sidepanel_maintenance_button).to_be_enabled()
        expect(self.sidepanel_maintenance_button).to_be_visible()

        expect(self.sidepanel_claim_button).to_be_enabled()
        expect(self.sidepanel_claim_button).to_be_visible()

        expect(self.sidepanel_buzz_button).to_be_enabled()
        expect(self.sidepanel_buzz_button).to_be_visible()

    def click_admin_link(self):
        self.sidepanel_admin_button.click()


