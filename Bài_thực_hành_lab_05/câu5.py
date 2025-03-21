chuoi = input("Nhập chuỗi ký tự: ")

# Lọc ra các ký tự là số
chuoi_so = "".join(ky_tu for ky_tu in chuoi if ky_tu.isdigit())

if chuoi_so:
    so = int(chuoi_so)
    
    # Kiểm tra số hoàn hảo
    tong_uoc = sum(i for i in range(1, so) if so % i == 0)
    
    print("Chuỗi số:", chuoi_so)
    if tong_uoc == so:
        print("Đây là số hoàn hảo!")
    else:
        print("Không phải số hoàn hảo!")
else:
    print("Không có số nào trong chuỗi!")
