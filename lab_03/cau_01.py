n = int(input("Nhập vào số phần tử n: "))
tong = 1
tich = 1
for i in range(1, n + 1):
    tich *= (2 * i) / (2 * i + 1)
    tong += tich
tong = round(tong, 3)
print("Kết quả là:", tong)
