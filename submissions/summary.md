
# Test Summary — Báo cáo tổng hợp kiểm thử

## 1. Thông tin nhóm

| Mục | Thông tin |
|---|---|
| **Nhóm** | `<!Group 18>` |
| **Lớp** | `<!ICT>` |
| **Ngày báo cáo** | 27/05/2026 |
| **Hệ thống kiểm thử** | https://stqa.rbc.vn — v1.0 |
| **Phạm vi** | Manual Black-box Testing dựa trên SRS |

---

## 2. Tổng quan kết quả

| Chỉ số | Giá trị |
|---|---:|
| Tổng số test case | 40 |
| Pass | 32 |
| Fail | 8 |
| Blocked | 0 |
| Not Run | 0 |
| **Tỷ lệ Pass** | **80%** |
| **Số bug phát hiện** | **8** |

> Ghi chú: TC-33 chưa có minh chứng thực thi nên để trạng thái **Not Run**. Nếu nhóm chạy bổ sung và Pass, tỷ lệ Pass sẽ tăng.

### Phân bổ theo nhóm chức năng

| Nhóm chức năng | TC | Pass | Fail | Not Run | Bug | Đánh giá |
|---|---:|---:|---:|---:|---:|---|
| Đăng nhập | 5 | 5 | 0 | 0 | 0 | Hoạt động ổn định |
| Danh sách sách, tìm kiếm, lọc | 9 | 8 | 1 | 0 | 1 | Tìm kiếm cơ bản tốt, lỗi trim khoảng trắng |
| Mượn sách | 7 | 5 | 2 | 0 | 2 | Có lỗi nghiệp vụ quan trọng về giới hạn mượn |
| Trả sách và quá hạn | 5 | 4 | 1 | 0 | 1 | Còn thiếu cảnh báo khi trả quá hạn |
| Quản lý thành viên | 4 | 2 | 2 | 0 | 2 | Validate email chưa nhất quán |
| Phiếu mượn và phân quyền | 4 | 3 | 1 | 0 | 1 | Có lỗi phân quyền nghiêm trọng |
| UI, ngôn ngữ, reset | 6 | 5 | 1 | 0 | 1 | Chuyển ngôn ngữ chưa hoàn chỉnh |

### Phân bổ bug theo mức độ

| Mức độ | Số lượng | Bug IDs |
|---|---:|---|
| High | 2 | BUG-02, BUG-06 |
| Medium | 4 | BUG-01, BUG-03, BUG-04, BUG-05 |
| Low | 2 | BUG-07, BUG-08 |

---

## 3. Kỹ thuật thiết kế đã sử dụng

| Kỹ thuật | Áp dụng cho REQ nào? | Số TC sử dụng | Giải thích cách áp dụng |
|---|---|---:|---|
| EP — Equivalence Partitioning | REQ-01, REQ-03, REQ-07 | Nhiều TC | Chia input thành hợp lệ/không hợp lệ: email tồn tại/không tồn tại, mật khẩu đúng/sai, từ khóa tồn tại/không tồn tại, email hợp lệ/sai định dạng/trùng |
| BVA — Boundary Value Analysis | REQ-04 | TC-19, TC-20 | Kiểm tra giới hạn tối đa 3 sách và hạn trả 14 ngày |
| Decision Table | REQ-04 | TC-14 → TC-18 | Kết hợp điều kiện trạng thái thành viên, trạng thái sách, số sách đang mượn để xác định cho mượn/từ chối |
| Access Control Testing | REQ-07, REQ-08 | TC-25, TC-29 → TC-32, TC-34, TC-40 | Kiểm tra thủ thư và thành viên có quyền truy cập khác nhau |
| State-based Testing | REQ-02, REQ-05, REQ-06 | TC-08, TC-21, TC-24, TC-33 | Kiểm tra chuyển trạng thái sách/phiếu sau mượn, trả, kiểm tra quá hạn, reset |
| Negative / Robustness Testing | REQ-01, REQ-03, REQ-04, REQ-07 | Nhiều TC | Kiểm tra dữ liệu sai, trường hợp bị từ chối, khoảng trắng thừa, email sai format |

---

## 4. Phân tích chất lượng phần mềm

### 4.1. Điểm mạnh

