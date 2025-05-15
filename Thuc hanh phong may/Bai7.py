def tim_lon_nhat(a, b, c):
    return max(a, b, c)
def tim_nho_nhat(a, b, c):
    return min(a, b, c)
a = int(input("Nhập số nguyên thứ nhất: "))
b = int(input("Nhập số nguyên thứ hai: "))
c = int(input("Nhập số nguyên thứ ba: "))

print("Số lớn nhất là:", tim_lon_nhat(a, b, c))
print("Số nhỏ nhất là:", tim_nho_nhat(a, b, c))
