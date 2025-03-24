str = input("Nhập chuỗi nhị phân: ")
gia_tri_ban_dau = 0

for i in range(len(str)):
    bit = int(str[i])  
    gia_tri_ban_dau = gia_tri_ban_dau * 2 + bit  

print(f"Số thập phân là: {gia_tri_ban_dau}")
