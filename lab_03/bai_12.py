def tinh_so_kiem_tra_container(ma_container):
    """Tính số kiểm tra container."""
    ma_chu = {
        'A': 10, 'B': 12, 'C': 13, 'D': 14, 'E': 15, 'F': 16, 'G': 17, 'H': 18, 'I': 19, 'J': 20,
        'K': 21, 'L': 23, 'M': 24, 'N': 25, 'O': 26, 'P': 27, 'Q': 28, 'R': 29, 'S': 30, 'T': 31,
        'U': 32, 'V': 34, 'W': 35, 'X': 36, 'Y': 37, 'Z': 38
    }
    
    trong_so = []
    for i, ky_tu in enumerate(ma_container):
        if ky_tu.isalpha():
            gia_tri = ma_chu[ky_tu]
        else:
            gia_tri = int(ky_tu)
        trong_so.append(gia_tri * (2**i))
    
    tong_trong_so = sum(trong_so)
    so_kiem_tra = tong_trong_so % 11
    return so_kiem_tra

# Ví dụ sử dụng
ma_container = "SUDU307007"
print(f"Số kiểm tra của mã container {ma_container} là: {tinh_so_kiem_tra_container(ma_container)}")