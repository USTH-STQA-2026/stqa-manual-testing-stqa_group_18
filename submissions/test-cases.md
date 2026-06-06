
# Test Cases — Bảng trường hợp kiểm thử

| Thông tin | |
|---|---|
| **Nhóm** | `<!Group 18>` |
| **Ngày tạo** | `27/05/2026` |
| **Hệ thống** | https://stqa.rbc.vn |
| **Tham chiếu** | SRS v1.0 |

---

## 1. Input Domain Modeling — IDM

### IDM — REQ-01 Đăng nhập

| Đặc tính | Phân vùng | Giá trị đại diện | Kết quả mong đợi |
|---|---|---|---|
| Email tồn tại? | Có | `librarian@library.com`, `ba.nguyen@email.com` | Đăng nhập thành công nếu mật khẩu đúng |
| Email tồn tại? | Không | `nobody@test.com` | Báo lỗi `Không tìm thấy thành viên` |
| Mật khẩu đúng? | Đúng | `admin123`, `password123` | Đăng nhập thành công |
| Mật khẩu đúng? | Sai | `wrongpassword` | Báo lỗi `Mật khẩu không đúng` |
| Trường rỗng? | Email + mật khẩu rỗng | `"" / ""` | Báo lỗi `Vui lòng nhập email và mật khẩu` |

### IDM — REQ-03 Tìm kiếm và lọc sách

| Đặc tính | Phân vùng | Giá trị đại diện | Kết quả mong đợi |
|---|---|---|---|
| Từ khóa tồn tại theo tên sách | Có | `Flutter` | Hiển thị sách khớp tên |
| Từ khóa tồn tại theo tác giả | Có | `Nguyễn Minh Đức` | Hiển thị sách của tác giả |
| Từ khóa không tồn tại | Không | `xyz123` | Hiển thị không tìm thấy sách |
| Chữ hoa/thường | Hoa/thường khác nhau | `Flutter`, `flutter`, `NGUYỄN MINH ĐỨC` | Kết quả vẫn đúng vì tìm kiếm không phân biệt hoa/thường |
| Khoảng trắng | Có khoảng trắng đầu/cuối | ` NGUYỄN MINH ĐỨC` | Hệ thống nên xử lý ổn định |
| Thể loại | Có trong seed data | `Công nghệ` | Chỉ hiển thị sách thuộc thể loại Công nghệ |

### IDM — REQ-04/REQ-05 Mượn và trả sách

| Đặc tính | Phân vùng | Giá trị đại diện | Kết quả mong đợi |
|---|---|---|---|
| Trạng thái sách | Có sẵn | `BOOK001` | Cho phép mượn nếu thành viên hợp lệ |
| Trạng thái sách | Đang mượn | `BOOK003` | Từ chối mượn |
| Trạng thái sách | Không có sẵn/thất lạc | `BOOK007` | Từ chối mượn |
| Trạng thái thành viên | Hoạt động | `MEM006` | Cho phép mượn |
| Trạng thái thành viên | Tạm ngưng | `MEM004` | Từ chối, báo đúng lý do tạm ngưng |
| Trạng thái thành viên | Hết hạn | `MEM005` | Từ chối, báo đúng lý do hết hạn |
| Số sách đang mượn | < 3 | 0, 1, 2 sách | Cho phép mượn |
| Số sách đang mượn | = 3 hoặc > 3 | 3, 4 sách | Từ chối mượn thêm |
| Trả sách | Phiếu đang mượn | `BR003` | Cho trả sách |
| Trả sách | Phiếu đã trả | `BR002` | Không cho trả lại |
| Trả sách quá hạn | returnDate > dueDate | `BR001` | Có cảnh báo quá hạn |

### IDM — REQ-06: Xử lý sách quá hạn

