n = int(input("Nhập n: "))

for i in range(2, int(n ** 0.5) + 1):
    if n % i == 0:
        print(f"{n} không phải là số nguyên tố.")
        break
else:
    print(f"{n} là số nguyên tố.")
    exit()

for i in range(n - 1, 1, -1):
    for j in range(2, int(i ** 0.5) + 1):
        if i % j == 0:
            break
    else:
        print(f"Số nguyên tố gần nhất là {i}")
        break
