# Cau 5.

def ucln(a,b):
    while b !=0:
        a, b = b, a%b
    return a
a = int(input("Nhập số a: "))
b = int(input("Nhập số b: "))
print("Ước chung lớn nhất là: ",ucln(a,b) )