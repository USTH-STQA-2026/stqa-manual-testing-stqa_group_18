# Test Summary

## 1. Group Information

| Item | Information |
|---|---|
| **Group** | `<!Group 18>` |
| **Class** | `<!ICT>` |
| **Report Date** | 27/05/2026 |
| **System Under Test** | https://stqa.rbc.vn — v1.0 |
| **Scope** | Manual black-box testing based on the SRS |

---

## 2. Result Overview

| Metric | Value |
|---|---:|
| Total test cases | 40 |
| Pass | 32 |
| Fail | 8 |
| Blocked | 0 |
| Not Run | 0 |
| **Pass Rate** | **80%** |
| **Bugs Found** | **8** |

> Note: TC-33 has no execution evidence, so it is marked as **Not Run**. If the team executes it later and it passes, the pass rate will increase.

### Distribution by Feature Group

| Feature Group | TC | Pass | Fail | Not Run | Bugs | Evaluation |
|---|---:|---:|---:|---:|---:|---|
| Login | 5 | 5 | 0 | 0 | 0 | Stable |
| Book list, search, and filter | 9 | 8 | 1 | 0 | 1 | Basic search works well, but leading/trailing spaces are not handled. |
| Borrow Book | 7 | 5 | 2 | 0 | 2 | Important business-rule issue with the borrow limit. |
| Return Book and Overdue Handling | 5 | 4 | 1 | 0 | 1 | Missing warning when returning an overdue book. |
| Member Management | 4 | 2 | 2 | 0 | 2 | Email validation is inconsistent. |
| Borrow Records and Permission | 4 | 3 | 1 | 0 | 1 | Serious permission issue. |
| UI, language, and reset | 6 | 4 | 1 | 1 | 0 | Language switching is incomplete; TC-33 was not executed. |

### Bug Distribution by Severity

| Severity | Quantity | Bug IDs |
|---|---:|---|
| High | 2 | BUG-02, BUG-06 |
| Medium | 4 | BUG-01, BUG-03, BUG-04, BUG-05 |
| Low | 2 | BUG-07, BUG-08 |

---

## 3. Test Design Techniques Used

| Technique | Applied Requirements | Number of TCs | Explanation |
|---|---|---:|---|
| EP — Equivalence Partitioning | REQ-01, REQ-03, REQ-07 | Many TCs | Inputs were divided into valid/invalid groups: existing/non-existing email, correct/incorrect password, existing/non-existing keyword, valid/invalid/duplicate email. |
| BVA — Boundary Value Analysis | REQ-04 | TC-19, TC-20 | Checked the maximum 3-book borrowing limit and the 14-day due date boundary. |
| Decision Table | REQ-04 | TC-14 → TC-18 | Combined member status, book status, and number of borrowed books to decide whether borrowing should be allowed or rejected. |
| Access Control Testing | REQ-07, REQ-08 | TC-25, TC-29 → TC-32, TC-34, TC-40 | Checked that Librarian and Member accounts have different access rights. |
| State-based Testing | REQ-02, REQ-05, REQ-06 | TC-08, TC-21, TC-24, TC-33 | Checked state transitions after borrowing, returning, overdue checking, and data reset. |
| Negative / Robustness Testing | REQ-01, REQ-03, REQ-04, REQ-07 | Many TCs | Tested invalid data, rejected cases, extra spaces, and invalid email formats. |

---

## 4. Software Quality Analysis

### 4.1 Strengths

- The login function works correctly for valid accounts, wrong email, wrong password, and empty input fields.
- The book list is displayed clearly with basic information such as title, author, category, publication year, and status.
- Basic search by book title/author and case-insensitive search work well.
- Basic borrow/return operations can be performed, and book/record status is updated after actions.
- The Librarian can check overdue books, and the system can mark overdue records.
- Some basic permissions work correctly: members cannot see the Members tab and cannot see the reset data button.

### 4.2 Weaknesses

- Serious business-rule bug: the system allows a member to borrow more than 3 books.
- Serious permission bug: a member can look up another member’s borrow records.
- The error message is inaccurate when a suspended member is rejected from borrowing.
- Returning an overdue book does not display the required overdue warning.
- Email validation in member management is inconsistent: the system rejects a valid email but accepts invalid email formats.
- English language switching is incomplete because some categories are still displayed in Vietnamese.
- Search does not handle leading/trailing spaces in keywords.

---

## 5. Recommended Bug Fix Priority

| Priority | Bug | Severity | Reason |
|---:|---|---|---|
| 1 | BUG-06 | High | Related to permission and privacy; members can view other members’ borrow records. |
| 2 | BUG-02 | High | Violates a core business rule: maximum 3 books per member. |
| 3 | BUG-03 | Medium | Overdue returns do not show a warning, reducing the value of overdue handling. |
| 4 | BUG-01 | Medium | Wrong error message can confuse users and librarians about member status. |
| 5 | BUG-04 | Medium | Librarian cannot add a member with a valid email, affecting member management. |
| 6 | BUG-05 | Medium | Invalid email formats can be saved, causing dirty data. |
| 7 | BUG-07 | Low | Search experience issue when users enter extra spaces. |
| 8 | BUG-08 | Low | English UI is not fully translated. |

---

## 6. Conclusion

The system has many basic functions working correctly, especially login, book list display, basic search, and normal borrow/return operations. However, the system is **not ready for release** in a real environment because there are at least 2 High-severity bugs: the system allows borrowing more than 3 books, and a member can view another member’s borrow records. These issues directly affect business rules, security, and access control.

The team should fix the High-severity bugs first, then fix the Medium-severity issues related to overdue handling and member management. After the fixes, regression testing should be performed for all TC-01 → TC-40, especially TC-17, TC-19, TC-23, TC-26, TC-27, and TC-32.

---

## 7. Lessons Learned

- Expected Results must be written clearly according to the SRS, not generally as “the system works normally.”
- Important bugs often appear at boundaries and permission checks, such as the 3-book limit and lookup of another member’s records.
- Negative testing is important because many bugs appear when users enter invalid data or perform actions outside the main flow.
- A bug report should include clear reproduction steps, expected result, actual result, and screenshot evidence.

## 8. Using AI
- The team used ChatGPT to correct the syntax.