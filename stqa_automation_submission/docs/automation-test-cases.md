# Automation Test Cases - STQA Library

| Information | Details |
|---|---|
| Team | Group18 |
| System | https://stqa.rbc.vn |
| Tools | Python, pytest, Playwright |
| Browser | Chromium |
| Scope | TC-01 to TC-12 from the starter automation project |

## Automated Test Case List

| TC ID | File | Test Objective | Preconditions | Test Data | Expected Result | REQ | Technique |
|---|---|---|---|---|---|---|---|
| TC-01 | tests/test_login.py | Successful login | A valid account exists in `.env` | TEST_EMAIL, TEST_PASSWORD | Navigate to the main page and display Logout | REQ-01 | EP |
| TC-02 | tests/test_login.py | Login with an incorrect password | A valid email exists | wrong_password_123456 | Login is rejected and the user remains on the login screen or sees an error message | REQ-01 | Negative, EP |
| TC-03 | tests/test_login.py | Login with empty inputs | The login page is open | Empty email/password | Login is rejected and validation or the login form is displayed | REQ-01 | Negative, EP |
| TC-04 | tests/test_search.py | Search for a book by title | Successful login | Flutter | Results containing Flutter are displayed | REQ-03 | EP |
| TC-05 | tests/test_search.py | Search for a non-existent book | Successful login | zzzzzz_no_book_999999 | An empty-result state is displayed | REQ-03 | Negative, EP |
| TC-06 | tests/test_search.py | Filter books by category | Successful login | Category | The category filter works or category information is displayed | REQ-03 | EP |
| TC-07 | tests/test_search.py | Search for books by author | Successful login | Nguyen | Author information or related results are displayed | REQ-03 | EP |
| TC-08 | tests/test_borrow_return.py | Borrow a book | Successful login and an available book exists | Borrow | The book changes to borrowed status or a success message is displayed | REQ-04 | Functional |
| TC-09 | tests/test_borrow_return.py | View borrowed books | Successful login | Borrow / Return | The borrowed-books page is displayed | REQ-05 | Functional |
| TC-10 | tests/test_borrow_return.py | Return a book | Successful login | Return | The book is returned or the borrowed list status is updated | REQ-05 | Functional |
| TC-11 | tests/test_general.py | Logout | Successful login | Logout | The user returns to the login screen | REQ-01 | Functional |
| TC-12 | tests/test_general.py | Switch the interface language to English | Successful login | EN/English | The interface displays English text | REQ-08 | Functional |

## Notes

The tests use helpers from `conftest.py` and `tests/helpers.py` to interact with the Flutter Semantics Tree instead of a standard HTML DOM.
