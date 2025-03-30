n = int(input("Nhập số lượng phần tử của danh sách A: "))
A = [int(input(f"Nhập phần tử thứ {i+1}: ")) for i in range(n)]

B = [x for x in A if x % 3 == 0 and x % 5 != 0]
print("Danh sách B:", B)

C = [x**2 for x in A]
print("Danh sách C:", C)

import random
D = random.sample([x for x in A if x % 3 == 0], random.randint(0, len(A)//3))
print("Danh sách D:", D)