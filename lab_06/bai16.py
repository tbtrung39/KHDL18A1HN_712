# bai16
X = int(input("Nhập X: "))
Y = int(input("Nhập Y: "))

matrix = [[i * j for j in range(Y)] for i in range(X)]

for row in matrix:
    print(row)
