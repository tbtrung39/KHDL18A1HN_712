print("Menu đồ uống:")
print("1. Cafe")
print("2. Cam vắt")
print("3. Nước ép cà rốt")
print("4. Nước lọc")
print("5. Nước dừa")

chon = int(input("Nhập số tương ứng với đồ uống bạn muốn gọi: "))

while chon < 1 or chon > 5:
    chon = int(input("Lựa chọn không hợp lệ. Vui lòng nhập lại: "))

if chon == 1:
    print("Bạn đã chọn Cafe.")
elif chon == 2:
    print("Bạn đã chọn Cam vắt.")
elif chon == 3:
    print("Bạn đã chọn Nước ép cà rốt.")
elif chon == 4:
    print("Bạn đã chọn Nước lọc.")
else:
    print("Bạn đã chọn Nước dừa.")