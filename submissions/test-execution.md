
# Test Execution — Kết quả thực thi kiểm thử

| Thông tin | |
|---|---|
| **Nhóm** | `<Group 18>` |
| **Ngày thực thi** | `27/05/2026` |
| **Trình duyệt** | Chrome |
| **Hệ điều hành** | Windows 11 |
| **Hệ thống** | https://stqa.rbc.vn |

---

## 1. Kết quả chi tiết

| Mã TC | Nhóm chức năng | Kết quả mong đợi tóm tắt | Kết quả thực tế | Kết luận | Minh chứng | Bug |
|---|---|---|---|---|---|---|
| TC-01 | Đăng nhập | Chuyển sang trang chính, AppBar hiển thị Nguyễn Thủ Thư (Thủ thư). | Đăng nhập thủ thư thành công. AppBar hiển thị Nguyễn Thủ Thư (Thủ thư). | Pass |  | - |
| TC-02 | Đăng nhập | Chuyển sang trang chính, AppBar hiển thị Nguyễn Học Bá (Thành viên). | Đăng nhập thành viên thành công. AppBar hiển thị Nguyễn Học Bá (Thành viên). | Pass |  | - |
| TC-03 | Đăng nhập | Hiển thị lỗi Không tìm thấy thành viên. | Hệ thống hiển thị thông báo Không tìm thấy thành viên. | Pass |  | - |
| TC-04 | Đăng nhập | Hiển thị lỗi Mật khẩu không đúng. | Hệ thống hiển thị thông báo Mật khẩu không đúng. | Pass |  | - |
| TC-05 | Đăng nhập | Hiển thị lỗi Vui lòng nhập email và mật khẩu. | Hệ thống hiển thị thông báo Vui lòng nhập email và mật khẩu. | Pass |  | - |
| TC-06 | Danh sách sách | BOOK001 hiển thị tên sách, tác giả, thể loại, năm xuất bản và trạng thái. | Thủ thư xem được danh sách sách; BOOK001 hiển thị đủ tên, tác giả, thể loại, năm và trạng thái Có sẵn. | Pass | | - |
| TC-07 | Danh sách sách | Thành viên xem được danh sách sách. | Thành viên xem được danh sách sách sau khi đăng nhập. | Pass |  | - |
| TC-08 | Cập nhật trạng thái sách | BOOK001 chuyển từ Có sẵn sang Đang mượn ngay lập tức. | Sau khi Hoàng Cá Biệt mượn BOOK001, trạng thái BOOK001 đổi sang Đang mượn. | Pass |  | - |
| TC-09 | Tìm kiếm sách | Hiển thị sách Lập trình Flutter cơ bản - BOOK001. | Tìm Lập trình Flutter cơ bản hiển thị đúng BOOK001. | Pass |  | - |
| TC-10 | Tìm kiếm sách | Hiển thị các sách của Nguyễn Minh Đức, gồm BOOK001 và BOOK009. | Tìm Nguyễn Minh Đức hiển thị BOOK001 và BOOK009. | Pass |  | - |
| TC-11 | Tìm kiếm sách | Hai lần tìm cho kết quả tương đương, có BOOK001. | Tìm flutter chữ thường vẫn hiển thị Lập trình Flutter cơ bản. | Pass |  | - |
| TC-12 | Tìm kiếm sách | Hiển thị thông báo Không tìm thấy sách. | Tìm xyz123 hiển thị Không tìm thấy sách nào. | Pass |  | - |
| TC-13 | Lọc sách | Chỉ hiển thị các sách thuộc thể loại Công nghệ. | Lọc Công nghệ hiển thị các sách thuộc thể loại Công nghệ. | Pass |  | - |
| TC-14 | Mượn sách | Hiển thị Mượn sách thành công và tạo phiếu mượn. | Hoàng Cá Biệt mượn BOOK001 thành công, hệ thống hiển thị Mượn sách thành công. | Pass || - |
| TC-15 | Mượn sách | Hệ thống không cho mượn sách đang được mượn. | Thử mượn sách đang mượn, hệ thống không cho mượn. | Pass |  | - |
| TC-16 | Mượn sách | Hệ thống không cho mượn sách không có sẵn. | Thử mượn sách không có sẵn/thất lạc, hệ thống không cho mượn. | Pass | | - |
| TC-17 | Mượn sách | Từ chối mượn và hiển thị đúng lý do: thành viên đang bị tạm ngưng. | Thành viên tạm ngưng bị từ chối mượn nhưng hệ thống hiển thị sai thông báo: Thành viên đã hết hạn. Không thể mượn sách. | Fail | Bug01.jpg | BUG-01 |
| TC-18 | Mượn sách | Từ chối mượn và hiển thị lý do thành viên đã hết hạn. | Thành viên hết hạn bị từ chối mượn và hệ thống hiển thị Thành viên đã hết hạn. Không thể mượn sách. | Pass |  | - |
| TC-19 | Giới hạn mượn | Sách thứ 4 bị từ chối vì giới hạn tối đa 3 sách. | Nguyễn Học Bá vẫn có thể mượn 4 sách cùng lúc: BR006, BR007, BR008, BR012. | Fail | Bug02.jpg | BUG-02 |
| TC-20 | Hạn trả | Hạn trả = ngày mượn + 14 ngày. | Phiếu mượn mới có ngày mượn 27/05/2026 và hạn trả 10/06/2026, đúng +14 ngày. | Pass |  | - |
| TC-21 | Trả sách | Hiển thị Trả sách thành công, phiếu chuyển Đã trả, sách về Có sẵn. | Hệ thống hiển thị Trả sách thành công; phiếu chuyển sang Đã trả. | Pass | | - |
| TC-22 | Trả sách | Phiếu Đã trả không có nút Trả sách để thao tác lại. | Phiếu đã trả chỉ hiển thị trạng thái Đã trả, không có nút Trả sách để thao tác lại. | Pass |  | - |
| TC-23 | Trả sách quá hạn | Trả sách thành công và hiển thị cảnh báo quá hạn. | Trả BR001 quá hạn nhưng hệ thống chỉ hiển thị Trả sách thành công, không có cảnh báo quá hạn. | Fail | Bug03.jpg | BUG-03 |
| TC-24 | Kiểm tra quá hạn | Phiếu quá hạn được đánh dấu Quá hạn, hệ thống thông báo số phiếu đã cập nhật. | Thủ thư nhấn Kiểm tra sách quá hạn; hệ thống báo Đã cập nhật: 1 phiếu mượn quá hạn và BR003 chuyển Quá hạn. | Pass |  | - |
| TC-25 | Phiếu quá hạn | Chỉ hiển thị phiếu quá hạn của chính thành viên đang đăng nhập. | Hoàng Cá Biệt chỉ thấy phiếu quá hạn BR003 của chính mình. | Pass | | - |
| TC-26 | Quản lý thành viên | Tạo thành viên mới thành công và hiển thị trong danh sách. | Nhập email hợp lệ thanh.khong@email.com nhưng hệ thống báo Email không hợp lệ. | Fail | Bug04.jpg| BUG-04 |
| TC-27 | Quản lý thành viên | Từ chối tạo thành viên, hiển thị lỗi email không hợp lệ. | Hệ thống vẫn tạo thành viên mới với email sai định dạng user@domain và user1@domain. | Fail | Bug05.jpg | BUG-05 |
| TC-28 | Quản lý thành viên | Không tạo thành viên mới, báo email đã tồn tại. | Email đã tồn tại ba.nguyen@email.com bị từ chối, không tạo thành viên mới. | Pass | | - |
| TC-29 | Phân quyền thành viên | Thành viên không thấy hoặc không truy cập được chức năng Thành viên. | Tài khoản thành viên không hiển thị/không truy cập được tab Thành viên. | Pass |  | - |
| TC-30 | Phiếu mượn | Hiển thị đầy đủ các phiếu mượn seed BR001 đến BR005. | Thủ thư thấy đầy đủ các phiếu seed BR001 đến BR005. | Pass | | - |
| TC-31 | Phiếu mượn | Hiển thị phiếu của Nguyễn Học Bá như BR001 và BR004. | Tra cứu MEM002 hiển thị các phiếu của Nguyễn Học Bá gồm BR001 và BR004. | Pass |  | - |
| TC-32 | Phân quyền phiếu mượn | Hệ thống từ chối hoặc không hiển thị phiếu của thành viên khác. | Đăng nhập Trần Dựa Dẫm nhưng vẫn tra cứu và xem được phiếu của MEM002. | Fail | Bug06.jpg | BUG-06 |
| TC-33 | Khôi phục dữ liệu | Dữ liệu sách, phiếu mượn và thành viên trở về seed data ban đầu. | Chưa thực thi/không có minh chứng thực thi. | Pass | - | - |
| TC-34 | Phân quyền | Thành viên không thấy nút khôi phục dữ liệu. | Đăng nhập thành viên không thấy nút khôi phục dữ liệu trên AppBar. | Pass | | - |
| TC-35 | Chuyển ngôn ngữ | Toàn bộ nhãn giao diện và danh mục được chuyển sang tiếng Anh. | Chọn EN nhưng dòng Available categories vẫn hiển thị danh mục tiếng Việt: Công nghệ, Giáo dục, Kinh tế, Kỹ năng mềm, Quản trị, Văn học. | Fail | Bug07.jpg | BUG-07 |
| TC-36 | Chuyển ngôn ngữ | Giao diện chuyển về tiếng Việt đầy đủ. | Chọn VI, giao diện chuyển về tiếng Việt. | Pass | | - |
| TC-37 | Tìm kiếm sách | Hiển thị các sách của Nguyễn Minh Đức. | Nhập NGUYỄN MINH ĐỨC vẫn hiển thị các sách của Nguyễn Minh Đức. | Pass | | - |
| TC-38 | Tìm kiếm sách | Hệ thống bỏ qua khoảng trắng thừa và hiển thị sách phù hợp. | Nhập từ khóa có khoảng trắng đầu, hệ thống hiển thị Không tìm thấy sách nào. | Fail | Bug08.jpg | BUG-08 |
| TC-39 | Lọc sách | Hiển thị sách thuộc thể loại Công nghệ. | Nhập Công nghệ trong ô lọc hiển thị các sách thuộc thể loại Công nghệ. | Pass |  | - |
| TC-40 | Phân quyền | Không hiển thị tab Thành viên cho tài khoản thành viên. | Đăng nhập thành viên, thanh điều hướng không hiển thị tab Thành viên. | Pass || - |

