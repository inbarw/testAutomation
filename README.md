# Selenium Python Assignment 

## Introduction
This project contains automated tests for a web application and api using Selenium WebDriver with Python and pytest.

## Getting Started

### Prerequisites
Ensure that you have the following installed on your system:
- Python 3.8+
  - You can download Python from the official website: [Python Downloads.](https://www.python.org/downloads/)
  - After installation, verify Python is installed by running:
    ```bash
    python --version
- pip (Python package manager)
  - Verify pip is installed by running:
    ```bash
    pip --version
  - If pip is not installed, you can install it by following [these instructions.](https://pip.pypa.io/en/stable/installation/)
- Google Chrome
- ChromeDriver
  - You can download ChromeDriver from the [official site.](https://googlechromelabs.github.io/chrome-for-testing/) (You can download 'stable')

### Installation
1. Clone the repository:
    ```bash
    https://github.com/inbarw/testAutomation.git
   ```
2. Create and activate a virtual environment:
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```
3. Install the required packages:
    ```bash
    pip install requirements.txt       
    ```
4. Ensure that the ChromeDriver is in your system's PATH, or specify the path in your test setup.

## Running Tests
### Run All Tests
To run all tests, execute:
```bash
pytest
```
To run ui test:
```bash
pytest tests/ui_tests/test_ui.py
```
To run api test:
```bash
pytest tests/api_tests/test_api.py
```