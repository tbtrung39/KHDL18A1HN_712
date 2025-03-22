# Nhập giá trị x từ người dùng
x = float(input("Nhập giá trị của x: "))

# Tính tử số
tu_so = -x + (x**2 + 4)**0.5

# Tính mẫu số
mau_so = (x**4 + 1)**(1/7)

# Tính giá trị của biểu thức f(x)
if mau_so == 0:
    print("Mẫu số bằng 0, biểu thức không xác định.")
else:
    f_x = tu_so / mau_so
# Làm tròn kết quả đến hai chữ số thập phân
    f_x_rounded = round(f_x, 2)
    # In kết quả
    print("f(x) =", f_x)