| Đặc tính | Phân vùng | Giá trị đại diện | Kết quả mong đợi |
|---|---|---|---|
| Vai trò người dùng | Thủ thư | `librarian@library.com` | Được quyền nhấn **Kiểm tra sách quá hạn** |
| Vai trò người dùng | Thành viên | `ba.nguyen@email.com` | Không có quyền kiểm tra quá hạn toàn hệ thống |
| Trạng thái phiếu mượn | Phiếu chưa quá hạn | Hạn trả lớn hơn ngày hiện tại | Không bị đánh dấu **Quá hạn** |
| Trạng thái phiếu mượn | Phiếu quá hạn | `BR003` có hạn trả trước ngày hiện tại | Bị đánh dấu **Quá hạn** |
| Kết quả cập nhật | Có phiếu quá hạn | `BR003` | Hiển thị số phiếu quá hạn đã cập nhật |

### IDM — REQ-07: Quản lý thành viên

| Đặc tính | Phân vùng | Giá trị đại diện | Kết quả mong đợi |
|---|---|---|---|
| Vai trò người dùng | Thủ thư | `librarian@library.com` | Được truy cập tab **Thành viên** |
| Vai trò người dùng | Thành viên | `ba.nguyen@email.com` | Không được truy cập chức năng quản lý thành viên |
| Email thêm mới | Email hợp lệ | `thanh.khong@email.com` | Tạo thành viên mới thành công |
| Email thêm mới | Email sai định dạng | `user@domain` | Bị từ chối, báo email không hợp lệ |
| Email thêm mới | Email đã tồn tại | `ba.nguyen@email.com` | Bị từ chối vì email đã tồn tại |
| Thông tin thành viên | Dữ liệu hợp lệ | Họ tên + email + số điện thoại hợp lệ | Thành viên mới xuất hiện trong danh sách |
| Thông tin thành viên | Dữ liệu không hợp lệ | Số điện thoại sai định dạng | Bị từ chối nếu hệ thống validate số điện thoại |

### IDM — REQ-08: Tra cứu phiếu mượn / Phân quyền

| Đặc tính | Phân vùng | Giá trị đại diện | Kết quả mong đợi |
|---|---|---|---|
| Vai trò người dùng | Thủ thư | `librarian@library.com` | Xem được toàn bộ phiếu mượn |
| Vai trò người dùng | Thành viên | `ba.nguyen@email.com` | Chỉ xem được phiếu của chính mình |
| Tra cứu phiếu | Tra cứu chính mình | `MEM002` khi login `MEM002` | Hiển thị phiếu của Nguyễn Học Bá |
| Tra cứu phiếu | Tra cứu thành viên khác | `MEM002` khi login `MEM003` | Bị từ chối hoặc không hiển thị dữ liệu |
| Dữ liệu phiếu mượn | Phiếu thuộc chính người dùng | `BR001`, `BR004` của `MEM002` | Được hiển thị |
| Dữ liệu phiếu mượn | Phiếu thuộc người khác | Phiếu của `MEM003` khi login `MEM002` | Không được hiển thị |
| Phân quyền dữ liệu | Thủ thư tra cứu bất kỳ mã thành viên | `MEM002`, `MEM003` | Hiển thị đúng phiếu theo mã thành viên |
## 2. Decision Table — Chức năng mượn sách

| Rule | Thành viên hoạt động? | Sách có sẵn? | Số sách đang mượn < 3? | Kết quả |
|---|---|---|---|---|
| R1 | Có | Có | Có | Cho mượn |
| R2 | Có | Không | Có | Từ chối vì sách không có sẵn |
| R3 | Có | Có | Không | Từ chối vì vượt giới hạn 3 sách |
| R4 | Tạm ngưng | Có | Có | Từ chối vì thành viên tạm ngưng |
| R5 | Hết hạn | Có | Có | Từ chối vì thành viên hết hạn |

---

## 3. Danh sách Test Case

