# Automation Test Summary - STQA Library

## 1. Objective

The objective of this automated test suite is to verify the main user flows of the library system:

- Login and logout
- Book search and filtering
- Book borrowing
- Viewing borrowed books
- Book return
- Switching the interface language

## 2. Technologies Used

| Component | Technology |
|---|---|
| Programming language | Python |
| Test framework | pytest |
| Browser automation | Playwright |
| Browser | Chromium |
| Website technology | Flutter Web CanvasKit |
| Interaction strategy | Flutter Accessibility Semantics Tree |

## 3. Test Distribution

| Functional Area | Test Cases | Count |
|---|---|---|
| Login/Logout | TC-01, TC-02, TC-03, TC-11 | 4 |
| Search/Filter | TC-04, TC-05, TC-06, TC-07 | 4 |
| Borrow/Return | TC-08, TC-09, TC-10 | 3 |
| Language | TC-12 | 1 |
| Total | TC-01 to TC-12 | 12 |

## 4. Evaluation

The test suite covers the main functions in the starter automation project. Negative tests such as wrong password, empty login form, and no-result search help verify validation and error handling. Borrowing and returning tests cover the core business flow of the library system.

## 5. Submission Notes

- Run `pytest -v -s` again on the team machine to collect the actual execution results.
- Enter real test account credentials in `.env`.
- Do not submit the `.env` file.
- If the UI text changes, update the candidate text lists in `tests/helpers.py`.
