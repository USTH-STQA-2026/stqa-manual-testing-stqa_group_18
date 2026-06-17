# Automation Test Execution - STQA Library

| Information | Details |
|---|---|
| Executor | Group18 |
| Execution date | Enter pytest execution date |
| System | https://stqa.rbc.vn |
| Tools | pytest + Playwright |
| Command | `pytest -v -s` |
| Evidence | `screenshots/*.png`, terminal output, and `report.xml` if CI is used |

## Detailed Results

| TC ID | File | Functional Area | Expected Result | Actual Result | Conclusion | Evidence |
|---|---|---|---|---|---|---|
| TC-01 | tests/test_login.py | Login | Successful login | Update after execution | Pass/Fail | screenshots/tc01_login_success.png |
| TC-02 | tests/test_login.py | Login | Wrong password is rejected | Update after execution | Pass/Fail | screenshots/tc02_login_wrong_password.png |
| TC-03 | tests/test_login.py | Login | Empty fields are validated | Update after execution | Pass/Fail | screenshots/tc03_login_empty_fields.png |
| TC-04 | tests/test_search.py | Search | A book is found by title | Update after execution | Pass/Fail | screenshots/tc04_search_by_book_name.png |
| TC-05 | tests/test_search.py | Search | No result is shown for an unusual keyword | Update after execution | Pass/Fail | screenshots/tc05_search_no_result.png |
| TC-06 | tests/test_search.py | Filter | Category filtering works | Update after execution | Pass/Fail | screenshots/tc06_filter_by_category.png |
| TC-07 | tests/test_search.py | Search | Author search works | Update after execution | Pass/Fail | screenshots/tc07_search_by_author.png |
| TC-08 | tests/test_borrow_return.py | Borrow | Book borrowing succeeds | Update after execution | Pass/Fail | screenshots/tc08_borrow_book.png |
| TC-09 | tests/test_borrow_return.py | Borrowed list | Borrowed books are displayed | Update after execution | Pass/Fail | screenshots/tc09_view_borrowed_books.png |
| TC-10 | tests/test_borrow_return.py | Return | The book is returned or the status is updated | Update after execution | Pass/Fail | screenshots/tc10_return_book.png |
| TC-11 | tests/test_general.py | Logout | The user returns to the login screen | Update after execution | Pass/Fail | screenshots/tc11_logout.png |
| TC-12 | tests/test_general.py | Language | The interface switches to English | Update after execution | Pass/Fail | screenshots/tc12_switch_language_to_english.png |

## Summary After Execution

| Metric | Value |
|---|---|
| Total automated tests | 12 |
| Pass | Update after execution |
| Fail | Update after execution |
| Blocked | Update after execution |
| Pass rate | Update after execution |

## Exporting a JUnit XML Report

```powershell
pytest -v --junitxml=report.xml
```
