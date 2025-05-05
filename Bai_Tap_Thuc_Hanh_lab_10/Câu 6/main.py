import doicoso2

chuoi = input("Nhập vào chuỗi ký tự: ")

chuoi_hop_le = doicoso2.loc_chuoi_16(chuoi)

coso = doicoso2.xac_dinh_co_so(chuoi_hop_le)
if coso:
    print(f"Chuỗi thuộc hệ cơ số: {coso}")
else:
    print("Không xác định được cơ số.")

if coso == 2:
    doicoso2.doi_co_so_2_sang_10(chuoi_hop_le)
elif coso == 8:
    doicoso2.doi_co_so_8_sang_10(chuoi_hop_le)
elif coso == 16:
    doicoso2.doi_co_so_16_sang_10(chuoi_hop_le)
elif coso == 10:
    print(f"Chuỗi đã ở cơ số 10: {chuoi_hop_le}")
else:
    print("Không thể chuyển đổi chuỗi.")