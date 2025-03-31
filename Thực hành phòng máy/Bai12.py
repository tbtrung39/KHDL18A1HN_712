so_du = 0
while True:
    nhap = input("Nhập giao dịch (D/W số tiền), hoặc nhấn Enter để dừng: ")
    if nhap == "":
        break
    loai, so_tien = nhap.split()
    so_tien = int(so_tien)
    if loai == "D":
        so_du += so_tien
    elif loai == "W":
        so_du -= so_tien
print("Số dư cuối cùng:", so_du)