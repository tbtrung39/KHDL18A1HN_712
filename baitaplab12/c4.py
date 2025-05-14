try:
    file_read = input("Nhập tên tập tin cần đọc: ")
    file_write = input("Nhập tên tập tin cần ghi: ")

    with open(file_read, 'r', encoding='utf-8') as f:
        content = f.read()

    with open(file_write, 'w', encoding='utf-8') as fw:
        fw.write(content)

    print("Sao chép nội dung thành công.")
except FileNotFoundError:
    print("Không tìm thấy tập tin cần đọc.")
except IOError:
    print("Lỗi khi ghi tập tin.")
finally:
    print("Kết thúc chương trình.")
