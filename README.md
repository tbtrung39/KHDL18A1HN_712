# **CHÚ Ý ĐỌC VÀ LÀM CHÍNH XÁC THEO HƯỚNG DẪN**

## I. Thực hiện clone repository

- Chọn 1 folder rỗng chuột phải chọn gitbash để clone git repository về máy với dòng lệnh bên dưới

```
git clone https://github.com/tbtrung39/KHDL18A1HN_712.git
```

**LƯU Ý:** Nếu chưa sử dụng Gitbash trên máy bao giờ, Gitbash lúc này sẽ yêu cầu đăng nhập vào tài khoản git. Bắt buộc phải sử dụng tài khoản git gắn với gmail sinh viên được nhà trường cấp

## II. Thực hiện tạo nhánh chính cá nhân

B1: Sau khi clone repository về máy thành công tiến hành tạo **NHÁNH CHÍNH** theo **ĐÚNG** format: `<ROOT_STT_họ và tên>`. Format phải **CHÍNH XÁC** giống như sau: `ROOT_11_Ngo_Quang_Dai`, STT là số thứ tự được gắn kèm với danh sách lớp. Sử dụng lệnh sau để tạo nhánh chính:

```
git checkout -b <tên nhánh chính vừa tạo>
```

**LƯU Ý:** Nhánh chính làm không chính xác sẽ bị xóa, nếu mất bài sinh viên tự chịu trách nhiệm

B2: Sau khi tạo nhánh chính, sinh viên tạo thêm file **<ho_va_ten.txt>** (Ví dụ: Ngo_Quang_Dai.txt) vào thư mục để bắt đầu thực hiện commit đầu tiên
B3: Sau khi thêm file txt bắt đầu thực hiện commit đầu tiên cho **NHÁNH CHÍNH**. Sử dụng lệnh sau:

```
git add .
git commit -m "first commit"
```

B4: cập nhập nhánh của mình lên givthub bằng cách Push **NHÁNH CHÍNH** lên remote repository với câu lệnh push origin kèm theo tên nhánh muốn push:

```
git push origin <tên nhánh chính vừa tạo>
```

## III. Thực hiện làm các bài tập theo từng lab

- Bài tập thực hiện theo từng lab, mỗi lab sẽ nằm ở một nhánh riêng bắt nguồn từ nhánh chính đã tạo ở trên
B1: Trước khi bắt đầu làm bài, checkout về nhánh chính cá nhân của mình. Sử dụng câu lệnh:
```
git checkout <tên nhánh chính>
```
B2: Tạo nhánh mới theo lab mà mình đang làm từ nhánh chính theo **ĐÚNG** format: `<STT_họ và tên/lab đang thực hiện>`. Format phải **CHÍNH XÁC** giống như sau: `11_Ngo_Quang_Dai_/lab_01`. Sử dụng lệnh sau để tạo nhánh:

```
git checkout -b <STT_họ và tên/lab đang thực hiện>
```

B3: Sau khi tạo nhánh mới, tạo một folder chứa tên lab mình đang thực hiện ở nhánh này (ví dụ: lab_01) và làm các bài tập được giao vào trong folder đó,
B4: Sau khi hoàn thành bài tập, thực hiện `add` thay đổi, `commit` rồi push lên đúng nhánh đang thực hiện. Sử dụng lệnh sau:

```
git add .
git commit -m "ghi những gì mình đã thực hiện"
git push origin <STT_họ và tên/lab đang thực hiện>
```

**LƯU Ý:** Kiểm tra kĩ nhánh hiện tại xem mình có đúng đang ở nhánh làm bài tập của mình không trước khi thực hiện. Nếu push trực tiếp vào nhánh **MAIN**, **NHÁNH CHÍNH CÁ NHÂN** hoặc **NHÁNH CỦA SINH VIÊN KHÁC**, vi phạm sinh viên sẽ bị trừ điểm quá trình.
**LƯU Ý:** Mỗi lab yêu cầu sinh viên làm một nhánh riêng và push commit mỗi bài lab chính xác vào nhánh đó.
**LƯU Ý:** Checkout về **NHÁNH CHÍNH** rồi mới tạo nhánh làm bài tập mới

## IV. Lưu ý trong quá trình thực hành
- **KHÔNG PUSH LÊN NHÁNH MAIN**
- **KHÔNG PUSH TRỰC TIẾP LÊN NHÁNH CHÍNH CỦA BẢN THÂN**
- **ĐẶT TÊN NHÁNH THEO ĐÚNG FORMAT**
- **HOÀN THÀNH BÀI TẬP ĐÚNG HẠN**

- Có bất kì vấn đề gì liên quan đến bài tập hoặc git có thể nhắn tin hỏi lại thầy trên nhóm lớp hoặc đặt câu hỏi ở phần **ISSUES**.
- Học thêm về git:
  - https://git-scm.com/book/en/v2
  - https://learngitbranching.js.org/?locale=vi
