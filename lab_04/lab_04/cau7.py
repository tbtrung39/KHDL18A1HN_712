a = int(input("Nhập số nguyên a: "))
b = int(input("Nhập số nguyên b: "))
x, y = a, b
while y != 0:
    x, y = y, x % y
bcnn = (a * b) // x
print("Bội chung nhỏ nhất của", a, "và", b, "là:", bcnn)