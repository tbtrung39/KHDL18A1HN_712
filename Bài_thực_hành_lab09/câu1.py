def max_recursive(a, b):
    if a > b:
        return a
    else:
        return b

# Hàm tìm max trong 3 số
def max_of_three(a, b, c):
    return max_recursive(max_recursive(a, b), c)

# Nhập từ bàn phím
a = int(input("Nhập số thứ nhất: "))
b = int(input("Nhập số thứ hai: "))
c = int(input("Nhập số thứ ba: "))

print("Số lớn nhất là:", max_of_three(a, b, c))

