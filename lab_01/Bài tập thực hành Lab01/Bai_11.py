n = int(input("Nhập số lần tung xúc sắc: "))
p = (1/6) ** 3
khongra6 = (1 - p) ** n
ra6 = 1 - khongra6
print("Xác suất có ít nhất 1 lần cả 3 viên xúc sắc ra 6 là:", round(ra6, 2))