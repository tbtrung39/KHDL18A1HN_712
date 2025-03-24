binary = input("Nhập chuỗi nhị phân (gồm 0 và 1): ")
if all(c in '01' for c in binary):
    thap_phan = int(binary, 2)
    print("Giá trị thập phân:", thap_phan)
else:
    print("Chuỗi không hợp lệ (phải chỉ gồm 0 và 1).")
