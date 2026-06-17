# Bug Reports

| Information | Details |
|---|---|
| **Group** | `<!Group 18>` |
| **Report Date** | `27/05/2026` |
| **System** | https://stqa.rbc.vn |
| **Total Bugs** | 8 |

## Environment

- **Browser:** Chrome
- **Operating System:** Windows 11
- **Interface Language:** Vietnamese / English depending on the test case

---

## BUG-01 — Incorrect error message shown when a suspended member borrows a book

| Attribute | Details |
|---|---|
| **Bug ID** | BUG-01 |
| **Related TC** | TC-17 |
| **Related REQ** | REQ-04 |
| **Severity** | Medium |
| **Detected By** | Phạm Duy Đức Tâm |
| **Detected Date** | 27/05/2026 |
| **Status** | Open |

**Precondition:**  
Log in with the suspended member account `cu.le@email.com / password123`.

**Steps to Reproduce:**
1. Log in using the account `cu.le@email.com`.
2. Go to the book list.
3. Select a book with the Available status.
4. Click the borrow book button.

**Expected Result:**  
The system should reject the borrowing request and display the correct reason: the member is suspended and cannot borrow books.

**Actual Result:**  
The system rejects the borrowing request but displays: `Thành viên đã hết hạn. Không thể mượn sách.`

**Impact:**  
Users and librarians may misunderstand the rejection reason, causing confusion between suspended status and expired membership.

**Evidence:**  
`Bug01.jpg`

**Suggested Fix:**  
Review the handling logic for the `suspended` status and ensure that suspended and expired membership messages are different.

---

## BUG-02 — System allows a member to borrow more than the maximum limit of 3 books

| Attribute | Details |
|---|---|
| **Bug ID** | BUG-02 |
| **Related TC** | TC-19 |
| **Related REQ** | REQ-04 |
| **Severity** | High |
| **Detected By** | Trần Quang Thành |
| **Detected Date** | 27/05/2026 |
| **Status** | Open |

**Precondition:**  
Log in with the member account `ba.nguyen@email.com / password123`.

**Steps to Reproduce:**
1. Log in using `ba.nguyen@email.com`.
2. Go to the book list.
3. Borrow several books that have the Available status.
4. Go to the Borrow / Return tab.
5. Observe the number of active borrowing records.

**Expected Result:**  
When the member has already borrowed 3 books, the system must reject the 4th borrowing request.

**Actual Result:**  
The system still allows Nguyễn Học Bá to borrow 4 books at the same time: BR006, BR007, BR008, BR012.

**Impact:**  
This violates a core business rule and prevents the system from correctly controlling the maximum number of books per member.

**Evidence:**  
`Bug02.jpg`

**Suggested Fix:**  
Before creating a borrowing record, count the member's active borrowing records; if the number is `>= 3`, block the request.

---

## BUG-03 — No overdue warning is displayed when returning an overdue book

| Attribute | Details |
|---|---|
| **Bug ID** | BUG-03 |
| **Related TC** | TC-23 |
| **Related REQ** | REQ-05 |
| **Severity** | Medium |
| **Detected By** | Lê Vân |
| **Detected Date** | 27/05/2026 |
| **Status** | Open |

**Precondition:**  
Log in using `ba.nguyen@email.com / password123`; borrowing record BR001 is overdue.

**Steps to Reproduce:**
1. Log in using `ba.nguyen@email.com`.
2. Go to the Borrow / Return tab.
3. Find borrowing record BR001.
4. Click Return Book.
5. Observe the notification.

**Expected Result:**  
The system should return the book successfully and display an overdue warning because the return date is later than the due date.

**Actual Result:**  
The system only displays `Trả sách thành công.` and does not show any overdue warning.

**Impact:**  
Members/librarians are not informed that the return transaction is overdue, making the overdue warning ineffective.

**Evidence:**  
`Bug03.jpg`

**Suggested Fix:**  
When processing book returns, check whether `returnDate > dueDate`; if true, display an overdue warning.

---

## BUG-04 — System rejects a valid email when adding a new member

| Attribute | Details |
|---|---|
| **Bug ID** | BUG-04 |
| **Related TC** | TC-26 |
| **Related REQ** | REQ-07 |
| **Severity** | Medium |
| **Detected By** | Phạm Duy Đức Tâm |
| **Detected Date** | 27/05/2026 |
| **Status** | Open |

**Precondition:**  
Log in with the librarian account `librarian@library.com / admin123`.

**Steps to Reproduce:**
1. Log in as a librarian.
2. Go to the Members tab.
3. Click Add Member.
4. Enter the full name `Thành thông minh`.
5. Enter the email `thanh.khong@email.com`.
6. Enter the phone number `0972316494`.
7. Click Add Member.

