def tim_min(a, b, c):
    return min(a, b, c)

def tim_max(a, b, c):
    return max(a, b, c)

a = int(input("Nhập số thứ nhất: "))
b = int(input("Nhập số thứ hai: "))
c = int(input("Nhập số thứ ba: "))
print("Số nhỏ nhất là:", tim_min(a, b, c))
print("Số lớn nhất là:", tim_max(a, b, c))
