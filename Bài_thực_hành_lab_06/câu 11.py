import random
n = int(input("Nhập số phần tử n: "))
A = [int(input(f"Nhập phần tử thứ {i+1}: ")) for i in range(n)]

# a. Danh sách B: chia hết cho 3 nhưng không chia hết cho 5
B = [x for x in A if x % 3 == 0 and x % 5 != 0]
print("Danh sách B (chia hết cho 3, không chia hết cho 5):", B)

# b. Danh sách C: bình phương của A
C = [x**2 for x in A]
print("Danh sách C (bình phương của A):", C)

# c. Danh sách D: phần tử ngẫu nhiên từ A chia hết cho 3
D = random.choice([x for x in A if x % 3 == 0]) if any(x % 3 == 0 for x in A) else "Không có số chia hết cho 3"
print("Phần tử ngẫu nhiên từ A chia hết cho 3:", D)