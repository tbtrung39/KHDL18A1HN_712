chuoi = input("Nhập chuỗi: ")

so_luong_so = 0

for ky_tu in chuoi:
    if '0' <= ky_tu <= '9': 
        so_luong_so += 1

print("Số ký tự là số:", so_luong_so)
