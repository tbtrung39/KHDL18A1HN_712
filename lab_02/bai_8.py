print("Chương trình tính lương nhân viên")
tnct = int(input("Nhập thâm niên công tác (tháng): "))
luong_cb = 1350000
if tnct < 12:
    he_so = 2.34
elif 12 <= tnct < 36:
    he_so = 3.33
elif 36 <= tnct < 60:
    he_so = 3.66
else:
    he_so = 3.99
luong = he_so * luong_cb
print("Lương nhân viên là %0.0f đồng" % luong)
