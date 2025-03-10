print("===== MENU ĐỒ UỐNG =====")
print("1. Cafe")
print("2. Cam vắt")
print("3. Nước ép cà rốt")
print("4. Nước lọc")
print("5. Nước dừa")
lua_chon = int(input("Nhập số tương ứng với đồ uống bạn muốn gọi: "))
if lua_chon == 1:
    print('Bạn đã chọn: Cafe')
elif lua_chon == 2:
    print("Bạn đã lựa chọn Cam vắt")
elif lua_chon == 3:
    print("bạn đã lựa chọn Nước ép cà rốt")
elif lua_chon == 4:
    print("Bạn đã lựa chọn Nước lọc")
elif lua_chon == 5:
    print("Bạn đã lựa chọn Nước dừa")
else:
    print("Lựa chọn không hợp lệ! Vui lòng chọn từ 1 đến 5.")