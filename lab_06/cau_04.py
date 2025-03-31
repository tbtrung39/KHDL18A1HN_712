danh_sach = []
while True:
    so = int(input("Nhập số tự nhiên (nhập 0 để dừng): "))
    if so == 0:
        break
    danh_sach.append(so)
danh_sach = [1, 2, 3] + danh_sach 
danh_sach.append(1) 
if len(danh_sach) >= 5:
    danh_sach.insert(4, 1) 

print("Danh sách sau khi chèn [1, 2, 3] vào đầu, cuối và vị trí thứ 5:", danh_sach)
k = int(input("Nhập vị trí k để xóa phần tử thứ k (tính từ 0): "))
if 0 <= k < len(danh_sach):
    del danh_sach[k]
    print(f"Danh sách sau khi xóa phần tử thứ {k}: {danh_sach}")
else:
    print("Vị trí không hợp lệ.")
danh_sach_tang = sorted(danh_sach)
danh_sach_giam = sorted(danh_sach, reverse=True)

print("Danh sách sau khi sắp xếp tăng dần:", danh_sach_tang)
print("Danh sách sau khi sắp xếp giảm dần:", danh_sach_giam)
