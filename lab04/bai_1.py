n = int(input("Nhập số nguyên dương n: "))
while n <= 0:
    n = int(input("Vui lòng nhập lại n: "))
#C
S4 = 0
i = 1
while i <= n:
    S4 += i**2
    i += 1
print("S4 =", S4)

# Câu b:
S5 = 0
i = 1
while i <= n:
    S5 += (2*i - 1)**3
    i += 1
print("S5 =", S5)

# Câu c:
S6 = 0
i = 1
while i <= n:
    S6 += (2*i)**4
    i += 1
print("S6 =", S6)
