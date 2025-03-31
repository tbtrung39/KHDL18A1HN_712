import random
n = int(input("Nhập số lượng phần tử trong danh sách A: "))
A = [int(input(f"Nhập phần tử thứ {i+1}: ")) for i in range(n)]
B = [x for x in A if x % 3 == 0 and x % 5 != 0]
print(f"Danh sách B (chia hết cho 3 nhưng không chia hết cho 5): {B}")
C = [x**2 for x in A]
print(f"Danh sách C (bình phương các phần tử trong A): {C}")
D = [x for x in A if x % 3 == 0]
random.shuffle(D)  
print(f"Danh sách D (các phần tử chia hết cho 3 được chọn ngẫu nhiên): {D}")