| Mã TC | Nhóm chức năng | Mục tiêu kiểm thử | Tiền điều kiện | Bước thực hiện | Dữ liệu đầu vào | Kết quả mong đợi | REQ | Kỹ thuật |
|---|---|---|---|---|---|---|---|---|
| TC-01 | Đăng nhập | Đăng nhập thành công bằng tài khoản Thủ thư | Trang đăng nhập đã mở, dữ liệu đã reset | 1. Nhập email. 2. Nhập mật khẩu. 3. Nhấn Đăng nhập. | librarian@library.com / admin123 | Chuyển sang trang chính, AppBar hiển thị Nguyễn Thủ Thư (Thủ thư). | REQ-01 | EP |
| TC-02 | Đăng nhập | Đăng nhập thành công bằng tài khoản Thành viên | Trang đăng nhập đã mở, dữ liệu đã reset | 1. Nhập email. 2. Nhập mật khẩu. 3. Nhấn Đăng nhập. | ba.nguyen@email.com / password123 | Chuyển sang trang chính, AppBar hiển thị Nguyễn Học Bá (Thành viên). | REQ-01 | EP |
| TC-03 | Đăng nhập | Đăng nhập thất bại với email không tồn tại | Trang đăng nhập đã mở | 1. Nhập email không tồn tại. 2. Nhập mật khẩu. 3. Nhấn Đăng nhập. | nobody@test.com / anything | Hiển thị lỗi Không tìm thấy thành viên. | REQ-01 | EP, Negative |
| TC-04 | Đăng nhập | Đăng nhập thất bại với mật khẩu sai | Trang đăng nhập đã mở | 1. Nhập email tồn tại. 2. Nhập mật khẩu sai. 3. Nhấn Đăng nhập. | ba.nguyen@email.com / wrongpassword | Hiển thị lỗi Mật khẩu không đúng. | REQ-01 | EP, Negative |
| TC-05 | Đăng nhập | Đăng nhập thất bại khi bỏ trống email và mật khẩu | Trang đăng nhập đã mở | 1. Để trống email. 2. Để trống mật khẩu. 3. Nhấn Đăng nhập. | Email trống, mật khẩu trống | Hiển thị lỗi Vui lòng nhập email và mật khẩu. | REQ-01 | EP, Negative |
| TC-06 | Danh sách sách | Thủ thư xem danh sách sách và thông tin sách | Đã đăng nhập thủ thư | 1. Vào tab Sách. 2. Quan sát BOOK001. | BOOK001 | BOOK001 hiển thị tên sách, tác giả, thể loại, năm xuất bản và trạng thái. | REQ-02 | EP |
| TC-07 | Danh sách sách | Thành viên xem được danh sách sách | Đã đăng nhập thành viên | 1. Vào tab Sách. 2. Quan sát danh sách. | ba.nguyen@email.com | Thành viên xem được danh sách sách. | REQ-02 | Access Control |
| TC-08 | Cập nhật trạng thái sách | Trạng thái sách cập nhật sau khi mượn | Đăng nhập thành viên hoạt động, sách có sẵn | 1. Mượn BOOK001. 2. Quan sát trạng thái BOOK001. | biet.hoang@email.com, BOOK001 | BOOK001 chuyển từ Có sẵn sang Đang mượn ngay lập tức. | REQ-02, REQ-04 | State-based |
| TC-09 | Tìm kiếm sách | Tìm theo tên sách | Đã đăng nhập thành viên | 1. Nhập từ khóa vào ô tìm kiếm. 2. Quan sát kết quả. | Lập trình Flutter cơ bản | Hiển thị sách Lập trình Flutter cơ bản - BOOK001. | REQ-03 | EP |
| TC-10 | Tìm kiếm sách | Tìm theo tác giả | Đã đăng nhập thành viên | 1. Nhập tên tác giả. 2. Quan sát kết quả. | Nguyễn Minh Đức | Hiển thị các sách của Nguyễn Minh Đức, gồm BOOK001 và BOOK009. | REQ-03 | EP |
| TC-11 | Tìm kiếm sách | Tìm kiếm không phân biệt hoa/thường | Đã đăng nhập thành viên | 1. Tìm Flutter. 2. Tìm flutter. 3. So sánh kết quả. | Flutter, flutter | Hai lần tìm cho kết quả tương đương, có BOOK001. | REQ-03 | EP |
| TC-12 | Tìm kiếm sách | Tìm từ khóa không tồn tại | Đã đăng nhập thành viên | 1. Nhập từ khóa không tồn tại. 2. Quan sát kết quả. | xyz123 | Hiển thị thông báo Không tìm thấy sách. | REQ-03 | EP, Negative |
| TC-13 | Lọc sách | Lọc thể loại Công nghệ | Đã đăng nhập thành viên | 1. Nhập Công nghệ vào ô lọc thể loại. 2. Quan sát kết quả. | Công nghệ | Chỉ hiển thị các sách thuộc thể loại Công nghệ. | REQ-03 | EP |
| TC-14 | Mượn sách | Mượn sách thành công với thành viên hoạt động | Đăng nhập Hoàng Cá Biệt, sách có sẵn | 1. Chọn BOOK001. 2. Nhấn nút mượn. | biet.hoang@email.com, BOOK001 | Hiển thị Mượn sách thành công và tạo phiếu mượn. | REQ-04 | Decision Table |
| TC-15 | Mượn sách | Từ chối mượn sách đang được mượn | Đăng nhập thành viên hoạt động | 1. Thử mượn sách có trạng thái Đang mượn. | BOOK003 | Hệ thống không cho mượn sách đang được mượn. | REQ-04 | Decision Table, Negative |
| TC-16 | Mượn sách | Từ chối mượn sách không có sẵn/thất lạc | Đăng nhập thành viên hoạt động | 1. Thử mượn sách không có sẵn hoặc thất lạc. | BOOK007 | Hệ thống không cho mượn sách không có sẵn. | REQ-04 | Decision Table, Negative |
| TC-17 | Mượn sách | Thành viên tạm ngưng không được mượn sách | Đăng nhập thành viên tạm ngưng | 1. Đăng nhập cu.le@email.com. 2. Thử mượn sách có sẵn. | cu.le@email.com / password123, BOOK001 | Từ chối mượn và hiển thị đúng lý do: thành viên đang bị tạm ngưng. | REQ-04 | Decision Table, Negative |
| TC-18 | Mượn sách | Thành viên hết hạn không được mượn sách | Đăng nhập thành viên hết hạn | 1. Đăng nhập binh.pham@email.com. 2. Thử mượn sách có sẵn. | binh.pham@email.com / password123, BOOK001 | Từ chối mượn và hiển thị lý do thành viên đã hết hạn. | REQ-04 | Decision Table, Negative |
| TC-19 | Giới hạn mượn | Không cho mượn vượt quá 3 sách | Đăng nhập thành viên hoạt động | 1. Mượn liên tiếp sách có sẵn. 2. Khi đã đủ 3 sách, thử mượn sách thứ 4. | ba.nguyen@email.com, nhiều sách có sẵn | Sách thứ 4 bị từ chối vì giới hạn tối đa 3 sách. | REQ-04 | BVA |
| TC-20 | Hạn trả | Hạn trả bằng ngày mượn + 14 ngày | Đăng nhập thành viên hoạt động | 1. Mượn sách. 2. Vào tab Mượn / Trả. 3. Kiểm tra hạn trả. | BOOK002 hoặc sách có sẵn | Hạn trả = ngày mượn + 14 ngày. | REQ-04 | BVA |
| TC-21 | Trả sách | Trả sách đang mượn thành công | Thành viên có phiếu đang mượn | 1. Vào Mượn / Trả. 2. Nhấn Trả sách trên phiếu đang mượn. | Phiếu đang mượn | Hiển thị Trả sách thành công, phiếu chuyển Đã trả, sách về Có sẵn. | REQ-05 | EP |
| TC-22 | Trả sách | Không cho trả lại phiếu đã trả | Thành viên có phiếu đã trả | 1. Vào Mượn / Trả. 2. Quan sát phiếu Đã trả. | BR002 | Phiếu Đã trả không có nút Trả sách để thao tác lại. | REQ-05 | Negative |
| TC-23 | Trả sách quá hạn | Trả sách quá hạn phải có cảnh báo | Đăng nhập Nguyễn Học Bá, có phiếu quá hạn | 1. Vào Mượn / Trả. 2. Trả phiếu BR001 quá hạn. | BR001 | Trả sách thành công và hiển thị cảnh báo quá hạn. | REQ-05 | EP, Negative |
| TC-24 | Kiểm tra quá hạn | Thủ thư kiểm tra và đánh dấu phiếu quá hạn | Đăng nhập thủ thư | 1. Vào Mượn / Trả. 2. Nhấn Kiểm tra sách quá hạn. | librarian@library.com | Phiếu quá hạn được đánh dấu Quá hạn, hệ thống thông báo số phiếu đã cập nhật. | REQ-06 | State-based |
| TC-25 | Phiếu quá hạn | Thành viên chỉ thấy phiếu quá hạn của mình | Thủ thư đã kiểm tra quá hạn | 1. Đăng nhập thành viên có phiếu quá hạn. 2. Vào Mượn / Trả. | biet.hoang@email.com | Chỉ hiển thị phiếu quá hạn của chính thành viên đang đăng nhập. | REQ-06, REQ-08 | Access Control |
| TC-26 | Quản lý thành viên | Thủ thư thêm thành viên với email hợp lệ | Đăng nhập thủ thư | 1. Vào Thành viên. 2. Nhấn thêm. 3. Nhập thông tin hợp lệ. 4. Nhấn Thêm thành viên. | Thành thông minh, thanh.khong@email.com, 0972316494 | Tạo thành viên mới thành công và hiển thị trong danh sách. | REQ-07 | EP |
| TC-27 | Quản lý thành viên | Từ chối email sai định dạng | Đăng nhập thủ thư | 1. Vào thêm thành viên. 2. Nhập email user@domain. 3. Nhấn thêm. | user@domain | Từ chối tạo thành viên, hiển thị lỗi email không hợp lệ. | REQ-07 | EP, Negative |
| TC-28 | Quản lý thành viên | Từ chối email đã tồn tại | Đăng nhập thủ thư | 1. Vào thêm thành viên. 2. Nhập email đã tồn tại. 3. Nhấn thêm. | ba.nguyen@email.com | Không tạo thành viên mới, báo email đã tồn tại. | REQ-07 | EP, Negative |
| TC-29 | Phân quyền thành viên | Thành viên thường không truy cập quản lý thành viên | Đăng nhập thành viên | 1. Quan sát thanh điều hướng. 2. Thử truy cập quản lý thành viên nếu có. | ba.nguyen@email.com | Thành viên không thấy hoặc không truy cập được chức năng Thành viên. | REQ-07, REQ-08 | Access Control |
| TC-30 | Phiếu mượn | Thủ thư xem tất cả phiếu seed | Đăng nhập thủ thư | 1. Vào Mượn / Trả. 2. Tab Tất cả phiếu mượn. | BR001-BR005 | Hiển thị đầy đủ các phiếu mượn seed BR001 đến BR005. | REQ-08 | Access Control |
| TC-31 | Phiếu mượn | Thành viên MEM002 xem phiếu của mình | Đăng nhập thành viên | 1. Vào Tra cứu phiếu mượn. 2. Nhập MEM002. | MEM002 | Hiển thị phiếu của Nguyễn Học Bá như BR001 và BR004. | REQ-08 | Access Control |
| TC-32 | Phân quyền phiếu mượn | Thành viên không được xem phiếu của người khác | Đăng nhập Trần Dựa Dẫm | 1. Vào Tra cứu phiếu mượn. 2. Nhập MEM002. | dam.tran@email.com, MEM002 | Hệ thống từ chối hoặc không hiển thị phiếu của thành viên khác. | REQ-08 | Access Control, Negative |
| TC-33 | Khôi phục dữ liệu | Thủ thư khôi phục dữ liệu về seed data | Đăng nhập thủ thư, dữ liệu đã thay đổi | 1. Thay đổi dữ liệu. 2. Nhấn Khôi phục dữ liệu. 3. Xác nhận. | Nút khôi phục dữ liệu | Dữ liệu sách, phiếu mượn và thành viên trở về seed data ban đầu. | General | State-based |
| TC-34 | Phân quyền | Thành viên không có quyền khôi phục dữ liệu | Đăng nhập thành viên | 1. Quan sát AppBar. 2. Kiểm tra nút khôi phục dữ liệu. | ba.nguyen@email.com | Thành viên không thấy nút khôi phục dữ liệu. | REQ-08 | Access Control |
| TC-35 | Chuyển ngôn ngữ | Chuyển giao diện sang tiếng Anh đầy đủ | Đã đăng nhập | 1. Nhấn EN. 2. Quan sát nhãn giao diện. | Nút EN | Toàn bộ nhãn giao diện và danh mục được chuyển sang tiếng Anh. | General UI | UI |
| TC-36 | Chuyển ngôn ngữ | Chuyển giao diện về tiếng Việt | Giao diện đang ở EN | 1. Nhấn VI. 2. Quan sát nhãn giao diện. | Nút VI | Giao diện chuyển về tiếng Việt đầy đủ. | General UI | UI |
| TC-37 | Tìm kiếm sách | Tìm tác giả viết hoa toàn bộ | Đăng nhập thành viên | 1. Nhập NGUYỄN MINH ĐỨC. 2. Quan sát kết quả. | NGUYỄN MINH ĐỨC | Hiển thị các sách của Nguyễn Minh Đức. | REQ-03 | EP |
| TC-38 | Tìm kiếm sách | Tìm kiếm xử lý khoảng trắng đầu/cuối | Đăng nhập thành viên | 1. Nhập từ khóa có khoảng trắng đầu/cuối. 2. Quan sát kết quả. |  NGUYỄN MINH ĐỨC | Hệ thống bỏ qua khoảng trắng thừa và hiển thị sách phù hợp. | REQ-03 | Robustness, Negative |
| TC-39 | Lọc sách | Lọc thể loại Công nghệ | Đăng nhập thành viên | 1. Nhập Công nghệ vào ô lọc. 2. Quan sát kết quả. | Công nghệ | Hiển thị sách thuộc thể loại Công nghệ. | REQ-03 | EP |
| TC-40 | Phân quyền | Thành viên không thấy tab Thành viên | Đăng nhập thành viên | 1. Quan sát thanh điều hướng dưới cùng. | ba.nguyen@email.com | Không hiển thị tab Thành viên cho tài khoản thành viên. | REQ-07, REQ-08 | Access Control |

---

## 4. Tổng hợp Test Case

| Feature Group | # TCs | REQ Coverage | IDM Techniques Applied |
|---|---|---|---|
| Login | 5 | REQ-01 | EP |
| View Book List | 3 | REQ-02 | EP |
| Search & Filter Books | 8 | REQ-03 | EP |
| Borrow Book | 7 | REQ-04 | EP, BVA, Decision Table |
| Return Book | 3 | REQ-05 | EP, Negative |
| Overdue Handling | 2 | REQ-06 | State-based, Access Control |
| Member Management | 3 | REQ-07 | EP |
| Borrow Record Lookup | 6 | REQ-08 | Access Control |
| **Total** | **40** | **REQ-01 → REQ-08** | **EP, BVA, Decision Table, Access Control, State-based, Negative** |