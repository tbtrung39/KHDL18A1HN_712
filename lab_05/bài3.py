n = int(input("Nhập số tự nhiên n: "))
binary_str = ""
while n > 0:
    binary_str = str(n % 2) + binary_str
    n //= 2

print("Chuỗi nhị phân:", binary_str if binary_str else "0")