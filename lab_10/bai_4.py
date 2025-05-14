import phuongtrinh

print("Giải phương trình bậc nhất: ax + b = 0")
a = float(input("\ta = "))
b = float(input("\tb = "))
print(phuongtrinh.bac_1(a, b))

print("Giải phương trình bậc hai: ax^2 + bx + c = 0")
a = float(input("\ta = "))
b = float(input("\tb = "))
c = float(input("\tc = "))
print(phuongtrinh.bac_2(a, b, c))