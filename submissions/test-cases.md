# Test Cases

| Information | |
|---|---|
| **Group** | `<!Group 18>` |
| **Created Date** | `27/05/2026` |
| **System** | https://stqa.rbc.vn |
| **Reference** | SRS v1.0 |

---

## 1. Input Domain Modeling — IDM

### IDM — REQ-01 Login

| Characteristic | Partition | Representative Value | Expected Result |
|---|---|---|---|
| Existing email? | Yes | `librarian@library.com`, `ba.nguyen@email.com` | Login succeeds if the password is correct. |
| Existing email? | No | `nobody@test.com` | Show error: `Member not found`. |
| Correct password? | Correct | `admin123`, `password123` | Login succeeds. |
| Correct password? | Incorrect | `wrongpassword` | Show error: `Incorrect password`. |
| Empty fields? | Empty email and password | `"" / ""` | Show error: `Please enter email and password`. |

### IDM — REQ-02 View Book List

| Characteristic | Partition | Representative Value | Expected Result |
|---|---|---|---|
| User role | Librarian | `librarian@library.com` | Can view the book list and detailed book information. |
| User role | Member | `ba.nguyen@email.com` | Can view the book list. |
| Book status | After borrowing | `BOOK001` | Book status is updated correctly. |

### IDM — REQ-03 Search and Filter Books

| Characteristic | Partition | Representative Value | Expected Result |
|---|---|---|---|
| Existing keyword by book title | Yes | `Flutter` | Matching books by title are displayed. |
| Existing keyword by author | Yes | `Nguyễn Minh Đức` | Books by the matching author are displayed. |
| Non-existing keyword | No | `xyz123` | A “No books found” message is displayed. |
| Case sensitivity | Different uppercase/lowercase input | `Flutter`, `flutter`, `NGUYỄN MINH ĐỨC` | Results are still correct because search is case-insensitive. |
| Extra spaces | Leading/trailing spaces | ` NGUYỄN MINH ĐỨC` | The system should ignore extra spaces. |
| Category | Existing category in seed data | `Công nghệ` | Only books in the Technology category are displayed. |

### IDM — REQ-04 Borrow Book

| Characteristic | Partition | Representative Value | Expected Result |
|---|---|---|---|
| Book status | Available | `BOOK001` | Borrowing is allowed if the member is valid. |
| Book status | Borrowed | `BOOK003` | Borrowing is rejected. |
| Book status | Unavailable/lost | `BOOK007` | Borrowing is rejected. |
| Member status | Active | `MEM006` | Borrowing is allowed. |
| Member status | Suspended | `MEM004` | Borrowing is rejected with the correct suspended-member reason. |
| Member status | Expired | `MEM005` | Borrowing is rejected with the correct expired-member reason. |
| Number of borrowed books | < 3 | 0, 1, 2 books | Borrowing is allowed. |
| Number of borrowed books | = 3 or > 3 | 3, 4 books | Borrowing more books is rejected. |
| Due date | Borrow date + 14 days | Successfully borrowed book | The due date is calculated correctly. |

### IDM — REQ-05 Return Book

| Characteristic | Partition | Representative Value | Expected Result |
|---|---|---|---|
| Return book | Active borrow record | `BR003` | Returning the book is allowed. |
| Return book | Already returned record | `BR002` | Returning the same record again is not allowed. |
| Overdue return | returnDate > dueDate | `BR001` | An overdue warning is displayed. |

### IDM — REQ-06 Handle Overdue Books

| Characteristic | Partition | Representative Value | Expected Result |
|---|---|---|---|
| User role | Librarian | `librarian@library.com` | Can click **Check Overdue Books**. |
| User role | Member | `ba.nguyen@email.com` | Cannot check overdue books for the whole system. |
| Borrow record status | Not overdue | Due date is later than the current date | The record is not marked as **Overdue**. |
| Borrow record status | Overdue | `BR003` has a due date before the current date | The record is marked as **Overdue**. |
| Update result | At least one overdue record | `BR003` | The number of updated overdue records is displayed. |

### IDM — REQ-07 Member Management

| Characteristic | Partition | Representative Value | Expected Result |
|---|---|---|---|
| User role | Librarian | `librarian@library.com` | Can access the **Members** tab. |
| User role | Member | `ba.nguyen@email.com` | Cannot access member management functions. |
| New email | Valid email | `thanh.khong@email.com` | A new member is created successfully. |
| New email | Invalid email format | `user@domain` | The input is rejected with an invalid email error. |
| New email | Existing email | `ba.nguyen@email.com` | The input is rejected because the email already exists. |

### IDM — REQ-08 Borrow Record Lookup / Permission

| Characteristic | Partition | Representative Value | Expected Result |
|---|---|---|---|
| User role | Librarian | `librarian@library.com` | Can view all borrow records. |
| User role | Member | `ba.nguyen@email.com` | Can only view their own borrow records. |
| Borrow record lookup | Look up own records | `MEM002` when logged in as `MEM002` | Records of Nguyễn Học Bá are displayed. |
| Borrow record lookup | Look up another member | `MEM002` when logged in as `MEM003` | The request is rejected or no other member’s data is displayed. |
| Data permission | Librarian searches any member ID | `MEM002`, `MEM003` | Correct borrow records are displayed for the selected member ID. |

---

## 2. Decision Table — Borrow Book Function

