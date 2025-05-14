n = int(input("Nhập số phần tử: "))
a = tuple(int(input(f"Nhập số thứ {i+1}: ")) for i in range(n))

a = sorted(set(a), reverse=True)  
if len(a) >= 2:
    sl = a[1]
    slp = a.index(sl)
else:
    sl = None
    slp = None

max_duong = max_am = dem_duong = dem_am = 0
for x in a:
    if x > 0:
        dem_duong += 1
        max_duong = max(max_duong, dem_duong)
        dem_am = 0 
    elif x < 0:
        dem_am += 1
        max_am = max(max_am, dem_am)
        dem_duong = 0  
    else:
        dem_duong = dem_am = 0 

print("\nKết quả:")
if sl is not None:
    print(f"Phần tử lớn thứ hai trong danh sách là {sl} và vị trí của nó là {slp}.")
else:
    print("Không có phần tử lớn thứ hai trong danh sách.")

print(f"Số lượng số dương liên tiếp nhiều nhất: {max_duong}")
print(f"Số lượng số âm liên tiếp nhiều nhất: {max_am}")