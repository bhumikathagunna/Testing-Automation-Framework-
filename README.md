# Automation Project

This project contains automated tests for both UI and API functionalities.

## Directory Structure
automation/
├── __init__.py
├── lib/
│   ├── __init__.py
│   ├── helpers.py
├── pages/
│   ├── __init__.py
│   ├── login_page.py
├── test_suits/
│   ├── __init__.py
│   ├── base_test.py
│   ├── conftest.py
│   ├── test_api.py
│   ├── test_login.py
│   ├── allure-results/
│   ├── .pytest_cache/
│   ├── =/


Key Files
lib/helpers.py: Contains helper functions for interacting with web elements.
pages/login_page.py: Page Object Model for the login page.
test_suits/base_test.py: Base test class that includes common setup and teardown methods.
test_suits/conftest.py: Configuration file for pytest fixtures.
test_suits/test_api.py: Contains test cases for API endpoints.
test_suits/test_login.py: Contains test cases for login functionality.


## Requirements

- Python 3.x
- pytest
- requests

## Installation

Install the required packages using pip:

```bash
pip install -r requirements.txt
```

## Running Tests

To run all tests, use the following command:
pytest 

To run a specific test file, use:
pytest path/to/test_file.py


## Test Cases

### UI Tests

- `test_login.py`: Contains test cases for login functionality.

### API Tests

- `test_api.py`: Contains test cases for API endpoints.


## Generate Allure Report
To generate an Allure report, follow these steps:
Run tests with Allure:
pytest --alluredir=allure-results

Generate the report:
allure serve allure-results
