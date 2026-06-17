# STQA Library Automation - Starter Template

This is a hands-on **Automated Web UI Testing** assignment for the **Software Testing and Quality Assurance (STQA)** course.

The project uses **Playwright + Python** to test the Library Book Borrowing System at [https://stqa.rbc.vn](https://stqa.rbc.vn).

> **Fictional System**: ABC Library is a fictional system designed for educational purposes. All names, organizations, and data are simulated.

---

## Team Information

> **Students: Fill in the team information in the table below before submission.**

| Field | Information |
|---|---|
| **Team name** | Group_18 |
| **Class** | ICT |
| **Semester** | 2025_2026 |

| # | Student ID | Full name | Role |
|---|---|---|---|
| 1 |23BA14260|Trần Quang Thành| Team leader |
| 2 |23ba14253 |Phạm Duy Đức Tâm | Member |
| 3 |2411065| Lê Vân| Member |
| 4 | | | Member |

---

## Before You Start - Context

### Where does this assignment fit in the workflow?

```text
SRS (Software Requirements Specification) -> Development -> A1: Manual Testing -> A2: Automation Testing (YOU ARE HERE)
```

In **A1** (if completed), you performed manual testing by opening the browser, clicking buttons, and recording results. In **A2**, you automate those actions with code.

### Stakeholders

| Role | Who? | Involvement |
|---|---|---|
| **Customer** | ABC Library | Provides business requirements; the BA writes the SRS |
| **Development Team** | Programming team | Builds the system |
| **Tester / QC** | You | Writes automated tests and detects defects |
| **QA Lead** | Instructor | Reviews the test results |

### What does the tester use as the test basis?

| Source | In this assignment |
|---|---|
| **SRS** | System requirements and expected behavior |
| **Test accounts** | Accounts used for executing automated tests |
| **A1 test cases** | Manual test cases can be reused as a basis for automation |

### Software Testing vs Quality Assurance

| | **Testing** | **QA** |
|---|---|---|
| **Your work in this project** | Write automated tests, execute tests, capture screenshots | Optional quality assessment report |
| **Purpose** | Find defects automatically, quickly, and repeatedly | Evaluate the process and propose improvements |

---

> **Important**: The website uses **Flutter Web (CanvasKit renderer)**. The entire UI is rendered on `<canvas>`, so it does not expose a normal HTML DOM. This project provides helper functions that interact with the UI through the **Accessibility Semantics Tree**.

---

## Project Structure

```text
stqa-library-automation-starter/
├── conftest.py          # Fixtures and helper functions
├── web_detector.py      # Web technology detector module
├── pytest.ini           # pytest configuration
├── requirements.txt     # Dependencies
├── .env.example         # Environment variable template
├── .gitignore
├── LICENSE
├── README.md
├── README_SUBMISSION.md
├── docs/
│   ├── automation-summary.md
│   ├── automation-test-cases.md
│   ├── automation-test-execution.md
│   └── manual-testing-context.md
└── tests/
    ├── __init__.py
    ├── helpers.py
    ├── test_login.py
    ├── test_search.py
    ├── test_borrow_return.py
    └── test_general.py
```

---

## Installation

### 1. Clone the repository and create a virtual environment

```bash
git clone <repo-url>
cd stqa-library-automation-starter
python3 -m venv venv
source venv/bin/activate   # macOS/Linux
# venv\Scripts\activate    # Windows
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
playwright install chromium
```

### 3. Configure environment variables

Create a `.env` file from the template:

```bash
cp .env.example .env
```

Edit `.env` with your login credentials:

```text
BASE_URL=https://stqa.rbc.vn
TEST_EMAIL=your_email@example.com
TEST_PASSWORD=your_password
TEST_DISPLAY_NAME=Your Display Name
```

> **Do not commit `.env`**. This file is already listed in `.gitignore`.

---

## Running Tests

```bash
# Run all tests
pytest

# Run one specific file
pytest tests/test_login.py

# Run one specific test case
pytest tests/test_login.py::test_tc01_login_success

# Show verbose output
pytest -v -s
```

Screenshots are saved automatically in the `screenshots/` directory.

---

## GitHub Actions CI

If a GitHub Actions workflow is available, it should run when:

- A `push` is made to the repository
- A `pull_request` is opened or updated

The CI workflow should:

1. Install Python and dependencies
2. Install Playwright Chromium
3. Run `pytest --junitxml=report.xml`
4. Upload artifacts, including:
   - `report.xml`
   - `screenshots/**`

### Viewing CI Results

1. Open the **Actions** tab on GitHub.
2. Open the latest run of the **Pytest CI** workflow.
3. Scroll to **Artifacts** and download `pytest-artifacts`.
4. Open `report.xml` to review the results in JUnit XML format.

### Public Repository Policy

- The workflow should run only the tests available in the repository's `tests/` directory.
- Do not add hidden tests to the public repository.

---

## Test Case List

| TC | Description | File | Status |
|---|---|---|---|
| TC-01 | Login success | `test_login.py` | Complete |
| TC-02 | Login failure with wrong password | `test_login.py` | Complete |
| TC-03 | Login failure with empty fields | `test_login.py` | Complete |
| TC-04 | Search by book title | `test_search.py` | Complete |
| TC-05 | Search with no result | `test_search.py` | Complete |
| TC-06 | Filter by category | `test_search.py` | Complete |
| TC-07 | Search by author | `test_search.py` | Complete |
| TC-08 | Borrow a book | `test_borrow_return.py` | Complete |
| TC-09 | View borrowed books | `test_borrow_return.py` | Complete |
| TC-10 | Return a book | `test_borrow_return.py` | Complete |
| TC-11 | Logout | `test_general.py` | Complete |
| TC-12 | Switch interface language to English | `test_general.py` | Complete |

---

## Available Helper Functions

The helper functions are provided in `conftest.py` and `tests/helpers.py`.

### Flutter Web Helpers

| Function | Description |
|---|---|
| `enable_flutter_semantics(page)` | Enables the Accessibility Semantics Tree before UI interaction |
| `flutter_fill(page, label, value)` | Fills text into an input field using its `aria-label` |
| `flutter_click_button(page, text)` | Clicks a button by its displayed text |
| `wait_for_flutter(page, text, ...)` | Waits for the Flutter Semantics Tree to update |

### Universal Helpers

| Function | Description |
|---|---|
| `smart_fill(page, label, value, tech)` | Automatically selects an appropriate fill strategy |
| `smart_click(page, text, tech)` | Automatically selects an appropriate click strategy |
| `login(page, test_config)` | Logs in with credentials from `.env` |

### Fixtures

| Fixture | Description |
|---|---|
| `page` | A fresh Playwright Page object for each test |
| `test_config` | Dictionary containing `base_url`, `email`, `password`, `display_name`, and `screenshot_dir` |
| `web_tech` | Detected web technology information |

---

## How to Interact with Flutter Web

Flutter Web (CanvasKit) renders everything onto `<canvas>`, so there is no standard HTML DOM. To test the UI, the automation code must:

1. **Enable the Semantics Tree**: Call `enable_flutter_semantics(page)` so Flutter creates hidden `<flt-semantics>` elements over the canvas.
2. **Interact through ARIA attributes**:
   - Input fields: `input[aria-label="Email"]`
   - Buttons: `flt-semantics[role="button"]:has-text("Login")`
   - Tabs: `flt-semantics[role="tab"][aria-label="Borrow / Return"]`
   - Groups such as book cards: `flt-semantics[role="group"][aria-label*="Code: BOOK"]`

### Basic Pattern Example

```python
from conftest import login, flutter_fill, wait_for_flutter


def test_example(page, test_config):
    # 1. Log in
    login(page, test_config)

    # 2. Find an element and interact with it
    flutter_fill(page, "Search by book title or author...", "Flutter")

    # 3. Smart wait for the result instead of using time.sleep
    wait_for_flutter(page, text="Flutter")

    # 4. Assert the result through the semantics tree
    result = page.locator('flt-semantics[aria-label*="Flutter"]')
    assert result.count() > 0, "Result was not found"

    # 5. Or collect all semantics text
    sem_text = " ".join(page.locator("flt-semantics").all_text_contents())
    assert "Flutter" in sem_text
```

### Important Notes

- Always call `enable_flutter_semantics(page)` after navigation or after an operation that changes the DOM.
- Use **Smart Wait** instead of `time.sleep()`:
  - `wait_for_flutter(page, text="...")` waits for text to appear in the Semantics Tree.
  - `page.locator("...").wait_for()` waits for a specific element.
  - See the comments in `conftest.py` for more waiting patterns.
- After filling an input, Flutter may create a hidden input in `<flt-text-editing-host>`. The `flutter_fill()` helper already handles this behavior.

---

## References

### Project Documents

| Goal | Destination |
|---|---|
| Review the automation summary | [docs/automation-summary.md](docs/automation-summary.md) |
| Review automation test cases | [docs/automation-test-cases.md](docs/automation-test-cases.md) |
| Record execution results | [docs/automation-test-execution.md](docs/automation-test-execution.md) |
| Review the A1 manual testing context | [docs/manual-testing-context.md](docs/manual-testing-context.md) |

### External Links

- [Playwright Python Docs](https://playwright.dev/python/)
- [Playwright Locators](https://playwright.dev/python/docs/locators)
- [Flutter Web Accessibility](https://docs.flutter.dev/ui/accessibility)
- [pytest Documentation](https://docs.pytest.org/)
