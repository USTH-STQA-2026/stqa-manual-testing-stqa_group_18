from pathlib import Path

from conftest import enable_flutter_semantics, flutter_fill, wait_for_flutter


EMAIL_LABELS = ["Email", "E-mail"]
PASSWORD_LABELS = ["Password"]
SEARCH_LABELS = [
    "Search by book title or author...",
    "Search by title or author...",
    "Search",
]


def semantic_text(page):
    enable_flutter_semantics(page)
    return " ".join(t.strip() for t in page.locator("flt-semantics").all_text_contents() if t.strip())


def save_screenshot(page, test_config, name):
    path = Path(test_config["screenshot_dir"]) / f"{name}.png"
    page.screenshot(path=str(path), full_page=True)
    return path


def contains_any(text, candidates):
    lower_text = text.lower()
    return any(c and c.lower() in lower_text for c in candidates)


def assert_contains_any(text, candidates, message):
    assert contains_any(text, candidates), f"{message}. Current semantic text: {text[:1000]}"


def open_app(page, test_config):
    page.goto(test_config["base_url"], wait_until="networkidle", timeout=60000)
    enable_flutter_semantics(page)


def wait_any_text(page, candidates, timeout=3000):
    for text in candidates:
        if not text:
            continue
        try:
            wait_for_flutter(page, text=text, timeout=timeout)
            return True
        except Exception:
            continue
    return False


def fill_any(page, labels, value):
    enable_flutter_semantics(page)
    for label in labels:
        try:
            flutter_fill(page, label, value)
            return label
        except Exception:
            continue

    fields = page.locator("input[aria-label], textarea[aria-label]")
    count = fields.count()
    for index in range(count):
        field = fields.nth(index)
        aria = field.get_attribute("aria-label") or ""
        if contains_any(aria, labels):
            field.click()
            field.fill(value)
            return aria

    raise AssertionError(f"Cannot find input field with labels: {labels}")


def click_any(page, candidates):
    enable_flutter_semantics(page)

    selectors = [
        'flt-semantics[role="button"]',
        'flt-semantics[role="tab"]',
        'flt-semantics',
    ]

    for selector in selectors:
        elements = page.locator(selector)
        count = elements.count()
        for index in range(count):
            element = elements.nth(index)
            try:
                text = (element.text_content() or "") + " " + (element.get_attribute("aria-label") or "")
                if contains_any(text, candidates):
                    element.click(timeout=5000)
                    wait_for_flutter(page, timeout=5000)
                    return text.strip()
            except Exception:
                continue

    raise AssertionError(f"Cannot click any of these texts: {candidates}")


def click_action_button(page, candidates, exclude=None):
    enable_flutter_semantics(page)
    exclude = exclude or []

    buttons = page.locator('flt-semantics[role="button"]')
    count = buttons.count()

    for index in range(count):
        button = buttons.nth(index)
        try:
            text = (button.text_content() or "") + " " + (button.get_attribute("aria-label") or "")
            if contains_any(text, candidates) and not contains_any(text, exclude):
                button.click(timeout=5000)
                wait_for_flutter(page, timeout=5000)
                return text.strip()
        except Exception:
            continue

    return click_any(page, candidates)


def assert_not_logged_in(page):
    text = semantic_text(page)
    assert "Logout" not in text, f"User should not be logged in. Current text: {text[:1000]}"
