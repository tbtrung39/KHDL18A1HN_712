import math 
x = float(input("Nhập giá trị x: ")) 
a  = -x + math.sqrt(x**2 + 4) 
b  = (x**4 + 1)**(1/7) 
c=a/b
print(f"Giá trị của biểu thức là: {c}") 
