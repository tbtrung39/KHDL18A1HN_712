import math

x = float(input("Nhap gia tri x (radian): "))
cos_x = 1
term = 1
n = 1

while abs(term) >= 1e-4:  
    term = (-1)**n * (x**(2*n)) / math.factorial(2*n)
    
    if abs(term) > 1e308: 
        print("Lỗi: Giá trị quá lớn để tính toán!")
        break

    cos_x += term
    n += 1

print(f"cos({x}) ~ {cos_x}")
