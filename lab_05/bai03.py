n = int(input("Nhập số tự nhiên n: "))
if n == 0:
    chuoi_nhi_phan = "0"
else:
    chuoi_nhi_phan = ""
    while n > 0:
        chuoi_nhi_phan = str(n % 2) + chuoi_nhi_phan
        n = n // 2
print(f"Số trong hệ nhị phân là: {chuoi_nhi_phan}")
