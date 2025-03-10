x = float(input("Nhập giá trị x: "))
n = int(input("Nhập số nguyên dương n: "))
while n <= 0:
    n = int(input("Vui lòng nhập lại số nguyên dương n: "))
cos_x = 1
i = 3
while i <= n:
    cos_x -= (x ** i) / (i * (i - 1))
    i += 2

print("Giá trị gần đúng của cos(x) =", cos_x)