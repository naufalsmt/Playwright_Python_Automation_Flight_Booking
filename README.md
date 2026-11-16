# ✈️ Flight Booking Automation Framework
![CI]([![Playwright Python Automation](https://github.com/naufalsmt/Playwright_Python_Automation_Flight_Booking/actions/workflows/playwright.yml/badge.svg)](https://github.com/naufalsmt/Playwright_Python_Automation_Flight_Booking/actions/workflows/playwright.yml))

## Project Overview

This project is an end-to-end web UI automation framework developed using **Python, Playwright, and Pytest** to automate flight booking workflows.
The framework focuses on validating flight search functionality, user interactions, flight results, and booking-related workflows through automated test execution.

## 🛠️ Tech Stack

- **Programming Language:** Python
- **Automation Tool:** Playwright
- **Test Framework:** Pytest
- **Design Pattern:** Page Object Model (POM)
- **Test Data:** JSON
- **CI/CD:** GitHub Actions
- **Version Control:** Git & GitHub

## 📂 Project Structure

```text
Playwright_Python_Automation_Flight_Booking/
│
├── .github/
│   └── workflows/       # GitHub Actions workflows
│
├── pages/               # Page Object Model classes
│
├── tests/               # Automated test cases
│
├── utils/               # Reusable utility functions
│
├── reports/             # Test execution reports
│
├── conftest.py          # Pytest fixtures
├── flight_test_data.json
├── invalid_json.json
├── requirements.txt
├── test_flight_booking_form.py
├── test_login.py
└── test_playwright_setup.py
```

## 🚀 Key Features

- Browser automation using Playwright
- Page Object Model implementation
- Reusable Pytest fixtures
- JSON-based test data management
- Positive and negative test scenarios
- Flight search workflow validation
- Automated test execution using Pytest
- CI/CD integration using GitHub Actions

## ⚙️ Installation & Setup

**1. Clone the repository**

```bash
git clone https://github.com/naufalsmt/Playwright_Python_Automation_Flight_Booking.git
```

**2. Navigate to the project directory**

```bash
cd Playwright Python Automation
```

**3. Install dependencies**

```bash
pip install -r requirements.txt
```

**4. Install Playwright browsers**

```bash
playwright install
```

## ▶️ Running Tests

Run all test cases:

```bash
pytest -v
```

Run a specific test file:

```bash
pytest tests/test_2_flight_selection.py -v
```

## 🔄 CI/CD Integration

GitHub Actions is integrated to execute automated tests through a workflow, supporting continuous testing and validation.

## 👨‍💻 Author

**Naufal Shamsudeen**

Software QA Engineer | Python | Playwright | Pytest | API Testing

[GitHub Profile](https://github.com/naufalsmt)
