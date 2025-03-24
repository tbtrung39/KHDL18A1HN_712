nhi_phan = input("Nhập chuỗi nhị phân (chỉ gồm 0 và 1): ")
if all(ky_tu in '01' for ky_tu in nhi_phan):
    thap_phan = int(nhi_phan, 2)  
    print("Giá trị thập phân là:", thap_phan)
else:
    print("Chuỗi không hợp lệ! Vui lòng nhập chỉ gồm 0 và 1.")
