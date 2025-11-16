import pytest
from playwright.sync_api import Page
from pages.LoginPage import LoginPage

#Loading the CSV data file and return in a List of Tuples
def load_csv_data():
    import csv
    data =[]
    with open("data/login_data_invalid.csv") as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            data.append(row)
        return data

#Parameterize username and password and calling the Function
@pytest.mark.parametrize("username,password", load_csv_data())

#Test
def test_invalid_cred_login(page: Page, username, password):

#Defining Page Object
    login_page = LoginPage(page)
#Navigate to the URL
    login_page.navigate_to_url()
#Enter Username and Password
    login_page.enter_username_password(username, password)
#Click on Login Button
    login_page.click_login()
#Assertion of Error Message
    login_page.verify_invalid_cred_error_texts()