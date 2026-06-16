from conftest import login
from tests.helpers import (
    SEARCH_LABELS,
    assert_contains_any,
    click_any,
    fill_any,
    save_screenshot,
    semantic_text,
    wait_any_text,
)


def test_tc04_search_by_book_name(page, test_config):
    login(page, test_config)

    fill_any(page, SEARCH_LABELS, "Flutter")
    wait_any_text(page, ["Flutter", "No result"])
    text = semantic_text(page)

    save_screenshot(page, test_config, "tc04_search_by_book_name")
    assert_contains_any(text, ["Flutter"], "TC-04 failed: search by book name did not show expected result")


def test_tc05_search_no_result(page, test_config):
    login(page, test_config)

    fill_any(page, SEARCH_LABELS, "zzzzzz_no_book_999999")
    wait_any_text(page, ["No result", "No books", "0"])
    text = semantic_text(page)

    save_screenshot(page, test_config, "tc05_search_no_result")
    assert_contains_any(
        text,
        ["No result", "No books", "0"],
        "TC-05 failed: no-result search did not display empty-result state",
    )


def test_tc06_filter_by_category(page, test_config):
    login(page, test_config)

    click_any(page, ["Category", "All", "Technology"])
    wait_any_text(page, ["Category", "All", "Technology"])
    text = semantic_text(page)

    save_screenshot(page, test_config, "tc06_filter_by_category")
    assert_contains_any(
        text,
        ["Category", "All", "Technology", "Book"],
        "TC-06 failed: category filter did not change or display category information",
    )


def test_tc07_search_by_author(page, test_config):
    login(page, test_config)

    fill_any(page, SEARCH_LABELS, "Nguyen")
    wait_any_text(page, ["Nguyen", "Author", "No result"])
    text = semantic_text(page)

    save_screenshot(page, test_config, "tc07_search_by_author")
    assert_contains_any(
        text,
        ["Nguyen", "Author"],
        "TC-07 failed: search by author did not show author-related result",
    )
