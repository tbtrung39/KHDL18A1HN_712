TNCT = int(input("Nhập thông niên công tác của nhân viên(tháng) : "))
he_so = 0 
if TNCT < 12 : 
    he_so = 2.34
elif TNCT <36 : 
    he_so = 3.33
elif TNCT < 60 : 
    he_so = 3.66 
else : 
    he_so = 3.99
luong = he_so * 1350000
print("Lương của nhân viên dựa theo thâm niên công tác là : ", luong )