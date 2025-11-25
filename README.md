# OrangeHRM with CI/CD

[![License](https://img.shields.io/badge/License-None-brightgreen.svg)](https://github.com/DiponMukherjee/OrangeHRM_with-CI-CD/blob/main/LICENSE)

## Description

This project appears to be a UI testing framework for the OrangeHRM demo website, utilizing Python and Playwright. It includes tests for login functionality (both valid and invalid credentials), dashboard elements, and adding users through the admin panel. It leverages page object model for better code maintainability.

## Table of Contents

1.  [Features](#features)
2.  [Tech Stack](#tech-stack)
3.  [Installation](#installation)
4.  [Usage](#usage)
5.  [Project Structure](#project-structure)
6.  [Contributing](#contributing)
7.  [License](#license)
8.  [Important Links](#important-links)
9.  [Footer](#footer)

## Features

*   **Login Page Tests:**
    *   Verification of social media links (LinkedIn, Facebook, Twitter, YouTube).
    *   Testing login with valid and invalid credentials.
    *   Handling empty username and password fields.
*   **Dashboard Tests:**
    *   Verification of dashboard text.
    *   Testing the visibility and functionality of the logout, help, and profile buttons.
    *   Verification of all side panel buttons (Admin, PIM, Leave, Time, Recruitment, My Info, Performance, Dashboard, Directory, Maintenance, Claim, Buzz).
*   **Admin Add User Page Tests:**
    *   Verification of user roles (Admin, ESS).
    *   Verification of statuses (Enabled, Disabled).

## Tech Stack

*   **Programming Language:** Python
*   **Testing Framework:** Playwright
*   **Other Libraries:** pytest, pytest-base-url, pytest-html, pytest-metadata, pytest-playwright, python-slugify, requests

## Installation

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/DiponMukherjee/OrangeHRM_with-CI-CD.git
    cd OrangeHRM_with-CI-CD
    ```

2.  **Install the dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

    The `requirements.txt` file contains the following:

    ```text
    certifi==2025.10.5
    charset-normalizer==3.4.4
    colorama==0.4.6
    greenlet==3.2.4
    idna==3.11
    iniconfig==2.3.0
    Jinja2==3.1.6
    MarkupSafe==3.0.3
    packaging==25.0
    playwright==1.55.0
    pluggy==1.6.0
    pyee==13.0.0
    Pygments==2.19.2
    pytest==8.4.2
    pytest-base-url==2.1.0
    pytest-html==4.1.1
    pytest-metadata==3.1.1
    pytest-playwright==0.7.1
    python-slugify==8.0.4
    requests==2.32.5
    text-unidecode==1.3
    typing_extensions==4.15.0
    urllib3==2.5.0
    ```

3.  **Install Playwright browsers:**

    ```bash
    playwright install
    ```

## Usage

1.  **Running Tests:**

    Execute the tests using pytest:

    ```bash
    pytest
    ```

    You can also specify a specific test file:

    ```bash
    pytest tests/test_01_LoginPage_UI.py
    ```

2.  **Authentication:**

    The project uses `auth/state.json` to store authentication state. The `conftest.py` file provides a fixture `authenticated_page` that automatically logs in before running tests that require authentication.

    ```python
    import pytest

    @pytest.fixture(scope="function")
    def authenticated_page(browser):
        context = browser.new_context(storage_state="auth/state.json")
        page = context.new_page()
        yield page
        context.close()
    ```

3.  **Test Data:**

    *   `data/login_data_invalid.csv`: Contains username and password pairs for invalid login attempts.
    *   `data/login_data_valid.json`: Contains valid username and password for login.

## Project Structure

```
OrangeHRM_with-CI-CD/
├── .idea/
│   ├── inspectionProfiles/
│   ├── *
├── auth/
│   ├── state.json
│   └── state2.json
├── data/
│   ├── login_data_invalid.csv
│   └── login_data_valid.json
├── pages/
│   ├── AdminPage.py
│   ├── Admin_AddUser_Page.py
│   ├── DashboardPage.py
│   ├── LoginPage.py
│   └── __init__.py
├── tests/
│   ├── test_01_LoginPage_UI.py
│   ├── test_02_login_page_invalid_cred.py
│   ├── test_03_login_empty_cred.py
│   ├── test_04_Login_Valid_StorageState.py
│   ├── test_05_dashboard_UI.py
│   └── test_07_AddUser_UI.py
├── conftest.py
├── pytest.ini
├── requirements.txt
└── README.md
```

*   `auth`: Contains authentication state files.
*   `data`: Contains test data (e.g., login credentials).
*   `pages`: Contains page object classes.
*   `tests`: Contains test files.
*   `conftest.py`: Contains pytest configuration and fixtures.
*   `requirements.txt`: Lists the project dependencies.
*   `README.md`: The documentation file.

## Contributing

Contributions are welcome! Please follow these steps:

1.  Fork the repository.
2.  Create a new branch for your feature or bug fix.
3.  Make your changes and commit them.
4.  Submit a pull request.

## License

This project has no specified license.

## Important Links

*   **OrangeHRM Demo:** [https://opensource-demo.orangehrmlive.com/](https://opensource-demo.orangehrmlive.com/)

## Footer

[OrangeHRM_with-CI-CD](https://github.com/DiponMukherjee/OrangeHRM_with-CI-CD) by [DiponMukherjee](https://github.com/DiponMukherjee). Feel free to fork, star, and open issues!


