import math
x = float(input("Nhập giá trị x (radian): "))
cos_x = 1  
term = 1  
N = 1 
while abs(term) >= 1e-6:  
    term = (-1)**N * (x**(2*N)) / math.factorial(2*N)
    cos_x += term
    N += 1
print(f"cos({x}) ≈ {cos_x}")
