import pytest
from pages.LoginPage import LoginPage
from pages.DashboardPage import DashboardPage
from playwright.sync_api import Page

def load_Json():
    import json
    data = []
    with open("data/login_data_valid.json", "r") as json_file:
        loader = json.load(json_file)
        for item in loader:
            username = item["username"]
            password = item["password"]
            data.append((username, password))
        return data

@pytest.mark.parametrize("username,password", load_Json())
def test_valid_cred_login(page:Page, username, password):
    login_page = LoginPage(page)
    dashboard_page = DashboardPage(page)

#Navigate to the URL
    login_page.navigate_to_url()

#Enter Username and Password
    login_page.enter_username_password(username, password)
#Click Login Button
    login_page.click_login()
    page.wait_for_timeout(5000)

#Verify Dashboard Text
    dashboard_page.verify_dashboard_text()
#Verify Logout button
    dashboard_page.verify_logout_help_profile_button()

    page.context.storage_state(path="auth/state.json")
