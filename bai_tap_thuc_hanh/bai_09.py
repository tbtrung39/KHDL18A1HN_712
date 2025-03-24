chuoi = input("Nhập chuỗi ký tự:")
chuoi_con_dai_nhat = ""
do_dai_max= 0
chuoi_hien_tai = chuoi[0]
for i in range(1, len(chuoi)):
    if chuoi[i] == chuoi[i - 1]:
        chuoi_hien_tai += chuoi[i]
    else:
        if len(chuoi_hien_tai) > do_dai_max:
            do_dai_max = len(chuoi_hien_tai)
            chuoi_con_dai_nhat = chuoi_hien_tai
        chuoi_hien_tai = chuoi[i]
if len(chuoi_hien_tai) > do_dai_max:
    chuoi_con_dai_nhat = chuoi_hien_tai
print(f"chuỗi con dài nhất có ký tự giống nhau liên tiếp:\"{chuoi_con_dai_nhat}\"")