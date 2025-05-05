import giaipt

print("Giải phương trình bậc nhất ax + b = 0")
a = float(input("Nhập a: "))
b = float(input("Nhập b: "))
print("Kết quả:", giaipt.giai_pt_bac_1(a, b))

print("\nGiải phương trình bậc hai ax² + bx + c = 0")
a = float(input("Nhập a: "))
b = float(input("Nhập b: "))
c = float(input("Nhập c: "))
print("Kết quả:", giaipt.giai_pt_bac_2(a, b, c))
