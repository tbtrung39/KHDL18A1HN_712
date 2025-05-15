# Cau 10.
a = int(input("Nhap so tu nhien a: "))
b = int(input("Nhap so tu nhien b: "))

tap_a = set(str(a))
tap_b = set(str(b))

print("Cac chu so trong a:", tap_a)
print("Cac chu so trong b:", tap_b)
print("Chu so xuat hien o ca 2:", tap_a & tap_b)
print("Chu so khong lap:", (tap_a | tap_b) - (tap_a & tap_b))