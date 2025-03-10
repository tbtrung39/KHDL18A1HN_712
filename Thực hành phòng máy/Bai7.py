a = int(input("Nhập số nguyên dương a: "))
b = int(input("Nhập số nguyên dương b: "))
while a <= 0 or b <= 0:
    print("Vui lòng nhập hai số nguyên dương!")
    a = int(input("Nhập số nguyên dương a: "))
    b = int(input("Nhập số nguyên dương b: "))
while a != b:
    if a > b:
        a -= b
    else:
        b -= a
print("Ước chung lớn nhất là:", a)
