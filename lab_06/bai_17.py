# Câu 17
n = int(input("Nhap n: "))
A = [[1 if i == j else 0 for j in range(n)] for i in range(n)]
for row in A:
    print(row)