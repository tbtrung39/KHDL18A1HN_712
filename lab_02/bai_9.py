print("Chương trình tính tiền điện")
kw = int(input("Nhập số KW điện tiêu thụ: "))
if 0 <= kw <= 100:
    don_gia = 2000
elif 101 <= kw <= 200:
    don_gia = 2500
elif 201 <= kw <= 300:
    don_gia = 3000
else:
    don_gia = 5000
tien_dien = kw * don_gia
print("Tiền điện phải trả là %0.0f đồng" % tien_dien)