def tinh_xac_suat(n):
    # Xác suất để cả 3 xúc xắc cùng ra 6 trong 1 lần tung
    p = (1/6) * (1/6) * (1/6)  # (1/6)^3
    # Xác suất không có lần nào cả 3 xúc xắc cùng ra 6 trong n lần tung
    q = 1 - p
    # Xác suất có ít nhất một lần cả 3 xúc xắc ra 6
    xac_suat = 1 - (q ** n)
    return round(xac_suat, 2)  # Làm tròn đến 2 chữ số thập phân

# Nhập số lần tung xúc xắc
n = int(input("Nhập số lần tung xúc xắc: "))

# Tính và hiển thị xác suất
print(f"Xác suất có ít nhất một lần cả 3 xúc xắc ra 6: {tinh_xac_suat(n)}")