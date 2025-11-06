# SauceDemo E2E Tests with Playwright + Behave (BDD)

This project demonstrates **Behavior-Driven Development (BDD)** for end-to-end testing of the [SauceDemo](https://www.saucedemo.com/) web application using **Playwright + Behave (Python)**.

To serve mainly as a comparison to [my Playwright + pytest framework for SauceDemo](https://github.com/ukk0/saucedemo-playwright-pytest) and a learning opportunity, I recreated the suite using Behave to explore **BDD structure** and **human-readable feature files**.  
Both projects target the same application but highlight **different frameworks and approaches** to automation and test design.

---

## Project overview

This project focuses on providing **high functional coverage** of the SauceDemo site using a **BDD-style test structure** that emphasizes clarity and human-readability.

It features:
- **Gherkin feature files** for readable test scenarios  
- **Step definitions** mapping behavior to Playwright actions  
- **Reusable utilities** for browser setup and common logic, mappings  
- Code quality checks with **pre-commit hooks**

---

## Project structure

├── features/ # Test scenarios per feature/page in Gherkin  
│ ├── steps/ # Test step definitions  
│ └── environment.py # Behave hooks (before_all, after_all, etc.)  
├── pages/ # Page Object Models (POMs)  
├── utils/ # Helper modules (browser factory, mappings etc.)  
├── requirements.txt  
└── .pre-commit-config.yaml  

---

## Setup

This project was developed using **Python 3.13**.  
It’s recommended to use the same version to ensure compatibility.

Install dependencies and Playwright browsers:
```bash
pip install -r requirements.txt
playwright install
```

Enabling pre-commit hooks:

```bash
pre-commit install
```

---

## Running tests

Run all feature files:
```bash
behave
```

Run a specific feature file:
```bash
behave features/login.feature
```

Additional test configuration options (browser, headless mode, slow motion, etc.) will be added later.

---

## Code quality

Pre-commit hooks automatically ensure clean and consistent code using:
- black — code formatting
- isort — import sorting

Hooks will automatically run during commits for changed files.  
They can also be run manually for all files with:
```bash
pre-commit run --all-files
```

---

## Test reporting

(Coming soon. Framework and format TBD)

---

## CI/CD Integration

(Coming soon. GitHub Actions pipeline will be added together with reporting)


