
import pytest

@pytest.fixture(scope="function")
def authenticated_page(browser):
    context = browser.new_context(storage_state="auth/state.json")
    page = context.new_page()
    yield page
    context.close()