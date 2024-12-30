# Game Kéo Búa Bao

## Mô tả tác phẩm

Ứng dụng "Game Kéo Búa Bao" là một chương trình Python được xây dựng bằng Tkinter, mang đến trò chơi đơn giản nhưng đầy thú vị. Trò chơi giữa người dùng và máy tính được thiết kế nhằm mục đích giải trí nhẹ nhàng.

---

## Chức năng
- Cho phép người dùng lựa chọn giữa ba phương án: **Kéo**, **Búa**, **Bao**.
- Random lựa chọn của máy tính.
- Hiển thị kết quả trận đấu bằng hộp thoại (messagebox).

---

## Hướng dẫn cài đặt và chạy

### Yêu cầu
- Python 3.x
- Thư viện Tkinter (tích hợp sẵn trong Python)

### Cài đặt
1. Tải file code Python về máy.
2. Mở terminal hoặc command prompt.
3. Chuyển đến thư mục chứa file Python.

```bash
cd /duong_dan_den_thu_muc
```

4. Chạy file Python:

```bash
python ten_file.py
```

---

## Cách chơi
1. Sau khi chạy chương trình, một giao diện hiển thị trò chơi sẽ xuất hiện.
2. Bấm vào một trong ba nút:
   - **Kéo**
   - **Búa**
   - **Bao**
3. Kết quả trận đấu sẽ được hiển thị trong hộp thoại.

---

## Mô tả chi tiết code

### 1. **Thư viện**
- `tkinter`: Xây dựng giao diện.
- `messagebox`: Hiển thị kết quả trận đấu.
- `random`: Lựa chọn ngẫu nhiên cho máy tính.

### 2. **Hàm xử lý kết quả**
Hàm `play_game(user_choice)` nhận lựa chọn từ người dùng, tạo lựa chọn ngẫu nhiên cho máy tính và so sánh theo quy tắc:
- Kéo thắng Bao
- Bao thắng Búa
- Búa thắng Kéo
- Hòa khi cả hai cùng lựa chọn.

Kết quả sẽ được hiển thị qua `messagebox`.

### 3. **Giao diện**
- Cửa sổ được thiết kế bằng `Tk` với cấu trúc đơn giản.
- Sử dụng `Button` để tạo các lựa chọn.
- Thêm phong cách (đổ nút, màu sắc) nhằm tăng trải nghiệm người dùng.

---

## Tùy chỉnh
Người dùng có thể tùy chỉnh giao diện hoặc quy tắc trò chơi bằng cách thay đổi code trong các phần liên quan:
- **Thay đổi giao diện**: Chỉnh sửa các thuộc tính trong `button_style` hoặc giao diện Tkinter.
- **Thay đổi quy tắc**: Sửa quy tắc so sánh trong hàm `play_game`.

