n = int(input("Nhập số nguyên dương n: "))
count = 0
tong = 0

print(f"Các ước số của {n} là:")
for i in range(1, n + 1):
    if n % i == 0:
        print(i, end=" ")
        count += 1
        tong += i

print(f"\nSố lượng ước số của {n} là: {count}")
print(f"Tổng các ước số của {n} là: {tong}")
