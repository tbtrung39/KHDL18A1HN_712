import giai_pt

def menu():
    print("Chọn loại phương trình:")
    print("1. Phương trình bậc nhất (ax + b = 0)")
    print("2. Phương trình bậc hai (ax^2 + bx + c = 0)")
    choice = input("Nhập lựa chọn (1 hoặc 2): ")
    return choice

choice = menu()

if choice == "1":
    a = float(input("Nhập a: "))
    b = float(input("Nhập b: "))
    result = giai_pt.giai_bac_nhat(a, b)
    print(result)
elif choice == "2":
    a = float(input("Nhập a: "))
    b = float(input("Nhập b: "))
    c = float(input("Nhập c: "))
    result = giai_pt.giai_bac_hai(a, b, c)
    print(result)
else:
    print("Lựa chọn không hợp lệ.")