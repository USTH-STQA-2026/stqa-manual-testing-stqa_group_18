# STQA Library Automation Submission

This package is prepared for the Automation Testing assignment for the library system at `https://stqa.rbc.vn`.

## Main Files to Submit

```text
conftest.py
web_detector.py
pytest.ini
requirements.txt
.env.example
tests/
  __init__.py
  helpers.py
  test_login.py
  test_search.py
  test_borrow_return.py
  test_general.py
docs/
  automation-test-cases.md
  automation-test-execution.md
  automation-summary.md
```

## How to Use

1. Copy all files in this package into the project directory.
2. Create a `.env` file from `.env.example`.
3. Enter real test account credentials in `.env`.
4. Install the dependencies:

```powershell
pip install -r requirements.txt
python -m playwright install chromium
```

5. Run the tests:

```powershell
pytest -v -s
```

6. Evidence screenshots are saved automatically in the `screenshots/` directory.

## Notes

- Do not commit the `.env` file.
- If a test fails because the UI text has changed, open the screenshot or run `pytest -v -s` to inspect the displayed text, then update the candidate text lists in `tests/helpers.py`.
- This test suite uses the Flutter Semantics Tree because the website is implemented with Flutter Web CanvasKit.
