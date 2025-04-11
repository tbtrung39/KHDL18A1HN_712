str = input("Nhập một chuỗi ký tự : ")
so_luong_so = 0
for ky_tu in str:
    if ky_tu.isdigit():
        so_luong_so +=1
print("Số ký tự là số trong chuỗi là :",so_luong_so)