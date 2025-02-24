TNCT = int(input("Nhập số tháng công tác: "))

luong_cb = 1350000

if TNCT < 12:
    he_so = 2.34
elif 12 <= TNCT < 36:
    he_so = 3.33
elif 36 <= TNCT < 60:
    he_so = 3.66
else:
    he_so = 3.99

luong = he_so * luong_cb
print("Lương nhân viên:", luong, "VNĐ")
