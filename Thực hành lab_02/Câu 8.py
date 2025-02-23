#Câu 8:
tnct = int(input("Nhập vào thâm niên công tác:"))
if tnct <12 :
    he_so = 2.34
elif tnct <36 :
    he_so = 3.33
elif tnct <60 :
    he_so = 3.66
else: he_so = 3.99
luong = he_so*1350000
print(luong)