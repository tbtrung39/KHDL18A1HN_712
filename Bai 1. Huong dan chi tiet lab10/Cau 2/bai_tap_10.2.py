import my_Matrix

# Khoi tao ma tran
A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# A = [['a','b','c'],['b','d','e'],['c','e','f']]

print("Kiem tra ma tran:")
if my_Matrix.isMatrix(A):
    print("A la mot ma tran.")
    print("\nMa tran hien tai:")
    my_Matrix.inMatrix(A)
else:
    print(" A khong phai la ma tran hop le.")

print("\nKiem tra ma tran vuong:")
if my_Matrix.isSquare(A):
    print("A la ma tran vuong.")
else:
    print("A khong phai la ma tran vuong.")

print("\nHoan doi hang:")
if my_Matrix.changeRow(A, 0, 1):
    print("Da hoan doi thanh cong hang 0 va 1!")
    print("\nMa tran sau khi hoan doi:")
    my_Matrix.inMatrix(A)
else:
    print("Hoan doi hang that bai.")

print("\nHoan doi cot:")
if my_Matrix.changeColumn(A, 0, 1):
    print("Da hoan doi thanh cong cot 0 va 1!")
    print("\nMa tran sau khi hoan doi:")
    my_Matrix.inMatrix(A)
else:
    print(" Hoan doi cot that bai.")

print("\nChuyen vi ma tran:")
print("Ma tran hien tai:")
my_Matrix.inMatrix(A)
At = my_Matrix.Transpose(A)
print("Ma tran chuyen vi cua A:")
my_Matrix.inMatrix(At)

print("\nKiem tra doi xung:")
if my_Matrix.getSymetry(A):
    print("A la ma tran doi xung!")
else:
    print(" A khong phai la ma tran doi xung.")
