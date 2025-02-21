print("Giải nghiệm phương trình bậc 2: ")
a = int(input("Nhập a : "))
b = int(input("Nhập b : "))
c = int(input("Nhập c : "))
delta = b*b -4*a*c
if delta > 0 :
    x1 = (-b+delta**(1/2))/(2*a)
    x2 = (-b-delta**(1/2))/(2*a)
    print(f"Phương trình có 2 nghiệm phân biệt là{x1} và {x2}")
elif delta == 0 : 
    x = -b /(2*a)
    print("Phương trình có nghiệm kép là ",x)
else : 
    print("Phương trình không có nghiệm thực")
