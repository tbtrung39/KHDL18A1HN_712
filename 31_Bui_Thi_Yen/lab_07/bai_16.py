# Cau 16.
danh_sach_so = list(map(int, input("Nhap day so, cach nhau boi dau cach: ").split()))
n = len(danh_sach_so)
dem = 0
cap = []

for i in range(n):
    for j in range(i + 1, n):
        if i + j < n and danh_sach_so[i] + danh_sach_so[j] == danh_sach_so[i + j]:
            dem += 1
            cap.append((i, j))

print("Tong so cap thoa dieu kien:", dem)
print("Cac cap:", cap)