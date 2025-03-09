n = int(input("Nhập số nguyên dương n: "))  
while n <= 0:
    n = int(input("Vui lòng nhập lại số nguyên dương n: "))

# Tính S4 = 1² + 2² + 3² + ... + n²
S4 = 0
i = 1
while i <= n:
    S4 += i ** 2
    i += 1
print("Tổng S4 =", S4)

# Tính S5 = 1³ + 3³ + 5³ + ... + (2n+1)³
S5 = 0
i = 1
count = 0  
while count < n:
    S5 += i ** 3
    i += 2  
    count += 1
print("Tổng S5 =", S5)

# Tính S6 = 2⁴ + 4⁴ + 6⁴ + ... + (2n)⁴
S6 = 0
i = 2
count = 0  
while count < n:
    S6 += i ** 4
    i += 2 
    count += 1
print("Tổng S6 =", S6)