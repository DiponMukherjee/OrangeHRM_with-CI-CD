from pages.Admin_AddUser_Page import Admin_AddUser_Page

def test_add_user_fields(authenticated_page):
    add_user_page = Admin_AddUser_Page(authenticated_page)

#Go to Add User Page
    add_user_page.navigate_to_add_user()

#Verify All User Roles are Available to select
    add_user_page.verify_all_user_roles()

#Verify All Statuses are Available to select
    add_user_page.verify_all_statuses()