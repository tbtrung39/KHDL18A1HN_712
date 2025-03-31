
danh_sach = []
while True:
    n = int(input("Nhập số tự nhiên (0 để kết thúc): "))
    if n == 0:
        break
    danh_sach.append(n)

print("Danh sách ban đầu:", danh_sach)


danh_sach = [1, 2, 3] + danh_sach  
danh_sach.extend([1, 2, 3])  
if len(danh_sach) >= 5:
    danh_sach[4:4] = [1, 2, 3]  

print("Danh sách sau khi chèn:", danh_sach)


k = int(input("Nhập vị trí phần tử cần xóa (bắt đầu từ 1): "))
if 1 <= k <= len(danh_sach):
    danh_sach.pop(k - 1)
else:
    print("Vị trí không hợp lệ!")

print("Danh sách sau khi xóa:", danh_sach)


danh_sach.sort()
print("Danh sách sau khi sắp xếp tăng dần:", danh_sach)


danh_sach.sort(reverse=True)
print("Danh sách sau khi sắp xếp giảm dần:", danh_sach)
