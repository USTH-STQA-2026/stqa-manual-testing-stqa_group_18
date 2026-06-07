# Test Execution Results

| Information | |
|---|---|
| **Group** | `<Group 18>` |
| **Execution Date** | `27/05/2026` |
| **Browser** | Chrome |
| **Operating System** | Windows 11 |
| **System** | https://stqa.rbc.vn |

---

## 1. Detailed Results

| TC ID | Feature Group | Expected Result Summary | Actual Result | Status | Evidence | Bug |
|---|---|---|---|---|---|---|
| TC-01 | Login | Navigate to the main page; AppBar shows Nguyễn Thủ Thư (Librarian). | Librarian login succeeded. AppBar shows Nguyễn Thủ Thư (Librarian). | Pass |  | - |
| TC-02 | Login | Navigate to the main page; AppBar shows Nguyễn Học Bá (Member). | Member login succeeded. AppBar shows Nguyễn Học Bá (Member). | Pass |  | - |
| TC-03 | Login | Display the error “Member not found.” | The system displays “Member not found.” | Pass |  | - |
| TC-04 | Login | Display the error “Incorrect password.” | The system displays “Incorrect password.” | Pass |  | - |
| TC-05 | Login | Display the error “Please enter email and password.” | The system displays “Please enter email and password.” | Pass |  | - |
| TC-06 | Book List | BOOK001 shows title, author, category, publication year, and status. | Librarian can view the book list; BOOK001 shows title, author, category, year, and Available status. | Pass |  | - |
| TC-07 | Book List | Member can view the book list. | Member can view the book list after logging in. | Pass |  | - |
| TC-08 | Book Status Update | BOOK001 changes from Available to Borrowed immediately. | After Hoàng Cá Biệt borrows BOOK001, BOOK001 status changes to Borrowed. | Pass |  | - |
| TC-09 | Search Books | Display “Basic Flutter Programming” — BOOK001. | Searching for “Basic Flutter Programming” displays BOOK001 correctly. | Pass |  | - |
| TC-10 | Search Books | Display books by Nguyễn Minh Đức, including BOOK001 and BOOK009. | Searching for Nguyễn Minh Đức displays BOOK001 and BOOK009. | Pass |  | - |
| TC-11 | Search Books | Both searches return equivalent results, including BOOK001. | Searching for lowercase “flutter” still displays “Basic Flutter Programming.” | Pass |  | - |
| TC-12 | Search Books | Display “No books found.” | Searching for xyz123 displays “No books found.” | Pass |  | - |
| TC-13 | Filter Books | Only books in the Technology category are displayed. | Filtering by Technology displays books in the Technology category. | Pass |  | - |
| TC-14 | Borrow Book | Display “Book borrowed successfully” and create a borrow record. | Hoàng Cá Biệt borrows BOOK001 successfully; the system displays “Book borrowed successfully.” | Pass |  | - |
| TC-15 | Borrow Book | The system does not allow borrowing a book that is already borrowed. | When trying to borrow an already borrowed book, the system rejects the request. | Pass |  | - |
| TC-16 | Borrow Book | The system does not allow borrowing an unavailable book. | When trying to borrow an unavailable/lost book, the system rejects the request. | Pass |  | - |
| TC-17 | Borrow Book | Reject borrowing and display the correct reason: the member is suspended. | The suspended member is rejected, but the system shows the wrong message: “Member has expired. Cannot borrow books.” | Fail | Bug01.jpg | BUG-01 |
| TC-18 | Borrow Book | Reject borrowing and display the reason that the member has expired. | The expired member is rejected and the system displays “Member has expired. Cannot borrow books.” | Pass |  | - |
| TC-19 | Borrow Limit | The 4th book is rejected because the maximum limit is 3 books. | Nguyễn Học Bá can still borrow 4 books at the same time: BR006, BR007, BR008, BR012. | Fail | Bug02.jpg | BUG-02 |
| TC-20 | Due Date | Due date = borrow date + 14 days. | The new borrow record has borrow date 27/05/2026 and due date 10/06/2026, correctly +14 days. | Pass |  | - |
| TC-21 | Return Book | Display “Book returned successfully”; the record becomes Returned and the book becomes Available. | The system displays “Book returned successfully”; the record changes to Returned. | Pass |  | - |
| TC-22 | Return Book | Returned records do not have the Return button again. | Returned records only show the Returned status and do not have a Return button. | Pass |  | - |
| TC-23 | Overdue Return | Return succeeds and an overdue warning is displayed. | BR001 is returned late, but the system only displays “Book returned successfully” without any overdue warning. | Fail | Bug03.jpg | BUG-03 |
| TC-24 | Overdue Check | Overdue records are marked as Overdue, and the number of updated records is displayed. | Librarian clicks Check Overdue Books; the system reports 1 overdue record updated and BR003 becomes Overdue. | Pass |  | - |
| TC-25 | Overdue Records | Only the logged-in member’s overdue records are displayed. | Hoàng Cá Biệt only sees their own overdue record BR003. | Pass |  | - |
| TC-26 | Member Management | A new member is created successfully and appears in the list. | A valid email `thanh.khong@email.com` is entered, but the system shows “Invalid email.” | Fail | Bug04.jpg | BUG-04 |
| TC-27 | Member Management | Reject member creation and display an invalid email error. | The system still creates a new member with invalid email formats `user@domain` and `user1@domain`. | Fail | Bug05.jpg | BUG-05 |
| TC-28 | Member Management | Do not create a new member; report that the email already exists. | Existing email `ba.nguyen@email.com` is rejected, and no new member is created. | Pass |  | - |
| TC-29 | Member Permission | Member cannot see or access the Members function. | Member account cannot see/access the Members tab. | Pass |  | - |
| TC-30 | Borrow Records | Display all seed borrow records BR001 to BR005. | Librarian can see all seed records BR001 to BR005. | Pass |  | - |
| TC-31 | Borrow Records | Display Nguyễn Học Bá’s records such as BR001 and BR004. | Looking up MEM002 displays Nguyễn Học Bá’s records, including BR001 and BR004. | Pass |  | - |
| TC-32 | Borrow Record Permission | The system rejects or hides another member’s borrow records. | Logged in as Trần Dựa Dẫm, but the user can still look up and view records of MEM002. | Fail | Bug06.jpg | BUG-06 |
| TC-33 | Data Reset | Books, borrow records, and members return to the original seed data. | Not executed / no execution evidence. | Not Run | - | - |
| TC-34 | Permission | Member cannot see the data reset button. | Logged in as a member; the reset data button is not shown on the AppBar. | Pass |  | - |
| TC-35 | Language Switching | All UI labels and categories are switched to English. | EN is selected, but Available categories still shows Vietnamese categories: Công nghệ, Giáo dục, Kinh tế, Kỹ năng mềm, Quản trị, Văn học. | Fail | Bug07.jpg | BUG-07 |
| TC-36 | Language Switching | The interface switches fully back to Vietnamese. | VI is selected, and the interface switches back to Vietnamese. | Pass |  | - |
| TC-37 | Search Books | Display books by Nguyễn Minh Đức. | Entering NGUYỄN MINH ĐỨC still displays books by Nguyễn Minh Đức. | Pass |  | - |
| TC-38 | Search Books | The system ignores extra spaces and displays matching books. | Entering a keyword with a leading space displays “No books found.” | Fail | Bug08.jpg | BUG-08 |
| TC-39 | Filter Books | Display books in the Technology category. | Entering Technology in the category filter displays books in the Technology category. | Pass |  | - |
| TC-40 | Permission | The Members tab is not shown for member accounts. | Logged in as a member; the bottom navigation bar does not show the Members tab. | Pass | | - |

---

## 2. Result Summary

| Metric | Value |
|---|---:|
| Total test cases | 40 |
| Pass | 31 |
| Fail | 8 |
| Blocked | 0 |
| **Pass Rate** | **80%** |
| Bugs found | 8 |

### Results by Feature Group

| Feature Group | Total TC | Pass | Fail | Not Run | Evaluation |
|---|---:|---:|---:|---:|---|
| Login | 5 | 5 | 0 | 0 | Stable |
| Book list / search / filter | 9 | 8 | 1 | 0 | Basic functions work well; search does not trim leading/trailing spaces. |
| Borrow Book | 7 | 5 | 2 | 0 | Serious issues with borrow limit and member status message. |
| Return Book / Overdue | 5 | 4 | 1 | 0 | Missing overdue warning when returning an overdue book. |
| Member Management | 4 | 2 | 2 | 0 | Email validation is incorrect. |
| Borrow Records / Permission | 4 | 3 | 1 | 0 | Security issue in borrow-record permission. |
| UI / Language / Reset | 6 | 4 | 1 | 0 | Language switching is incomplete; TC-33 was not executed. |
