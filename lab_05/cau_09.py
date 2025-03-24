
chuoi = input("Nhập chuỗi ký tự: ")
if not chuoi:
    print("Chuỗi rỗng!")
else:

    max_chuoi = chuoi[0]
    hien_tai = chuoi[0]

    for i in range(1, len(chuoi)):
        if chuoi[i] == hien_tai[-1]:
            hien_tai += chuoi[i]
        else:
            if len(hien_tai) > len(max_chuoi):
                max_chuoi = hien_tai
            hien_tai = chuoi[i]  
    if len(hien_tai) > len(max_chuoi):
        max_chuoi = hien_tai
    print("Chuỗi con dài nhất gồm các ký tự giống nhau liên tiếp là:", max_chuoi)
