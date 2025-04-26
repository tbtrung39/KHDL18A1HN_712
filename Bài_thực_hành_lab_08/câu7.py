def min_max(a, b, c):
    return min(a, b, c), max(a, b, c)

a = int(input("Nhập số thứ nhất: "))
b = int(input("Nhập số thứ hai: "))
c = int(input("Nhập số thứ ba: "))

nho, lon = min_max(a, b, c)
print(f"Số nhỏ nhất là: {nho}")
print(f"Số lớn nhất là: {lon}")
