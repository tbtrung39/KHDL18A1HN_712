# Danh sách menu đồ uống
menu = {
    1: "Cafe",
    2: "Cam vắt",
    3: "Nước ép cà rốt",
    4: "Nước lọc",
    5: "Nước dừa"
}

# Hiển thị menu
print("Menu đồ uống:")
for key, value in menu.items():
    print(f"{key}. {value}")

# Người dùng chọn đồ uống
choice = int(input("Nhập số tương ứng với đồ uống bạn muốn gọi: "))

# Kiểm tra lựa chọn và hiển thị kết quả
if choice in menu:
    print(f"Bạn đã chọn: {menu[choice]}")
else:
    print("Lựa chọn không hợp lệ! Vui lòng chọn lại.")
