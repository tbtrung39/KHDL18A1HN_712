def tim_trong_tam_tam_giac(A, B, C):
    """Tìm trọng tâm tam giác."""
    x = (A[0] + B[0] + C[0]) / 3
    y = (A[1] + B[1] + C[1]) / 3
    return round(x, 2), round(y, 2)

# Ví dụ sử dụng
A = (1, 2)
B = (3, 4)
C = (5, 6)
x, y = tim_trong_tam_tam_giac(A, B, C)
print(f"Trọng tâm tam giác: ({x}, {y})")