**Expected Result:**  
The system should accept the valid email, create the new member, and display the member in the list.

**Actual Result:**  
The system displays the error `Email không hợp lệ.` and does not allow the member to be added.

**Impact:**  
The librarian cannot add a new member even though the email is in a valid format.

**Evidence:**  
`Bug04.jpg`

**Suggested Fix:**  
Review the email validation regex/logic; emails in the `user@domain.ext` format must be accepted.

---

## BUG-05 — System allows adding a member with an invalid email format

| Attribute | Details |
|---|---|
| **Bug ID** | BUG-05 |
| **Related TC** | TC-27 |
| **Related REQ** | REQ-07 |
| **Severity** | Medium |
| **Detected By** | Lê Vân |
| **Detected Date** | 27/05/2026 |
| **Status** | Open |

**Precondition:**  
Log in as a librarian.

**Steps to Reproduce:**
1. Log in as a librarian.
2. Go to the Members tab.
3. Click Add Member.
4. Enter an invalid email format such as `user@domain`.
5. Enter the remaining valid information.
6. Click Add Member.

**Expected Result:**  
The system should reject the member creation request and display an invalid email error.

**Actual Result:**  
The system still creates a new member with an invalid email format such as `user@domain` or `user1@domain`.

**Impact:**  
Member data may contain invalid email formats, which can cause issues during searching or later processing.

**Evidence:**  
`Bug05.jpg`

**Suggested Fix:**  
Update the email validation so that only complete email formats such as `user@domain.ext` are accepted.

---

## BUG-06 — Member can look up borrowing records of another member

| Attribute | Details |
|---|---|
| **Bug ID** | BUG-06 |
| **Related TC** | TC-32 |
| **Related REQ** | REQ-08 |
| **Severity** | High |
| **Detected By** | Trần Quang Thành |
| **Detected Date** | 27/05/2026 |
| **Status** | Open |

**Precondition:**  
Log in with the member account `dam.tran@email.com / password123`.

**Steps to Reproduce:**
1. Log in using `dam.tran@email.com`.
2. Go to the Borrow / Return tab.
3. Select borrowing record lookup.
4. Enter another member ID `MEM002`.
5. Click Search.

**Expected Result:**  
A member should only be able to view their own borrowing records; the system must reject the request or not display another member's data.

**Actual Result:**  
Trần Dựa Dẫm can still view Nguyễn Học Bá's borrowing records, including BR001 and BR004.

**Impact:**  
This violates access control and user data privacy.

**Evidence:**  
`Bug06.jpg`

**Suggested Fix:**  
When the role is Member, limit queries to the `memberId` of the currently logged-in account and do not allow searching for another member ID.

---

## BUG-07 — Search does not handle leading whitespace in keywords

| Attribute | Details |
|---|---|
| **Bug ID** | BUG-07 |
| **Related TC** | TC-38 |
| **Related REQ** | REQ-03 |
| **Severity** | Low |
| **Detected By** | Phạm Duy Đức Tâm |
| **Detected Date** | 27/05/2026 |
| **Status** | Open |

**Precondition:**  
Log in with a member account.

**Steps to Reproduce:**
1. Log in as a member.
2. Go to the Books tab.
3. Enter a keyword with leading whitespace, for example ` NGUYỄN MINH ĐỨC`.
4. Observe the search result.

**Expected Result:**  
The system should ignore unnecessary whitespace and still display matching books.

**Actual Result:**  
The system displays `Không tìm thấy sách nào.`

**Impact:**  
Users may fail to find books if they accidentally enter extra whitespace.

**Evidence:**  
`Bug07.jpg`

**Suggested Fix:**  
Trim the search keyword before comparing it with book data.

---

## BUG-08 — English interface still displays category names in Vietnamese

| Attribute | Details |
|---|---|
| **Bug ID** | BUG-08 |
| **Related TC** | TC-35 |
| **Related REQ** | General UI / Language Switching |
| **Severity** | Low |
| **Detected By** | Phạm Duy Đức Tâm |
| **Detected Date** | 27/05/2026 |
| **Status** | Open |

**Precondition:**  
The user is already logged in to the system.

**Steps to Reproduce:**
1. Log in using any account.
2. Click the EN button in the top-right corner.
3. Observe the Available categories line under the category filter.

**Expected Result:**  
When English is selected, all interface labels and category names should be displayed in English.

**Actual Result:**  
The Available categories line still displays: `Công nghệ, Giáo dục, Kinh tế, Kỹ năng mềm, Quản trị, Văn học`.

**Impact:**  
The bilingual interface is inconsistent, and the English user experience is incomplete.

**Evidence:**  
`Bug8.jpg`

**Suggested Fix:**  
Add English translations for category names and update them according to the current interface language.

---
