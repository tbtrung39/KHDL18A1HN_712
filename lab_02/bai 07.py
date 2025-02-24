so_kw = int(input("Nhập số kWh tiêu thụ: "))

if so_kw > 300:
    tien = so_kw * 5000
elif so_kw > 200:
    tien = so_kw * 3000
elif so_kw > 100:
    tien = so_kw * 2500
else:
    tien = so_kw * 2000

print("Số tiền điện phải trả:", tien, "VNĐ")
