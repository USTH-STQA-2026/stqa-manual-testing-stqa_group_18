from conftest import login
from tests.helpers import (
    assert_contains_any,
    click_action_button,
    click_any,
    save_screenshot,
    semantic_text,
    wait_any_text,
)


def test_tc11_logout(page, test_config):
    login(page, test_config)

    click_action_button(page, ["Logout"])
    wait_any_text(page, ["Login", "Email", "Password"])
    text = semantic_text(page)

    save_screenshot(page, test_config, "tc11_logout")
    assert_contains_any(text, ["Login", "Email", "Password"], "TC-11 failed: logout did not return to login screen")
    assert "Logout" not in text


def test_tc12_switch_language_to_english(page, test_config):
    login(page, test_config)

    click_any(page, ["EN", "English"])
    wait_any_text(page, ["Logout", "Borrow", "Return", "Search", "Book", "Category"])
    text = semantic_text(page)

    save_screenshot(page, test_config, "tc12_switch_language_to_english")
    assert_contains_any(
        text,
        ["Logout", "Borrow", "Return", "Search", "Book", "Category"],
        "TC-12 failed: English language was not displayed after switching language",
    )
