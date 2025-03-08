from fractions import Fraction

while True:
    tu = int(input("Nhập tử số: "))
    mau = int(input("Nhập mẫu số: "))
    if mau != 0:
        break
    print("Mẫu số phải khác 0, vui lòng nhập lại.")

phan_so = Fraction(tu, mau)
print("Phân số rút gọn:", phan_so)
