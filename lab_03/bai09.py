#CÂU A
n = int(input("Nhập số nguyên dương n: "))
if n <= 0:
    print("Vui lòng nhập một số nguyên dương lớn hơn 0.")
    n = int(input("Nhập số nguyên dương n: "))
S4 = 0
for i in range(1, n+1):
    S4 += i**2  
print(f"Tổng S4 (1^2 + 2^2 + 3^2 + ... + n^2) là: {S4}")

#CÂU B
n = int(input("Nhập số nguyên dương n: "))
if n <= 0:
    print("Vui lòng nhập một số nguyên dương lớn hơn 0.")
    n = int(input("Nhập số nguyên dương n: "))
S5 = 0
for i in range(1, n+1):
    so_le = 2 * i - 1  
    S5 += so_le**3  
print(f"Tổng S5 (1^3 + 3^3 + 5^3 + ... + (2n+1)^3) là: {S5}")

# CÂU C 
n = int(input("Nhập số nguyên dương n: "))
if n <= 0:
    print("Vui lòng nhập một số nguyên dương lớn hơn 0.")
    n = int(input("Nhập số nguyên dương n: "))
S6 = 0
for i in range(1, n+1):
    so_chan = 2 * i  # Tính số chẵn tương ứng (2, 4, 6, ...)
    S6 += so_chan**4  # Cộng bình phương của số chẵn vào tổng
print(f"Tổng S6 (2^4 + 4^4 + 6^4 + ... + (2n)^4) là: {S6}")


