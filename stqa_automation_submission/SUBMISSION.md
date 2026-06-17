# Submission Report - STQA Library Automation

| Information | Details |
|---|---|
| **Team** | Group18 |
| **Course** | Software Testing and Quality Assurance (STQA) |
| **Assignment** | A2 - Automation Testing |
| **System Under Test** | ABC Library System - https://stqa.rbc.vn |
| **Tools** | Python, pytest, Playwright |
| **Browser** | Chromium |
| **Website technology** | Flutter Web (CanvasKit renderer) |
| **Scope** | TC-01 to TC-12 |

> **Note**: ABC Library is a fictional system built for educational purposes. All names, organizations, and data are simulated.

---

## 1. Objective

This automated test suite verifies the main business flows of the library system, re-automated from the manual test cases produced in stage A1:

- Login / Logout and validation checks
- Book search and filtering
- Borrowing a book, viewing borrowed books, returning a book
- Switching the interface language

The goal is to detect defects **automatically, quickly, and repeatably**, while building a foundation for future regression testing.

---

## 2. Key Technical Context

The target website is built with **Flutter Web using the CanvasKit renderer**. The entire UI is painted onto a `<canvas>` element and **does not expose a standard HTML DOM**. As a result, ordinary Playwright locators (by text, button, or HTML role) do not work directly.

The team's solution is to interact through Flutter's **Accessibility Semantics Tree**:

1. **Enable the Semantics Tree** via `enable_flutter_semantics(page)` so Flutter generates hidden `<flt-semantics>` elements over the canvas.
2. **Interact through ARIA attributes**:
   - Input fields: `input[aria-label="Email"]`
   - Buttons: `flt-semantics[role="button"]:has-text("Login")`
   - Tabs: `flt-semantics[role="tab"][aria-label="Borrow / Return"]`
   - Book cards: `flt-semantics[role="group"][aria-label*="Code: BOOK"]`
3. **Smart Wait** instead of `time.sleep()`, using `wait_for_flutter()` to wait for the Semantics Tree to update and to reduce test flakiness.

---

## 3. Test Suite Architecture

```text
stqa-library-automation/
├── conftest.py          # Fixtures + Flutter interaction helpers (login, fill, click, wait)
├── web_detector.py      # Web technology detector module (Flutter/CanvasKit)
├── pytest.ini           # pytest configuration
├── requirements.txt     # Pinned dependencies
├── .env.example         # Environment variable template
└── tests/
    ├── helpers.py            # Test-level utilities (semantic_text, click_any, ...)
    ├── test_login.py         # TC-01, TC-02, TC-03
    ├── test_search.py        # TC-04, TC-05, TC-06, TC-07
    ├── test_borrow_return.py # TC-08, TC-09, TC-10
    └── test_general.py       # TC-11, TC-12
```

### Resilience against flakiness and UI changes

The tests do not hard-code a single expected string. Instead, the team uses **candidate text lists** together with the `contains_any` / `assert_contains_any` helpers. When the UI changes a label (for example, "Search by title" becomes "Search by book title or author..."), only the candidate list in `tests/helpers.py` needs updating, not each individual test. This keeps the suite robust against small UI changes.

---

## 4. Test Case List

| TC | File | Test Objective | Expected Result | REQ | Technique |
|---|---|---|---|---|---|
| TC-01 | test_login.py | Successful login | Reach main page, display Logout | REQ-01 | EP |
| TC-02 | test_login.py | Login with wrong password | Rejected / stays on login screen | REQ-01 | Negative, EP |
| TC-03 | test_login.py | Login with empty fields | Rejected / validation shown | REQ-01 | Negative, EP |
| TC-04 | test_search.py | Search by book title | Results containing "Flutter" shown | REQ-03 | EP |
| TC-05 | test_search.py | Search for a non-existent book | Empty-result state displayed | REQ-03 | Negative, EP |
| TC-06 | test_search.py | Filter by category | Filter works / category info displayed | REQ-03 | EP |
| TC-07 | test_search.py | Search by author | Author info / related results shown | REQ-03 | EP |
| TC-08 | test_borrow_return.py | Borrow a book | Book becomes borrowed / success message | REQ-04 | Functional |
| TC-09 | test_borrow_return.py | View borrowed books | Borrowed-books page displayed | REQ-05 | Functional |
| TC-10 | test_borrow_return.py | Return a book | Book returned / list status updated | REQ-05 | Functional |
| TC-11 | test_general.py | Logout | Return to login screen | REQ-01 | Functional |
| TC-12 | test_general.py | Switch language to English | Interface displays English text | REQ-08 | Functional |

**Distribution by function**: Login/Logout (4) · Search/Filter (4) · Borrow/Return (3) · Language (1) · **Total: 12**.

---

## 5. Installation and Execution Guide

### 5.1. Set up the environment

```bash
python3 -m venv venv
source venv/bin/activate      # macOS/Linux
# venv\Scripts\activate       # Windows

pip install -r requirements.txt
python -m playwright install chromium
```

