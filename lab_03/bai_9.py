def tinh_tong_9(n):
    """Tính các tổng S4, S5, S6 bằng vòng lặp for."""
    if n <= 0:
        return "n phải là số nguyên dương"
    
    S4 = sum(i**2 for i in range(1, n + 1))
    S5 = sum((2*i + 1)**3 for i in range(n + 1))
    S6 = sum((2*i)**4 for i in range(1, n + 1))
    return S4, S5, S6

# Ví dụ sử dụng
n = 3
S4, S5, S6 = tinh_tong_9(n)
print(f"S4 = {S4}, S5 = {S5}, S6 = {S6}")