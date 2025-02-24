kw = float(input("Nhập số KW điện tiêu thụ: "))
if 0 <= kw <= 100:
    tien_dien = kw * 2000
elif 101 <= kw <= 200:
    tien_dien = kw * 2500
elif 201 <= kw <= 300:
    tien_dien = kw * 3000
else:
    tien_dien = kw * 5000

print(f"Tiền điện phải trả là: {tien_dien:,.0f} đồng")