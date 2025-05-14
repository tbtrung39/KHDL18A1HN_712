#Câu 10:
n = int(input("Nhập số nguyên dương n: "))
print(f"Các ước số của {n} là:")
for i in range(1, n + 1):
    if n % i == 0:
        print(i, end=" ")