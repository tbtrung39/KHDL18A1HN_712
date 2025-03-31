danh_sach = []
while True:
    so = int(input("Nhập số tự nhiên (0 để kết thúc): "))
    if so == 0:
        break
    danh_sach.append(so)
chen_danh_sach = [1, 2, 3]
danh_sach = chen_danh_sach + danh_sach 
danh_sach.extend(chen_danh_sach) 
if len(danh_sach) >= 5:
    danh_sach = danh_sach[:4] + chen_danh_sach + danh_sach[4:]
print("Danh sách sau khi chèn:", danh_sach)
k = int(input("Nhập vị trí phần tử cần xóa (bắt đầu từ 0): "))
if 0 <= k < len(danh_sach):
    danh_sach.pop(k)
    print("Danh sách sau khi xóa phần tử thứ", k, ":", danh_sach)
else:
    print("Vị trí không hợp lệ!")
danh_sach_tang_dan = sorted(danh_sach)
print("Danh sách sắp xếp tăng dần:", danh_sach_tang_dan)
danh_sach_giam_dan = sorted(danh_sach, reverse=True)
print("Danh sách sắp xếp giảm dần:", danh_sach_giam_dan)