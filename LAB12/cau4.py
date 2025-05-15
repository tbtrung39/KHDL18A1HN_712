try:
    input_file = input("Nhập tên tập tin cần đọc: ")
    output_file = input("Nhập tên tập tin cần ghi: ")

    with open(input_file, "r") as file_in:
        content = file_in.read()

    with open(output_file, "w") as file_out:
        file_out.write(content)

    print(f"Đã ghi nội dung từ '{input_file}' vào '{output_file}'.")
except FileNotFoundError:
    print("Không tìm thấy tập tin cần đọc.")
except IOError:
    print("Lỗi khi mở tập tin. Kiểm tra lại chế độ mở.")
except Exception as e:
    print(f"Lỗi không xác định: {e}")
finally:
    print("Chương trình đã kết thúc.")
