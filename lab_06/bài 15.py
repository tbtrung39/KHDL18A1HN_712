X, Y = map(int, input("Nhập giá trị X và Y (cách nhau bằng dấu cách): ").split())
matrix = [[i * j for j in range(Y)] for i in range(X)]
print(matrix)