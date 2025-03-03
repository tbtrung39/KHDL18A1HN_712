def tong_nghich_dao(n):
    """Tính tổng nghịch đảo của n số nguyên đầu tiên."""
    if n <= 0:
        return "n phải là số nguyên dương"
    
    tong = 0
    for i in range(1, n + 1):
        tong += 1 / i
    return tong

# Ví dụ sử dụng
n = 5
print(f"Tổng nghịch đảo của {n} số nguyên đầu tiên là: {tong_nghich_dao(n)}")