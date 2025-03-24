n = int(input("Nhập một số tự nhiên: "))
nhi_phan = ""
if n == 0:
    nhi_phan = "0"
else:
    while n > 0:
        du = n % 2
        nhi_phan = str(du) + nhi_phan
        n = n // 2
print("Chuỗi nhị phân là:", nhi_phan)
