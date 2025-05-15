import doicoso2

chuoi = input("Nhập chuỗi ký tự: ")

chuoi_loc = doicoso2.loc_ky_tu_hop_le(chuoi)
print("Chuỗi sau khi loại bỏ ký tự không hợp lệ:", chuoi_loc)

coso_hop_le = doicoso2.cac_co_so_hop_le(chuoi_loc)
print("Chuỗi hợp lệ ở các hệ cơ số:", coso_hop_le)
for cs in [2, 8, 16]:
    if cs in coso_hop_le:
        ket_qua = doicoso2.doi_coso_ve_10(chuoi_loc, cs)
        print(f"Giá trị hệ 10 nếu chuỗi thuộc cơ số {cs}: {ket_qua}")
    else:
        print(f"Chuỗi không hợp lệ với cơ số {cs}.")
