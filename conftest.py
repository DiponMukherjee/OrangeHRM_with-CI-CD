
import pytest

@pytest.fixture(scope="function")
def authenticated_page(browser):
    context = browser.new_context(storage_state="auth/state.json")
    page = context.new_page()
    yield page
    context.close()

#Addopting the --env argument from pytest command
def pytest_addoption(parser):
    parser.addoption(
        "--env",
        action="store",
        default="dev"
    )

#Using the --env value - mapping base_url- and declaring as session scoped fixture00
@pytest.fixture(scope="session")
def base_url(request):
    # Read the environment from command line
    env = request.config.getoption("--env")

    # Map each environment to a base URL
    urls = {
        "dev": "https://opensource-demo.orangehrmlive.com/web/index.php",
        "stage": "https://opensource-demo.orangehrmlive.com/web/index.php"
    }

    return urls[env]
