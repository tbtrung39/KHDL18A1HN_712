import ptbac

print("Giải phương trình bậc nhất ax + b = 0")
a = float(input("Nhập a: "))
b = float(input("Nhập b: "))
print(ptbac.giai_pt_bac_1(a, b))

print("\nGiải phương trình bậc hai ax^2 + bx + c = 0")
a = float(input("Nhập a: "))
b = float(input("Nhập b: "))
c = float(input("Nhập c: "))
print(ptbac.giai_pt_bac_2(a, b, c))
