kw = int(input("Nhập số kWh tiêu thụ: "))
if kw <= 100:
    cost = kw * 2000
elif kw <= 200:
    cost = 100 * 2000 + (kw - 100) * 2500
elif kw <= 300:
    cost = 100 * 2000 + 100 * 2500 + (kw - 200) * 3000
else:
    cost = 100 * 2000 + 100 * 2500 + 100 * 3000 + (kw - 300) * 5000

print(f"Tiền điện phải trả: {cost} đồng")