- Chức năng đăng nhập hoạt động đúng với tài khoản hợp lệ, sai email, sai mật khẩu và bỏ trống input.
- Danh sách sách hiển thị rõ ràng, có đủ thông tin cơ bản như tên sách, tác giả, thể loại, năm xuất bản và trạng thái.
- Tìm kiếm cơ bản theo tên sách/tác giả và không phân biệt hoa/thường hoạt động tốt.
- Chức năng mượn/trả cơ bản có thể thao tác được, trạng thái sách/phiếu được cập nhật sau thao tác.
- Thủ thư có thể kiểm tra quá hạn và hệ thống đánh dấu được phiếu quá hạn.
- Một số phân quyền cơ bản đúng: member không thấy tab Thành viên, không thấy nút khôi phục dữ liệu.

### 4.2. Điểm yếu

- Lỗi nghiệp vụ nghiêm trọng: hệ thống cho phép mượn vượt quá giới hạn 3 sách/thành viên.
- Lỗi phân quyền nghiêm trọng: thành viên có thể tra cứu phiếu mượn của thành viên khác.
- Thông báo lỗi chưa chính xác khi thành viên tạm ngưng bị từ chối mượn sách.
- Trả sách quá hạn không hiển thị cảnh báo quá hạn như yêu cầu.
- Validate email trong chức năng thêm thành viên không nhất quán: vừa từ chối email hợp lệ, vừa cho phép email sai định dạng.
- Chuyển ngôn ngữ EN chưa đầy đủ, danh mục thể loại vẫn hiển thị tiếng Việt.
- Tìm kiếm chưa xử lý khoảng trắng thừa ở đầu/cuối từ khóa.

---

## 5. Đề xuất ưu tiên sửa lỗi

| Thứ tự | Bug | Mức độ | Lý do ưu tiên |
|---:|---|---|---|
| 1 | BUG-06 | High | Liên quan phân quyền và quyền riêng tư; thành viên xem được phiếu người khác |
| 2 | BUG-02 | High | Vi phạm quy tắc nghiệp vụ cốt lõi: tối đa 3 sách/thành viên |
| 3 | BUG-03 | Medium | Trả sách quá hạn không cảnh báo, làm mất ý nghĩa xử lý quá hạn |
| 4 | BUG-01 | Medium | Thông báo sai lý do khiến thủ thư/người dùng hiểu nhầm trạng thái thành viên |
| 5 | BUG-04 | Medium | Không thêm được thành viên với email hợp lệ, ảnh hưởng nghiệp vụ quản lý thành viên |
| 6 | BUG-05 | Medium | Cho phép lưu email sai định dạng, gây dữ liệu bẩn |
| 7 | BUG-07 | Low | Lỗi trải nghiệm tìm kiếm khi nhập khoảng trắng thừa |
| 8 | BUG-08 | Low | Giao diện tiếng Anh chưa dịch hoàn chỉnh |

---

## 6. Kết luận

Hệ thống có nhiều chức năng cơ bản hoạt động tốt, đặc biệt là đăng nhập, hiển thị danh sách sách, tìm kiếm cơ bản và thao tác mượn/trả thông thường. Tuy nhiên, hệ thống **chưa sẵn sàng phát hành** nếu dùng trong môi trường thật vì còn ít nhất 2 lỗi mức High: cho phép mượn vượt giới hạn 3 sách và thành viên có thể xem phiếu mượn của người khác. Hai lỗi này ảnh hưởng trực tiếp đến nghiệp vụ và bảo mật/phân quyền.

Đề xuất sửa các lỗi High trước, sau đó sửa các lỗi Medium liên quan đến quá hạn và quản lý thành viên. Sau khi sửa, cần chạy regression test lại toàn bộ TC-01 → TC-40, đặc biệt là TC-17, TC-19, TC-23, TC-26, TC-27 và TC-32.

---

## 7. Bài học rút ra

- Expected Result phải viết cụ thể theo SRS, không viết chung chung như “hệ thống hoạt động bình thường”.
- Các lỗi quan trọng thường nằm ở boundary và phân quyền, ví dụ giới hạn 3 sách và tra cứu phiếu của người khác.
- Negative testing rất quan trọng vì nhiều bug xuất hiện khi nhập dữ liệu sai hoặc thao tác ngoài luồng chính.
- Khi ghi bug report, cần có bước tái hiện rõ ràng, expected vs actual và minh chứng ảnh chụp màn hình.

## 8. Khai báo sử dụng AI
- Nhóm đã dùng chat GPT để sửa cú pháp .