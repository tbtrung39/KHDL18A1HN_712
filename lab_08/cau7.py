def tim_max(a, b, c):
    return max(a, b, c)

def tim_min(a, b, c):
    return min(a, b, c)

x = int(input("Nhập số thứ nhất: "))
y = int(input("Nhập số thứ hai: "))
z = int(input("Nhập số thứ ba: "))

so_lon_nhat = tim_max(x, y, z)
so_nho_nhat = tim_min(x, y, z)

print(f"Số lớn nhất là: {so_lon_nhat}")
print(f"Số nhỏ nhất là: {so_nho_nhat}")
