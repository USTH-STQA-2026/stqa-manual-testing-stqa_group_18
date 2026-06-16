import os
import pytest
from dotenv import load_dotenv
from playwright.sync_api import sync_playwright
from web_detector import detect_technology, WebTech

load_dotenv()

BASE_URL = os.getenv("BASE_URL", "https://stqa.rbc.vn")
TEST_EMAIL = os.getenv("TEST_EMAIL", "")
TEST_PASSWORD = os.getenv("TEST_PASSWORD", "")
TEST_DISPLAY_NAME = os.getenv("TEST_DISPLAY_NAME", "")
SCREENSHOT_DIR = os.path.join(os.path.dirname(__file__), "screenshots")
os.makedirs(SCREENSHOT_DIR, exist_ok=True)


# ---------------------------------------------------------------------------
# Smart Wait - use explicit UI readiness checks instead of time.sleep
# ---------------------------------------------------------------------------
# Playwright supports auto-waiting for most actions such as click, fill,
# and assertion operations. However, Flutter Web CanvasKit renders the UI
# on a canvas, so the Semantics Tree may need time to update after each UI
# change.
#
# Recommended:
#   wait_for_flutter(page, text="Logout")          # Wait for text to appear
#   page.locator("...").wait_for(timeout=5000)     # Wait for a specific element
#
# Avoid:
#   time.sleep(3)    # Hard sleep is slow and flaky
# ---------------------------------------------------------------------------


def wait_for_flutter(page, text=None, selector=None, timeout=10000):
    """Smart wait for the Flutter Semantics Tree to update.

    Args:
        text: Wait for text to appear in flt-semantics.
        selector: Wait for a CSS selector to match an element.
        timeout: Maximum wait time in milliseconds. Defaults to 10 seconds.

    Examples:
        wait_for_flutter(page)                              # Wait for semantics to be ready.
        wait_for_flutter(page, text="Logout")               # Wait for "Logout".
        wait_for_flutter(page, selector='input[aria-label="Email"]')
    """
    if text:
        # Flutter Web uses both textContent and aria-label, so wait for both.
        page.locator(
            f'flt-semantics:has-text("{text}"), flt-semantics[aria-label*="{text}"]'
        ).first.wait_for(state="attached", timeout=timeout)
    elif selector:
        page.locator(selector).first.wait_for(state="attached", timeout=timeout)
    else:
        page.locator("flt-semantics").first.wait_for(state="attached", timeout=timeout)


@pytest.fixture(scope="session")
def browser():
    # Use explicit HEADLESS env so CI can choose headed mode with xvfb when needed.
    headless = os.getenv("HEADLESS", "false").lower() == "true"
    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=headless,
            args=["--force-renderer-accessibility"],
        )
        yield browser
        browser.close()


@pytest.fixture()
def page(browser):
    context = browser.new_context()
    page = context.new_page()
    yield page
    context.close()


@pytest.fixture()
def test_config():
    """Provide test configuration from environment variables."""
    return {
        "base_url": BASE_URL,
        "email": TEST_EMAIL,
        "password": TEST_PASSWORD,
        "display_name": TEST_DISPLAY_NAME,
        "screenshot_dir": SCREENSHOT_DIR,
    }


@pytest.fixture()
def web_tech(page) -> WebTech:
    """Detect the web technology and return a WebTech object.

    Tests can use this fixture to determine which interaction strategy is
    appropriate for the current page.
    """
    page.goto(BASE_URL, wait_until="networkidle", timeout=60000)
    page.locator("flt-glass-pane").wait_for(state="attached", timeout=15000)
    tech = detect_technology(page)
    print(f"\n[web_detector] {tech.name.value}", end="")
    if tech.renderer:
        print(f" ({tech.renderer})", end="")
    print()
    return tech


def enable_flutter_semantics(page, timeout=15000):
    """Enable the Flutter Semantics Tree so interactable DOM elements exist.

    The helper waits for Flutter to finish rendering before enabling
    semantics.
    """
    # Already enabled.
    if page.locator("flt-semantics").count() > 0:
        return

    enable_btn = page.locator('flt-semantics-placeholder[role="button"]').first
    try:
        enable_btn.wait_for(state="attached", timeout=timeout)
        enable_btn.focus()
        enable_btn.dispatch_event("click")
    except Exception:
        # Fallback for headless runs where placeholder click is flaky.
        page.keyboard.press("Tab")
        page.keyboard.press("Enter")

    page.locator("flt-semantics, input[aria-label], textarea[aria-label]").first.wait_for(
        state="attached",
        timeout=timeout,
    )


def flutter_fill(page, label, value):
    """Fill a Flutter text field through the semantics input."""
    field = page.locator(f'input[aria-label="{label}"]').first
    field.wait_for(state="attached", timeout=10000)
    field.click()

    # Flutter creates a hidden editing input; wait for it instead of sleeping.
    active_input = page.locator("flt-text-editing-host input, flt-text-editing-host textarea")
    try:
        active_input.first.wait_for(state="attached", timeout=3000)
        active_input.first.fill(value)
    except Exception:
        field.fill(value)


def flutter_click_button(page, text):
    """Click a Flutter button through a semantics element."""
    btn = page.locator(f'flt-semantics[role="button"]:has-text("{text}")')
    btn.click()


# ---------------------------------------------------------------------------
# Universal helpers - automatically choose a strategy by web technology
# ---------------------------------------------------------------------------

def smart_fill(page, label, value, tech: WebTech = None):
    """Fill a field using the interaction strategy that fits the technology.

    Args:
        label: aria-label for Flutter, or placeholder/label for standard HTML.
        value: Value to enter.
        tech: WebTech object. If None, the technology is detected automatically.
    """
    if tech is None:
        tech = detect_technology(page)

    if tech.is_flutter_canvaskit:
        enable_flutter_semantics(page)
        flutter_fill(page, label, value)
    else:
        # Standard HTML: find by label, placeholder, or aria-label.
        by_label = page.get_by_label(label)
        if by_label.count() > 0:
            by_label.first.fill(value)
            return
        by_placeholder = page.get_by_placeholder(label)
        if by_placeholder.count() > 0:
            by_placeholder.first.fill(value)
            return
        page.locator(f'input[aria-label="{label}"]').fill(value)


def login(page, test_config):
    """Log in and wait for the main page to load."""
    page.goto(test_config["base_url"], wait_until="networkidle", timeout=60000)
    enable_flutter_semantics(page)
    flutter_fill(page, "Email", test_config["email"])
    flutter_fill(page, "Password", test_config["password"])
    flutter_click_button(page, "Login")
    # Smart wait for the main page to load by waiting for the Logout button.
    wait_for_flutter(page, text="Logout")
    enable_flutter_semantics(page)


def smart_click(page, text, tech: WebTech = None):
    """Click a button using the interaction strategy that fits the technology.

    Args:
        text: Displayed button text.
        tech: WebTech object. If None, the technology is detected automatically.
    """
    if tech is None:
        tech = detect_technology(page)

    if tech.is_flutter_canvaskit:
        enable_flutter_semantics(page)
        flutter_click_button(page, text)
    else:
        # Standard HTML: find button by accessible name.
        page.get_by_role("button", name=text).click()
