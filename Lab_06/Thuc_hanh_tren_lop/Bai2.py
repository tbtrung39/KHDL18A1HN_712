n = int(input("Nhập số phần tử: "))
a = tuple(int(input(f"Nhập số thứ {i+1}: ")) for i in range(n))

m = max(a)
i_m = a.index(m)
print(f"Số lớn nhất: {m} ở vị trí {i_m}")

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

print(f"Số lượng số dương liên tiếp nhiều nhất: {max_duong}")
print(f"Số lượng số âm liên tiếp nhiều nhất: {max_am}")
