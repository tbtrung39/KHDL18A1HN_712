# Câu 2
n = int(input("Nhap so phan tu n: "))
lst = []
for i in range(n):
    num = int(input("Nhap phan tu thu " + str(i + 1) + ": "))
    lst.append(num)
gia_tri_lon_nhat = max(lst)
danh_sach_loc = [x for x in lst if x != gia_tri_lon_nhat]
if danh_sach_loc:
    gia_tri_lon_nhi = max(danh_sach_loc)
    vi_tri = lst.index(gia_tri_lon_nhi)
    print("Phan tu lon thu hai la " + str(gia_tri_lon_nhi) + ", o vi tri " + str(vi_tri))
else:
    print("Khong co phan tu lon thu hai")
#
so_duong_hien_tai = 0
for gia_tri in lst:
    if gia_tri > 0:
        so_duong_hien_tai += 1
        max_so_duong = max(max_so_duong, so_duong_hien_tai)
    else:
        so_duong_hien_tai = 0
print("So luong so duong lien tiep nhieu nhat la:", max_so_duong)
#
tong_max = 0
tong_hien_tai = 0
for so in lst:
    if so > 0:
        tong_hien_tai += so
        if tong_hien_tai > tong_max:
            tong_max = tong_hien_tai
    else:
        tong_hien_tai = 0
print("Tong lon nhat cua cac so duong lien tiep la:", tong_max)