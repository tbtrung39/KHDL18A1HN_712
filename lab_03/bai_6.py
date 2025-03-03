def tinh_tong_bac_3(n):
    """Tính tổng bậc 3 của n số nguyên đầu tiên."""
    tong = sum(i**3 for i in range(1, n + 1))
    return tong

# Ví dụ sử dụng
n = 4
print(f"Tổng bậc 3 của {n} số nguyên đầu tiên là: {tinh_tong_bac_3(n)}")