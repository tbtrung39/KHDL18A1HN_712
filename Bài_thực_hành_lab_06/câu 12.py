# Khởi tạo số dư ban đầu
so_du = 0

print("Nhập các giao dịch (mỗi dòng 1 giao dịch, Enter để kết thúc):")
print("Định dạng: D [số tiền] (gửi tiền) hoặc W [số tiền] (rút tiền)")

while True:
    giao_dich = input().strip()
    
    # Kết thúc khi người dùng nhập dòng trống
    if not giao_dich:
        break
    
    try:
        # Tách loại giao dịch và số tiền
        loai, so_tien = giao_dich.split()
        so_tien = int(so_tien)
        
        # Xử lý giao dịch
        if loai.upper() == 'D':
            so_du += so_tien
        elif loai.upper() == 'W':
            so_du -= so_tien
        else:
            print(f"Loại giao dịch không hợp lệ: {loai} (bỏ qua)")
    except ValueError:
        print(f"Định dạng không hợp lệ: {giao_dich} (bỏ qua)")

# In kết quả
print(f"Số dư hiện tại trong tài khoản: {so_du}")