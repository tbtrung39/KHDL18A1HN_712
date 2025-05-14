# Câu 1. Vòng lặp while
# a) In ra các số từ 1 đến 10 bằng while.
# b) Tính tổng các số chẵn từ 1 đến 100.
# c) Nhập số n và tính giai thừa của n.

# a.
i = 1
while i <= 10:
    print(i, end=" ")
    i += 1
print("\n")

# b.
i = 2
tong = 0
while i <= 100:
    tong += i
    i += 2
print("Tổng các số chẵn từ 1 đến 100 là:", tong)
print()

# c.
n = int(input("Nhập số nguyên dương n: "))
i = 1
giaithua = 1
while i <= n:
    giaithua *= i
    i += 1
print(f"Giai thừa của {n} là: {giaithua}")
