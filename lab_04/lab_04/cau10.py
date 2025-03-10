n = int(input("Nhập số thập phân: "))
s = ""
while n > 0:
    du = n % 2
    s = str(du) + s
    n = n // 2
print("Số nhị phân là:", s)