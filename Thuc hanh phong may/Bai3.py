def doc_va_ghi_file():
    ten_file = input("Nhập tên file cần đọc: ")

    try:
        with open(ten_file, 'r', encoding='utf-8') as f:
            noi_dung = f.read()
    except FileNotFoundError:
        print("Lỗi: Không tìm thấy file.")
        return

    with open('copy.dat', 'w', encoding='utf-8') as f_copy:
        f_copy.write(noi_dung)

    print(f"Đã sao chép nội dung từ '{ten_file}' vào 'copy.dat' thành công.")

if __name__ == "__main__":
    doc_va_ghi_file()
