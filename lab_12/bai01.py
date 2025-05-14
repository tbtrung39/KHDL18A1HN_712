def tinh_dien_tich_tam_giac(a, b, c):
    import math
    nữa_chu_vi = (a + b + c) / 2
    return math.sqrt(nữa_chu_vi * (nữa_chu_vi - a) * (nữa_chu_vi - b) * (nữa_chu_vi - c))

try:
    cạnh_a = float(input("Nhập cạnh a: "))
    cạnh_b = float(input("Nhập cạnh b: "))
    cạnh_c = float(input("Nhập cạnh c: "))

    if cạnh_a <= 0 or cạnh_b <= 0 or cạnh_c <= 0:
        raise ValueError("Cạnh phải lớn hơn 0.")
    if cạnh_a + cạnh_b <= cạnh_c or cạnh_a + cạnh_c <= cạnh_b or cạnh_b + cạnh_c <= cạnh_a:
        raise ValueError("Ba cạnh không tạo thành tam giác.")

    diện_tích = tinh_dien_tich_tam_giac(cạnh_a, cạnh_b, cạnh_c)
    print("Diện tích tam giác là:", diện_tích)
except ValueError as lỗi:
    print("Lỗi:", lỗi)