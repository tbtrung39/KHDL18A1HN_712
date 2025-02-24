luong_co_ban = 1350000
TNCT = int(input("Nhập số tháng thâm niên công tác: "))
if TNCT < 12:
    he_so = 2.34
elif TNCT < 36:
    he_so = 3.33
elif TNCT < 60:
    he_so = 3.66
else:
    he_so = 3.99
luong = he_so * luong_co_ban
print("Lương của nhân viên là:", luong)
