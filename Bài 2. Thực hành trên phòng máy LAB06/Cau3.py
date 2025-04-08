# Câu 3
#
lst = []
while True:
    gia_tri = int(input("Nhap mot so tu nhien (nhap 0 de dung): "))
    if gia_tri == 0:
        break
    lst.append(gia_tri)
phan_tu_duong = [x for x in lst if x > 0]
phan_tu_khac = [x for x in lst if x <= 0]
danh_sach_moi = phan_tu_duong + phan_tu_khac
print("Danh sach sau khi chuyen cac phan tu duong len dau:", danh_sach_moi)
#
m = int(input("Nhap mot so m: "))
danh_sach_moi.insert(0, m)
danh_sach_moi.append(m)
if len(danh_sach_moi) >= 5:
    danh_sach_moi.insert(4, m) 
print("Danh sach sau khi chen m vao:", danh_sach_moi)