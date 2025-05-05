import sys

# Thêm đường dẫn chứa mypackage
sys.path.append("H:\\BỔ TRỢ\\Tài liệu\\Lớp 12\\3. THỰC TẬP LẬP TRÌNH CƠ BẢN KHDL\\Bai 1. Huong dan chi tiet lab10\\Cau 5")

# Import package
import mypackage

# Tạo 2 ma trận A và B
A = [[1, 1, 1], [1, 0, 0], [-1, 1, 2]]
B = [[0, 1, 3], [2, 3, 4], [0, 2, 3]]

# In ma trận A
print("Ma trận A:")
mypackage.inMatrix(A)

# In ma trận B
print("Ma trận B:")
mypackage.inMatrix(B)

# Cộng A + B
print("Tổng ma trận A + B:")
C = mypackage.add_matrix(A, B)
mypackage.inMatrix(C)

# Nhân A x B
print("Tích ma trận A x B:")
D = mypackage.mul_matrix(A, B)
mypackage.inMatrix(D)
