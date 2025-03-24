chuoi_nhi_phan = input("Nhập số nhị phân: ")
hop_le = True
for ky_tu in chuoi_nhi_phan:
    if ky_tu not in "01":
        hop_le = False
        break
if hop_le:
    so_thap_phan = 0
    for ky_tu in chuoi_nhi_phan:
        so_thap_phan = so_thap_phan * 2 + int(ky_tu)

    print("Số thập phân tương ứng:", so_thap_phan)
else:
    print("Chuỗi không hợp lệ! Chỉ được chứa '0' và '1'.")