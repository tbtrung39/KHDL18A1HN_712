def tinh_ket_qua(n):
    """Tính kết quả của phép toán với n số hạng."""
    tong = 0
    mau = 1
    for i in range(1, n + 1):
        tu = 2 * i + 1
        mau *= (2 * i) * (2 * i + 1)
        tong += tu / mau
    return round(tong, 3)

# Ví dụ sử dụng
n = 3
print(f"Kết quả phép toán với {n} số hạng là: {tinh_ket_qua(n)}")