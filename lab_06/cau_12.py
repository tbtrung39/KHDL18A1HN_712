so_du = 0
while True:
    giao_dich = input("Nhập giao dịch (hoặc 'kết thúc' để kết thúc): ")
    
    if giao_dich.lower() == 'kết thúc':
        break  
    hanh_dong, so_tien = giao_dich.split()
    so_tien = int(so_tien)  
    if hanh_dong == 'D':  
        so_du += so_tien  
    elif hanh_dong == 'W':  
        so_du -= so_tien  
print("Số tiền thực tế trong tài khoản là:", so_du)