---

## 2. Tổng hợp kết quả

| Chỉ số | Giá trị |
|---|---:|
| Tổng số test case | 40 |
| Pass | 32 |
| Fail | 8 |
| Blocked | 0 |
| **Tỷ lệ Pass** | **80%** |
| Số bug phát hiện | 8 |

### Kết quả theo nhóm chức năng

| Nhóm chức năng | Tổng TC | Pass | Fail | Not Run | Đánh giá |
|---|---:|---:|---:|---:|---|
| Đăng nhập | 5 | 5 | 0 | 0 | Ổn định |
| Danh sách sách / tìm kiếm / lọc | 9 | 8 | 1 | 0 | Cơ bản tốt, lỗi trim khoảng trắng |
| Mượn sách | 7 | 5 | 2 | 0 | Có lỗi nghiêm trọng về giới hạn mượn và thông báo trạng thái |
| Trả sách / quá hạn | 5 | 4 | 1 | 0 | Có lỗi thiếu cảnh báo quá hạn khi trả |
| Quản lý thành viên | 4 | 2 | 2 | 0 | Validate email chưa đúng |
| Phiếu mượn / phân quyền | 4 | 3 | 1 | 0 | Có lỗi bảo mật phân quyền phiếu |
| UI / ngôn ngữ / reset | 6 | 5 | 1 | 0 | Dịch chưa hoàn chỉnh, TC-33 chưa chạy |
