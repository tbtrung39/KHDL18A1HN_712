kw = float(input("Nhập số kw điện tiêu thụ"))
if 0<=kw<=100:
    don_gia = 2000
elif kw<=200:
    don_gia = 2500
elif kw<=300:
    don_gia = 3000
else:
    don_gia = 5000
tien_dien = kw*don_gia
print("tiền điện phải trả là",tien_dien) 