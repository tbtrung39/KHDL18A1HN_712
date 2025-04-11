tong_tien = 0

print("Nhập giao dịch (ví dụ: D 100 hoặc W 200). Nhấn Enter để kết thúc:")

while True:
    dong = input()
    if not dong:
        break
    loai, so_tien = dong.split()
    so_tien = int(so_tien)
    if loai == 'D':
        tong_tien += so_tien
    elif loai == 'W':
        tong_tien -= so_tien

print("Số dư cuối cùng:", tong_tien)