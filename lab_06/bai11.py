import random

# Nhập số lượng phần tử trong danh sách A
n = int(input("Nhập số lượng phần tử trong danh sách A: "))

# Nhập các phần tử của danh sách A
A = [int(input(f"Nhập phần tử thứ {i+1}: ")) for i in range(n)]

# a. Tạo danh sách B chứa các phần tử chia hết cho 3 nhưng không chia hết cho 5 từ danh sách A
B = [x for x in A if x % 3 == 0 and x % 5 != 0]

# In kết quả danh sách B
print("Danh sách B (chia hết cho 3 nhưng không chia hết cho 5):", B)

# b. Tạo danh sách C với các phần tử là bình phương của các phần tử trong danh sách A
C = [x**2 for x in A]

# In kết quả danh sách C
print("Danh sách C (bình phương các phần tử trong danh sách A):", C)

# c. Tạo danh sách D gồm các phần tử chia hết cho 3 từ danh sách A, lấy ngẫu nhiên
D = [x for x in A if x % 3 == 0]

# Nếu danh sách D có phần tử, chọn ngẫu nhiên một phần tử
if D:
    random_choice = random.choice(D)
    print(f"Danh sách D (ngẫu nhiên từ các phần tử chia hết cho 3): [{random_choice}]")
else:
    print("Không có phần tử nào chia hết cho 3 trong danh sách A.")
