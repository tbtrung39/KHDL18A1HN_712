str = input("Nhập một chuỗi ký tự : ")
dem_ky_tu_khac = 0
for ky_tu in str:
    if not ky_tu.isdigit():
        dem_ky_tu_khac +=1
print("Số ký tự không phải chữ cái tiếng anh và không phải số là :",dem_ky_tu_khac)