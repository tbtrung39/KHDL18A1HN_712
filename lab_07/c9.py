n = int(input("Nhập số nguyên n: "))
A = {i for i in range(1, n+1) if i % 3 == 0}
B = {i for i in range(1, n+1) if i % 3 != 0}

print("Tập A (chia hết cho 3):", A)
print("Tập B (không chia hết cho 3):", B)
