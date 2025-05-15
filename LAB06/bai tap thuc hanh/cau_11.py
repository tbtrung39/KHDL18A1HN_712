import random
n = int(input("Nhap so luong phan tu: "))
A = [random.randint(1, 200) for _ in range(n)]
B = [x for x in A if x % 5 == 0]
C = [x for x in A if x % 3 != 0]
D = [x**2 for x in A]
print("A:", A)
print("B (chia het cho 5):", B)
print("C (khong chia het cho 3):", C)
print("D (binh phuong):", D)