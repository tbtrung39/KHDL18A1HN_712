def tinh_tong_8(n):
    """Tính các tổng S1, S2, S3."""
    if n <= 0:
        return "n phải là số nguyên dương"
    
    S1 = n * (n + 1) // 2
    S2 = (n + 1) ** 2
    S3 = n * (n + 1)
    return S1, S2, S3

# Ví dụ sử dụng
n = 5
S1, S2, S3 = tinh_tong_8(n)
print(f"S1 = {S1}, S2 = {S2}, S3 = {S3}")