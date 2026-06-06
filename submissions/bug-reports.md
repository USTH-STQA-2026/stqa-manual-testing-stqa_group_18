
# Bug Reports — Báo cáo lỗi

| Thông tin | |
|---|---|
| **Nhóm** | `<!Group 18>` |
| **Ngày báo cáo** | `27/05/2026` |
| **Hệ thống** | https://stqa.rbc.vn |
| **Tổng số bug** | 8 |

---


## BUG-01

| Thuộc tính | Chi tiết |
|---|---|
| **Mã lỗi** | BUG-01 |
| **TC liên quan** | TC-17 |
| **REQ liên quan** | REQ-04 |
| **Mức độ** | Medium |
| **Người phát hiện** | Phạm Duy Đức Tâm |
| **Ngày phát hiện** | 27/05/2026 |
| **Trạng thái** | Open |

**Tiêu đề:**  
Thông báo lỗi sai lý do khi thành viên tạm ngưng mượn sách

**Môi trường:**
- Trình duyệt: Chrome
- Hệ điều hành: Windows 11
- Ngôn ngữ giao diện: Tiếng Việt / English tùy TC

**Điều kiện tiên quyết:**  
Đăng nhập bằng tài khoản thành viên tạm ngưng `cu.le@email.com / password123`.

**Bước tái hiện:**
1. Đăng nhập bằng tài khoản `cu.le@email.com`.
2. Vào danh sách sách.
3. Chọn một sách có trạng thái Có sẵn.
4. Nhấn nút mượn sách.

**Kết quả mong đợi:**  
Hệ thống từ chối mượn sách và hiển thị đúng lý do: thành viên đang bị tạm ngưng, không thể mượn sách.

**Kết quả thực tế:**  
Hệ thống từ chối mượn sách nhưng hiển thị: `Thành viên đã hết hạn. Không thể mượn sách.`

**Tác động:**  
Người dùng và thủ thư bị hiểu sai lý do từ chối, gây nhầm lẫn giữa trạng thái tạm ngưng và hết hạn.

**Minh chứng:**  
`Bug01.jpg`

**Đề xuất xử lý:**  
Kiểm tra lại nhánh xử lý trạng thái `suspended`, đảm bảo thông báo tạm ngưng và hết hạn khác nhau.

---


## BUG-02

| Thuộc tính | Chi tiết |
|---|---|
| **Mã lỗi** | BUG-02 |
| **TC liên quan** | TC-19 |
| **REQ liên quan** | REQ-04 |
| **Mức độ** | High |
| **Người phát hiện** | Trần Quang Thành |
| **Ngày phát hiện** | 27/05/2026 |
| **Trạng thái** | Open |

**Tiêu đề:**  
Hệ thống cho phép thành viên mượn vượt quá giới hạn tối đa 3 sách

**Môi trường:**
- Trình duyệt: Chrome
- Hệ điều hành: Windows 11
- Ngôn ngữ giao diện: Tiếng Việt / English tùy TC

**Điều kiện tiên quyết:**  
Đăng nhập bằng tài khoản thành viên `ba.nguyen@email.com / password123`.

**Bước tái hiện:**
1. Đăng nhập bằng `ba.nguyen@email.com`.
2. Vào danh sách sách.
3. Mượn liên tiếp các sách còn trạng thái Có sẵn.
4. Vào tab Mượn / Trả.
5. Quan sát số phiếu đang mượn.

**Kết quả mong đợi:**  
Khi thành viên đã mượn đủ 3 sách, hệ thống phải từ chối mượn sách thứ 4.

**Kết quả thực tế:**  
Hệ thống vẫn cho Nguyễn Học Bá mượn 4 sách cùng lúc: BR006, BR007, BR008, BR012.

**Tác động:**  
Vi phạm quy tắc nghiệp vụ chính, làm hệ thống không kiểm soát được giới hạn số sách mỗi thành viên.

**Minh chứng:**  
`Bug02.jpg`

**Đề xuất xử lý:**  
Trước khi tạo phiếu mượn, đếm số phiếu trạng thái đang mượn của member; nếu `>= 3` thì chặn.

---


## BUG-03

| Thuộc tính | Chi tiết |
|---|---|
| **Mã lỗi** | BUG-03 |
| **TC liên quan** | TC-23 |
| **REQ liên quan** | REQ-05 |
| **Mức độ** | Medium |
| **Người phát hiện** | Lê Vân |
| **Ngày phát hiện** | 27/05/2026 |
| **Trạng thái** | Open |

**Tiêu đề:**  
Trả sách quá hạn nhưng hệ thống không hiển thị cảnh báo quá hạn

**Môi trường:**
- Trình duyệt: Chrome
- Hệ điều hành: Windows 11
- Ngôn ngữ giao diện: Tiếng Việt / English tùy TC

