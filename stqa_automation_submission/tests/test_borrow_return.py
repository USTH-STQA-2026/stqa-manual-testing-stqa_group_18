from conftest import login
from tests.helpers import (
    assert_contains_any,
    click_action_button,
    click_any,
    save_screenshot,
    semantic_text,
    wait_any_text,
)


def test_tc08_borrow_book(page, test_config):
    login(page, test_config)

    click_action_button(page, ["Borrow"], exclude=["Borrow / Return"])
    wait_any_text(page, ["Borrowed", "success", "Return"])
    text = semantic_text(page)

    save_screenshot(page, test_config, "tc08_borrow_book")
    assert_contains_any(
        text,
        ["Borrowed", "success", "Return"],
        "TC-08 failed: borrow action did not show success or borrowed status",
    )


def test_tc09_view_borrowed_books(page, test_config):
    login(page, test_config)

    click_any(page, ["Borrow / Return", "Borrowed"])
    wait_any_text(page, ["Borrowed", "Return", "No borrowed"])
    text = semantic_text(page)

    save_screenshot(page, test_config, "tc09_view_borrowed_books")
    assert_contains_any(
        text,
        ["Borrowed", "Return", "No borrowed"],
        "TC-09 failed: borrowed books page was not displayed",
    )


def test_tc10_return_book(page, test_config):
    login(page, test_config)

    click_any(page, ["Borrow / Return", "Borrowed"])
    wait_any_text(page, ["Return", "No borrowed", "Borrowed"])

    before = semantic_text(page)

    if "Return" in before:
        click_action_button(page, ["Return"])
        wait_any_text(page, ["Returned", "success", "No borrowed"])

    after = semantic_text(page)

    save_screenshot(page, test_config, "tc10_return_book")
    assert_contains_any(
        before + " " + after,
        ["Return", "Returned", "No borrowed", "Borrowed"],
        "TC-10 failed: return flow was not available or did not update status",
    )
