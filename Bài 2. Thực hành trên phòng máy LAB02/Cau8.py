# Cau8.
luong_can_ban = 1350000
TNCT = int(input("Nhập vào thâm niên công tác (số tháng): "))
if TNCT < 12:
    he_so = 2.34
elif 12 <= TNCT < 36:
    he_so = 3.33
elif 36 <= TNCT < 60:
    he_so = 3.66
else: 
    he_so = 3.99
luong = he_so * luong_can_ban
print(f"Lương của nhân viên là: {luong} đồng")
