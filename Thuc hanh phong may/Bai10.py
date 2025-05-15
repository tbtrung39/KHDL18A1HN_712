n = int(input("Nhập số nguyên dương n: "))
if n <= 0:
    print("Vui lòng nhập số nguyên dương.")
else:
    print(f"Các ước số của {n} là:")
    for i in range(1, n + 1):
        if n % i == 0:
            print(i, end=" ")
