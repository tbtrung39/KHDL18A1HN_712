a = int(input("Nhập số nguyên a: "))
b = int(input("Nhập số nguyên b: "))

m, n = a, b
while n != 0:
    m, n = n, m % n
bcnn = (a * b) // m

print("Bội chung nhỏ nhất của", a, "và", b, "là:", bcnn)