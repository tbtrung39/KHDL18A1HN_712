kw = int(input("Nhập số KW điện tiêu thụ: "))

if kw >= 0 and kw <= 100:
    tien = kw * 2000
elif kw > 100 and kw <= 200:
    tien = 100 * 2000 + (kw - 100) * 2500
elif kw > 200 and kw <= 300:
    tien = 100 * 2000 + 100 * 2500 + (kw - 200) * 3000
elif kw > 300:
    tien = 100 * 2000 + 100 * 2500 + 100 * 3000 + (kw - 300) * 5000
else:
    tien = 0  # Trường hợp nhập số KW âm
print("Tiền điện phải trả:", tien, "đồng")