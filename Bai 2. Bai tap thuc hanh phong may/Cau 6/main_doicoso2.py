import doicoso2

chuoi = input("Nhap vao mot chuoi ky tu: ")
chuoi_sach = doicoso2.loai_bo_ky_tu_khong_hop_le(chuoi)
print("Chuoi sau khi loai bo ky tu khong hop le:", chuoi_sach)

co_so = doicoso2.xac_dinh_co_so(chuoi_sach)
if co_so == -1:
    print("Khong xac dinh duoc co so cua chuoi.")
else:
    print("Chuoi co the thuoc he co so:", co_so)

    if co_so == 2:
        print("Chuyen sang he 10:", doicoso2.doi_co_so_2_sang_10(chuoi_sach))
    elif co_so == 8:
        print("Chuyen sang he 10:", doicoso2.doi_co_so_8_sang_10(chuoi_sach))
    elif co_so == 16:
        print("Chuyen sang he 10:", doicoso2.doi_co_so_16_sang_10(chuoi_sach))
    else:
        print("Chuoi da o he 10, khong can chuyen doi.")
