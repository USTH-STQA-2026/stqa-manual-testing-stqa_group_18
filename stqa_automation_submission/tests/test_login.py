from conftest import login
from tests.helpers import (
    EMAIL_LABELS,
    PASSWORD_LABELS,
    assert_contains_any,
    assert_not_logged_in,
    fill_any,
    open_app,
    save_screenshot,
    semantic_text,
    wait_any_text,
    click_action_button,
)


def test_tc01_login_success(page, test_config):
    login(page, test_config)

    text = semantic_text(page)
    expected = ["Logout", test_config.get("display_name", "")]

    save_screenshot(page, test_config, "tc01_login_success")
    assert_contains_any(text, expected, "TC-01 failed: login success screen was not displayed")


def test_tc02_login_wrong_password(page, test_config):
    open_app(page, test_config)

    fill_any(page, EMAIL_LABELS, test_config["email"])
    fill_any(page, PASSWORD_LABELS, "wrong_password_123456")
    click_action_button(page, ["Login"])

    wait_any_text(page, ["Invalid", "incorrect", "Login"])
    text = semantic_text(page)

    save_screenshot(page, test_config, "tc02_login_wrong_password")
    assert_not_logged_in(page)
    assert_contains_any(
        text,
        ["Invalid", "incorrect", "Login", "Email", "Password"],
        "TC-02 failed: wrong password was not rejected",
    )


def test_tc03_login_empty_fields(page, test_config):
    open_app(page, test_config)

    click_action_button(page, ["Login"])

    wait_any_text(page, ["Email", "Password", "required", "Please"])
    text = semantic_text(page)

    save_screenshot(page, test_config, "tc03_login_empty_fields")
    assert_not_logged_in(page)
    assert_contains_any(
        text,
        ["Email", "Password", "required", "Please", "Login"],
        "TC-03 failed: empty login form was not validated",
    )
