filename = input("Nhập tên tập tin cần đọc: ")

try:
    with open(filename, 'r', encoding='utf-8') as f:
        print("Nội dung tập tin:")
        print(f.read())
except FileNotFoundError:
    print("Tập tin không tồn tại.")
