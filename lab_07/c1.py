A = set()

print("Nhập các số thực vào tập hợp A (gõ 'ESC' để kết thúc):")

while True:
    entry = input("Nhập số thực: ")
    if entry.upper() == "ESC":
        break
    try:
        number = float(entry)
        A.add(number)
    except ValueError:
        print("Lỗi: vui lòng nhập số thực hợp lệ hoặc 'ESC' để thoát.")

print("\nTập hợp A gồm các số thực đã nhập:")
print(A)
