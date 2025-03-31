# bai17
n = int(input("Nhập bậc của ma trận đơn vị n: "))

A = [[1 if i == j else 0 for j in range(n)] for i in range(n)]

print("Ma trận đơn vị bậc", n, ":")
for row in A:
    print(row)
