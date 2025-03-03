def tinh_tich_vo_huong(a, b):
    """Tính tích vô hướng của 2 vector."""
    if len(a) != len(b):
        return "Hai vector không cùng chiều"
    return sum(a[i] * b[i] for i in range(len(a)))

# Ví dụ sử dụng
a = [1, 2, 3]
b = [4, 5, 6]
print(f"Tích vô hướng: {tinh_tich_vo_huong(a, b)}")