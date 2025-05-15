try:
    file_name = input("Nhập tên tập tin: ")
    with open(file_name, "r") as file:
        content = file.read()
    
    with open("copy.dat", "w") as copy_file:
        copy_file.write(content)
    print("Đã sao chép nội dung vào file 'copy.dat'.")
except FileNotFoundError:
    print("Không tìm thấy tập tin với tên đã nhập.")
except Exception as e:
    print(f"Lỗi không xác định: {e}")