**Điều kiện tiên quyết:**  
Đăng nhập bằng `ba.nguyen@email.com / password123`, phiếu BR001 quá hạn.

**Bước tái hiện:**
1. Đăng nhập bằng `ba.nguyen@email.com`.
2. Vào tab Mượn / Trả.
3. Tìm phiếu BR001.
4. Nhấn Trả sách.
5. Quan sát thông báo.

**Kết quả mong đợi:**  
Hệ thống trả sách thành công và hiển thị cảnh báo quá hạn vì ngày trả sau hạn trả.

**Kết quả thực tế:**  
Hệ thống chỉ hiển thị `Trả sách thành công.`, không có cảnh báo quá hạn.

**Tác động:**  
Thành viên/thủ thư không biết giao dịch trả sách bị quá hạn, làm mất ý nghĩa cảnh báo quá hạn.

**Minh chứng:**  
`Bug03.jpg`

**Đề xuất xử lý:**  
Khi xử lý trả sách, kiểm tra `returnDate > dueDate`; nếu đúng, hiển thị cảnh báo quá hạn.

---


## BUG-04

| Thuộc tính | Chi tiết |
|---|---|
| **Mã lỗi** | BUG-04 |
| **TC liên quan** | TC-26 |
| **REQ liên quan** | REQ-07 |
| **Mức độ** | Medium |
| **Người phát hiện** | Phạm Duy Đức Tâm |
| **Ngày phát hiện** | 27/05/2026 |
| **Trạng thái** | Open |

**Tiêu đề:**  
Hệ thống từ chối email hợp lệ khi thêm thành viên mới

**Môi trường:**
- Trình duyệt: Chrome
- Hệ điều hành: Windows 11
- Ngôn ngữ giao diện: Tiếng Việt / English tùy TC

**Điều kiện tiên quyết:**  
Đăng nhập bằng thủ thư `librarian@library.com / admin123`.

**Bước tái hiện:**
1. Đăng nhập thủ thư.
2. Vào tab Thành viên.
3. Nhấn thêm thành viên.
4. Nhập họ tên `Thành thông minh`.
5. Nhập email `thanh.khong@email.com`.
6. Nhập SĐT `0972316494`.
7. Nhấn Thêm thành viên.

**Kết quả mong đợi:**  
Hệ thống chấp nhận email hợp lệ, tạo thành viên mới và hiển thị trong danh sách.

**Kết quả thực tế:**  
Hệ thống hiển thị lỗi `Email không hợp lệ.` và không cho thêm thành viên.

**Tác động:**  
Thủ thư không thể thêm thành viên mới dù nhập email đúng định dạng.

**Minh chứng:**  
`Bug04.jpg`

**Đề xuất xử lý:**  
Kiểm tra lại regex/logic validate email; email dạng `user@domain.ext` phải được chấp nhận.

---


## BUG-05

| Thuộc tính | Chi tiết |
|---|---|
| **Mã lỗi** | BUG-05 |
| **TC liên quan** | TC-27 |
| **REQ liên quan** | REQ-07 |
| **Mức độ** | Medium |
| **Người phát hiện** | Lê Vân |
| **Ngày phát hiện** | 27/05/2026 |
| **Trạng thái** | Open |

**Tiêu đề:**  
Hệ thống cho phép thêm thành viên với email sai định dạng

**Môi trường:**
- Trình duyệt: Chrome
- Hệ điều hành: Windows 11
- Ngôn ngữ giao diện: Tiếng Việt / English tùy TC

**Điều kiện tiên quyết:**  
Đăng nhập bằng thủ thư.

**Bước tái hiện:**
1. Đăng nhập thủ thư.
2. Vào tab Thành viên.
3. Nhấn thêm thành viên.
4. Nhập email sai định dạng `user@domain`.
5. Nhập dữ liệu còn lại hợp lệ.
6. Nhấn Thêm thành viên.

**Kết quả mong đợi:**  
Hệ thống từ chối tạo thành viên và hiển thị lỗi email không hợp lệ.

**Kết quả thực tế:**  
Hệ thống vẫn tạo thành viên mới với email sai định dạng `user@domain` hoặc `user1@domain`.

**Tác động:**  
Dữ liệu thành viên có thể bị sai định dạng, gây lỗi khi tra cứu/xử lý về sau.

**Minh chứng:**  
`Bug05.jpg`

**Đề xuất xử lý:**  
Cập nhật validate email để chỉ chấp nhận định dạng đầy đủ `user@domain.ext`.

---


## BUG-06

| Thuộc tính | Chi tiết |
|---|---|
| **Mã lỗi** | BUG-06 |
| **TC liên quan** | TC-32 |
| **REQ liên quan** | REQ-08 |
| **Mức độ** | High |
| **Người phát hiện** | Trần Quang Thành |
| **Ngày phát hiện** | 27/05/2026 |
| **Trạng thái** | Open |

