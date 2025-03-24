Str = input("Nhập chuỗi nhị phân: ")
hop_le = True
for ky_tu in Str:
    if ky_tu != '0' and ky_tu != '1':
        hop_le = False
        break
if not hop_le:
    print("Chuỗi không hợp lệ! Chỉ được chứa 0 và 1.")
else:
    thap_phan = 0
    luy_thua = 1  # 2^0 = 1
    for i in range(len(Str) - 1, -1, -1):
        if Str[i] == '1':
            thap_phan += luy_thua
        luy_thua *= 2
    print("Giá trị thập phân là:", thap_phan)
