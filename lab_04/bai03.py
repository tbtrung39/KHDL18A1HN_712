import math
x=float(input("Nhập x(radian): "))
epsilon=1e-4
cos_x=1
term=1
n=1
while abs(term)> epsilon:
    term *= -x**2/((2*n-1) * (2*n))
    cos_x +=term
    n+=1
print(f"giá trị gần đúng của cos({x}) là: {cos_x}")
print(f"giá trị thực từ math.cos({x}) là: {math.cos(x)}")
