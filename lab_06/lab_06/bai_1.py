# Câu 1
a = [2,-4,1,9,-3,6,3,-2,6,8]
#
tong_cac_phan_tu = sum(a)
print("Tong cac phan tu: ", tong_cac_phan_tu)
#
so_luong_duong = sum(1 for x in a if x > 0)
tong_so_duong = sum(x for x in a if x > 0)
print("So luong cac so duong:", so_luong_duong)
print("Tong cac so duong:", tong_so_duong)
#
vi_tri_am_dau = next((i for i, x in enumerate(a) if x < 0), -1)
print("Vi tri cua phan tu am dau tien:", vi_tri_am_dau)
#
vi_tri_duong_cuoi = next((i for i in range(len(a)-1, -1, -1) if a[i] > 0), -1)
print("Vi tri cua phan tu duong cuoi cung:", vi_tri_duong_cuoi)
#
max_gia_tri = max(a)
vi_tri_max_cuoi = len(a) - 1 - a[::-1].index(max_gia_tri)
print("Phan tu lon nhat:", max_gia_tri)
print("Vi tri phan tu lon nhat cuoi cung:", vi_tri_max_cuoi)