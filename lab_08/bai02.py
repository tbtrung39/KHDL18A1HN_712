def tim_ucln(a, b):
    while b != 0:
        a, b = b, a % b
    return a

tu = int(input("Nhập tử số: "))
mau = int(input("Nhập mẫu số: "))

ucln = tim_ucln(tu, mau)

tu_gon = tu // ucln
mau_gon = mau // ucln

print(f"Phân số rút gọn là: {tu_gon}/{mau_gon}")
