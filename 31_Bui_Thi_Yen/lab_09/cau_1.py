def max3(a, b, c):
    def max2(x, y):
        return x if x > y else y
    return max2(a, max2(b, c))

a = int(input("Nhập số thứ nhất: "))
b = int(input("Nhập số thứ hai: "))
c = int(input("Nhập số thứ ba: "))
print("Số lớn nhất là:", max3(a, b, c))