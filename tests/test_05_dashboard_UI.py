from pages.DashboardPage import DashboardPage
from playwright.sync_api import Page

def test_dashboard_page(authenticated_page):

#Defining the page object
    dashboard_page = DashboardPage(authenticated_page)

#Navigate to the Dashboard Page
    dashboard_page.navigate_to_dashboard_page()

#Verify logout, help and Profile button
    dashboard_page.verify_logout_help_profile_button()


#Verify all the sidepanel buttons are visible and enabled
    dashboard_page.verify_all_sidepanel_button()