### 5.2. Configure environment variables

Create a `.env` file from the template, then enter real test credentials:

```bash
cp .env.example .env
```

```text
BASE_URL=https://stqa.rbc.vn
TEST_EMAIL=your_email@example.com
TEST_PASSWORD=your_password
TEST_DISPLAY_NAME=Your Display Name
HEADLESS=false
```

> **Do not commit the `.env` file.** It is already listed in `.gitignore`.

### 5.3. Run the tests

```bash
# Run all tests
pytest -v -s

# Run one file
pytest tests/test_login.py

# Run one specific test case
pytest tests/test_login.py::test_tc01_login_success

# Export a JUnit XML report (for CI)
pytest -v --junitxml=report.xml
```

Evidence screenshots are saved automatically in the `screenshots/` directory (e.g. `tc01_login_success.png`).

---

## 6. Execution Results

> Update the table below after running `pytest -v -s` on the team machine.

| TC ID | Functional Area | Expected Result | Actual Result | Conclusion | Evidence |
|---|---|---|---|---|---|
| TC-01 | Login | Successful login | _Update_ | Pass/Fail | screenshots/tc01_login_success.png |
| TC-02 | Login | Wrong password rejected | _Update_ | Pass/Fail | screenshots/tc02_login_wrong_password.png |
| TC-03 | Login | Empty fields validated | _Update_ | Pass/Fail | screenshots/tc03_login_empty_fields.png |
| TC-04 | Search | Book found by title | _Update_ | Pass/Fail | screenshots/tc04_search_by_book_name.png |
| TC-05 | Search | No result shown | _Update_ | Pass/Fail | screenshots/tc05_search_no_result.png |
| TC-06 | Filter | Filter by category | _Update_ | Pass/Fail | screenshots/tc06_filter_by_category.png |
| TC-07 | Search | Search by author | _Update_ | Pass/Fail | screenshots/tc07_search_by_author.png |
| TC-08 | Borrow | Book borrowed successfully | _Update_ | Pass/Fail | screenshots/tc08_borrow_book.png |
| TC-09 | Borrowed list | Borrowed books displayed | _Update_ | Pass/Fail | screenshots/tc09_view_borrowed_books.png |
| TC-10 | Return | Book returned / status updated | _Update_ | Pass/Fail | screenshots/tc10_return_book.png |
| TC-11 | Logout | Return to login screen | _Update_ | Pass/Fail | screenshots/tc11_logout.png |
| TC-12 | Language | Switch to English | _Update_ | Pass/Fail | screenshots/tc12_switch_language_to_english.png |

| Metric | Value |
|---|---|
| Total automated tests | 12 |
| Pass | _Update_ |
| Fail | _Update_ |
| Pass rate | _Update_ |

**Link to A1 (manual)**: A1 had 40 test cases (Pass 32 / Fail 8, 80% pass rate). The 8 manual bugs serve as a basis for adding automated regression tests in later iterations. This A2 suite currently focuses on TC-01 to TC-12 from the starter project.

---

## 7. CI Integration (GitHub Actions)

The workflow should run on `push` and `pull_request`, with the following steps:

1. Install Python and dependencies
2. Install Playwright Chromium
3. Run `pytest --junitxml=report.xml`
4. Upload artifacts: `report.xml` and `screenshots/**`

To view results: open the **Actions** tab → latest run → **Artifacts** section → download `pytest-artifacts` → open `report.xml` (JUnit XML format).

> **Public repository policy**: run only the tests inside the `tests/` directory; do not add hidden tests to the public repository.

---

## 8. Files to Submit

```text
conftest.py
web_detector.py
pytest.ini
requirements.txt
.env.example
tests/__init__.py
tests/helpers.py
tests/test_login.py
tests/test_search.py
tests/test_borrow_return.py
tests/test_general.py
docs/automation-test-cases.md
docs/automation-test-execution.md
docs/automation-summary.md
README_SUBMISSION.md
```

---

## 9. Notes & Known Issues

- **Do not submit the `.env` file** (it contains login credentials).
- If a test fails because the UI text changed: open the corresponding screenshot or run `pytest -v -s` to inspect the actual displayed text, then update the **candidate text list** in `tests/helpers.py`.
- Because the system is Flutter Web CanvasKit, **always call `enable_flutter_semantics(page)`** after each navigation or any action that changes the semantic DOM.
- Some tests (TC-08, TC-10) depend on **data state** (whether a book is available or already borrowed). If the test account has borrowed all books or none, results may differ — assertions are designed to accept multiple valid states to reduce flakiness.
- It is recommended to re-run `pytest` on the team machine to collect actual results before filling in Section 6.

---

## 10. Related Documents

| Purpose | Path |
|---|---|
| Automation summary | docs/automation-summary.md |
| Test case list | docs/automation-test-cases.md |
| Execution results | docs/automation-test-execution.md |
| A1 manual testing context | docs/manual-testing-context.md |
