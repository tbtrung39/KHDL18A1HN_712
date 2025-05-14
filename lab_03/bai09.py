# a
n = int(input("Nhập số nguyên dương n: "))
if n <= 0:
    print("Vui lòng nhập một số nguyên dương lớn hơn 0.")
    n = int(input("Nhập số nguyên dương n: "))
S4 = 0
for i in range(1, n+1):
    S4 += i**2  
print(f"S4 = {S4}")

# b
n = int(input("Nhập số nguyên dương n: "))
if n <= 0:
    print("Vui lòng nhập một số nguyên dương lớn hơn 0.")
    n = int(input("Nhập số nguyên dương n: "))
S5 = 0
for i in range(1, n+1):
    so_le = 2 * i - 1  
    S5 += so_le**3  
print(f"S5 = {S5}")

# c
n = int(input("Nhập số nguyên dương n: "))
if n <= 0:
    print("Vui lòng nhập một số nguyên dương lớn hơn 0.")
    n = int(input("Nhập số nguyên dương n: "))
S6 = 0
for i in range(1, n+1):
    so_chan = 2*i
    S6 += so_chan**4
print(f"S6 = {S6}")


