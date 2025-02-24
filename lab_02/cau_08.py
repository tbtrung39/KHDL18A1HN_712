tnct = int(input("Nhập thâm niên công tác (tháng): "))
if 0 <= tnct < 12:
    he_so = 2.34
elif 12 <= tnct < 36:
    he_so = 3.33
elif 36 <= tnct < 60:
    he_so = 3.66
else:
    he_so = 3.99
luong_cban = 1350000
luong = he_so * luong_cban
print(f"Lương của nhân viên với thâm niên {tnct} tháng là: {luong:.2f} đồng.")
