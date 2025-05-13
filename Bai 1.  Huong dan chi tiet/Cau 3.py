# Cau 3.

sum = 0
try:
    with open('Bai 1.  Huong dan chi tiet/data.dat', 'r') as f:
        for line in f:
            sum += int(line)
except FileNotFoundError:
    print("Khong tim thay file")
except PermissionError:
    print("Khong co quyen truy cap file")
except ValueError:
    print("Loi dinh dang du lieu")
else:
    print("Tong day so da cho la:", sum)
