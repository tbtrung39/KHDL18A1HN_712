n = int(input("Nhập số nguyên dương n: "))
while n <= 0:
    print("Vui lòng nhập số nguyên dương!")
    n = int(input("Nhập số nguyên dương n: "))
S4 = 0
S5 = 0
S6 = 0
for i in range(1, n + 1):
    S4 += i ** 2
for i in range(1, n + 1):
    S5 += (2 * i - 1) ** 3
for i in range(1, n + 1):
    S6 += (2 * i) ** 4
print("Tổng S4 = %d" % S4)
print("Tổng S5 = %d" % S5)
print("Tổng S6 = %d" % S6)