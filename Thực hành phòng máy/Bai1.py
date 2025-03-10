n = int(input("Nhập số nguyên dương n: "))
while n <= 0:
    n = int(input("Số không hợp lệ! Nhập lại n: "))
S4 = 0
i = 1
while i <= n:
    S4 += i**2
    i += 1
S5 = 0
i = 1
count = 0
while count < n:
    S5 += i**3
    i += 2
    count += 1
S6 = 0
i = 2
count = 0
while count < n:
    S6 += i**4
    i += 2
    count += 1
print("S4 =", S4)
print("S5 =", S5)
print("S6 =", S6)