| Rule | Active member? | Book available? | Borrowed books < 3? | Result |
|---|---|---|---|---|
| R1 | Yes | Yes | Yes | Allow borrowing. |
| R2 | Yes | No | Yes | Reject because the book is unavailable. |
| R3 | Yes | Yes | No | Reject because the member exceeds the 3-book limit. |
| R4 | Suspended | Yes | Yes | Reject because the member is suspended. |
| R5 | Expired | Yes | Yes | Reject because the member has expired. |

---

## 3. Test Cases Grouped by Requirement

### REQ-01 — Login

| TC ID | Test Objective | Technique |
|---|---|---|
| TC-01 | Successful login with a Librarian account | EP |
| TC-02 | Successful login with a Member account | EP |
| TC-03 | Failed login with a non-existing email | EP, Negative |
| TC-04 | Failed login with an incorrect password | EP, Negative |
| TC-05 | Failed login with empty email and password | EP, Negative |

### REQ-02 — View Book List

| TC ID | Test Objective | Technique |
|---|---|---|
| TC-06 | Librarian can view the book list and book information | EP |
| TC-07 | Member can view the book list | Access Control |
| TC-08 | Book status is updated after borrowing | State-based |

### REQ-03 — Search and Filter Books

| TC ID | Test Objective | Technique |
|---|---|---|
| TC-09 | Search by book title | EP |
| TC-10 | Search by author | EP |
| TC-11 | Search is case-insensitive | EP |
| TC-12 | Search with a non-existing keyword | EP, Negative |
| TC-13 | Filter by Technology category | EP |
| TC-37 | Search using an uppercase author name | EP |
| TC-38 | Search handles leading/trailing spaces | Robustness, Negative |
| TC-39 | Filter by Technology category | EP |

### REQ-04 — Borrow Book

| TC ID | Test Objective | Technique |
|---|---|---|
| TC-14 | Borrow a book successfully with an active member | Decision Table |
| TC-15 | Reject borrowing a book that is already borrowed | Decision Table, Negative |
| TC-16 | Reject borrowing an unavailable/lost book | Decision Table, Negative |
| TC-17 | Suspended member cannot borrow books | Decision Table, Negative |
| TC-18 | Expired member cannot borrow books | Decision Table, Negative |
| TC-19 | Do not allow borrowing more than 3 books | BVA |
| TC-20 | Due date equals borrow date + 14 days | BVA |

### REQ-05 — Return Book

| TC ID | Test Objective | Technique |
|---|---|---|
| TC-21 | Return an active borrowed book successfully | EP |
| TC-22 | Do not allow returning an already returned record again | Negative |
| TC-23 | Overdue return must display a warning | EP, Negative |

### REQ-06 — Handle Overdue Books

| TC ID | Test Objective | Technique |
|---|---|---|
| TC-24 | Librarian checks and marks overdue records | State-based |
| TC-25 | Member only sees their own overdue records | Access Control |

### REQ-07 — Member Management

| TC ID | Test Objective | Technique |
|---|---|---|
| TC-26 | Librarian adds a member with a valid email | EP |
| TC-27 | Reject an invalid email format | EP, Negative |
| TC-28 | Reject an already existing email | EP, Negative |
| TC-29 | Regular member cannot access member management | Access Control |
| TC-40 | Member cannot see the Members tab | Access Control |

### REQ-08 — Borrow Record Lookup / Permission

| TC ID | Test Objective | Technique |
|---|---|---|
| TC-30 | Librarian can view all seed borrow records | Access Control |
| TC-31 | Member MEM002 can view their own records | Access Control |
| TC-32 | Member cannot view another member’s records | Access Control, Negative |
| TC-34 | Member cannot reset system data | Access Control |

### General UI / System

| TC ID | Test Objective | Note |
|---|---|---|
| TC-33 | Librarian resets data to seed data | General system function |
| TC-35 | Switch the interface fully to English | General UI |
| TC-36 | Switch the interface back to Vietnamese | General UI |

---

## 4. Test Case Summary by Requirement

| REQ | Function | Test Cases |
|---|---|---|
| REQ-01 | Login | TC-01 → TC-05 |
| REQ-02 | View Book List | TC-06 → TC-08 |
| REQ-03 | Search and Filter Books | TC-09 → TC-13, TC-37 → TC-39 |
| REQ-04 | Borrow Book | TC-14 → TC-20 |
| REQ-05 | Return Book | TC-21 → TC-23 |
| REQ-06 | Handle Overdue Books | TC-24 → TC-25 |
| REQ-07 | Member Management | TC-26 → TC-29, TC-40 |
| REQ-08 | Borrow Record Lookup / Permission | TC-30 → TC-32, TC-34 |
| General | UI / System | TC-33, TC-35, TC-36 |

---

## 5. Coverage Summary

| Feature Group | # TCs | REQ Coverage | Techniques Applied |
|---|---:|---|---|
| Login | 5 | REQ-01 | EP, Negative |
| View Book List | 3 | REQ-02 | EP, Access Control, State-based |
| Search & Filter Books | 8 | REQ-03 | EP, Robustness, Negative |
| Borrow Book | 7 | REQ-04 | BVA, Decision Table, Negative |
| Return Book | 3 | REQ-05 | EP, Negative |
| Overdue Handling | 2 | REQ-06 | State-based, Access Control |
| Member Management | 5 | REQ-07 | EP, Access Control, Negative |
| Borrow Record Lookup / Permission | 4 | REQ-08 | Access Control, Negative |
| General UI / System | 3 | General | UI, State-based |
| **Total** | **40** | **REQ-01 → REQ-08 + General** | **EP, BVA, Decision Table, Access Control, State-based, Negative, Robustness, UI** |