**Tiêu đề:**  
Thành viên có thể tra cứu phiếu mượn của thành viên khác

**Môi trường:**
- Trình duyệt: Chrome
- Hệ điều hành: Windows 11
- Ngôn ngữ giao diện: Tiếng Việt / English tùy TC

**Điều kiện tiên quyết:**  
Đăng nhập bằng tài khoản thành viên `dam.tran@email.com / password123`.

**Bước tái hiện:**
1. Đăng nhập bằng `dam.tran@email.com`.
2. Vào tab Mượn / Trả.
3. Chọn Tra cứu phiếu mượn.
4. Nhập mã thành viên khác `MEM002`.
5. Nhấn Tra cứu.

**Kết quả mong đợi:**  
Thành viên chỉ được xem phiếu mượn của chính mình; hệ thống phải từ chối hoặc không hiển thị dữ liệu người khác.

**Kết quả thực tế:**  
Trần Dựa Dẫm vẫn xem được phiếu của Nguyễn Học Bá gồm BR001 và BR004.

**Tác động:**  
Vi phạm phân quyền và quyền riêng tư dữ liệu người dùng.

**Minh chứng:**  
`Bug06.jpg`

**Đề xuất xử lý:**  
Khi role là Member, giới hạn truy vấn theo memberId của tài khoản đang đăng nhập; không cho nhập mã người khác.

---


## BUG-07

| Thuộc tính | Chi tiết |
|---|---|
| **Mã lỗi** | BUG-07 |
| **TC liên quan** | TC-38 |
| **REQ liên quan** | REQ-03 |
| **Mức độ** | Low |
| **Người phát hiện** | Phạm Duy Đức Tâm |
| **Ngày phát hiện** | 27/05/2026 |
| **Trạng thái** | Open |

**Tiêu đề:**  
Tìm kiếm không xử lý khoảng trắng thừa ở đầu từ khóa

**Môi trường:**
- Trình duyệt: Chrome
- Hệ điều hành: Windows 11
- Ngôn ngữ giao diện: Tiếng Việt / English tùy TC

**Điều kiện tiên quyết:**  
Đăng nhập bằng tài khoản thành viên.

**Bước tái hiện:**
1. Đăng nhập thành viên.
2. Vào tab Sách.
3. Nhập từ khóa có khoảng trắng đầu, ví dụ ` NGUYỄN MINH ĐỨC`.
4. Quan sát kết quả.

**Kết quả mong đợi:**  
Hệ thống nên bỏ qua khoảng trắng thừa và vẫn hiển thị các sách phù hợp.

**Kết quả thực tế:**  
Hệ thống hiển thị `Không tìm thấy sách nào.`

**Tác động:**  
Người dùng dễ không tìm thấy sách nếu vô tình nhập thừa khoảng trắng.

**Minh chứng:**  
`Bug07.jpg`

**Đề xuất xử lý:**  
Trim từ khóa tìm kiếm trước khi so sánh.

---


## BUG-08

| Thuộc tính | Chi tiết |
|---|---|
| **Mã lỗi** | BUG-08 |
| **TC liên quan** | TC-35 |
| **REQ liên quan** | General UI / Language Switching |
| **Mức độ** | Low |
| **Người phát hiện** | Phạm Duy Đức Tâm |
| **Ngày phát hiện** | 27/05/2026 |
| **Trạng thái** | Open |

**Tiêu đề:**  
Giao diện tiếng Anh vẫn hiển thị danh mục thể loại bằng tiếng Việt

**Môi trường:**
- Trình duyệt: Chrome
- Hệ điều hành: Windows 11
- Ngôn ngữ giao diện: Tiếng Việt / English tùy TC

**Điều kiện tiên quyết:**  
Đã đăng nhập vào hệ thống.

**Bước tái hiện:**
1. Đăng nhập bằng tài khoản bất kỳ.
2. Nhấn nút EN ở góc trên bên phải.
3. Quan sát dòng Available categories dưới ô lọc thể loại.

**Kết quả mong đợi:**  
Khi chọn tiếng Anh, toàn bộ nhãn giao diện và danh mục thể loại phải hiển thị bằng tiếng Anh.

**Kết quả thực tế:**  
Dòng Available categories vẫn hiển thị: `Công nghệ, Giáo dục, Kinh tế, Kỹ năng mềm, Quản trị, Văn học`.

**Tác động:**  
Giao diện song ngữ không nhất quán, trải nghiệm tiếng Anh chưa hoàn chỉnh.

**Minh chứng:**  
`Bug08.jpg`

**Đề xuất xử lý:**  
Bổ sung bản dịch tiếng Anh cho danh mục thể loại và cập nhật theo ngôn ngữ hiện tại.

---
