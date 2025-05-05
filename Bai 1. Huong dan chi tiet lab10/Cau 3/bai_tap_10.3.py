import Tinh_Toan_Matrix as my_Matrix

A = [[1, 2, 3], [4, 5, 6]]
B = [[7, 8, 9], [10, 11, 12]]

print('Tong cua 2 ma tran A + B:')
C = my_Matrix.add_matrix(A, B)
print(C)
my_Matrix.inMatrix(C)

print('Hieu cua 2 ma tran A - B:')
D = my_Matrix.sub_matrix(A, B)
print(D)
my_Matrix.inMatrix(D)
print('Tich cua 2 ma tran A x B:')
E = my_Matrix.mul_matrix(A, B)
print(E)
my_Matrix.inMatrix(E)