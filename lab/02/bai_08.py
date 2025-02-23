TNCT = int(input("Nhập số tháng thâm niên công tác: "))
luong_co_ban = 1350000  # Lương căn bản

if TNCT < 12:
    he_so = 2.34
elif TNCT < 36:
    he_so = 3.33
elif TNCT < 60:
    he_so = 3.66
else:
    he_so = 3.99

luong = he_so * luong_co_ban
print(f"Lương nhân viên: {round(luong, 2)} VNĐ")