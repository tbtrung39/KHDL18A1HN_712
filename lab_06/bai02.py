n = int(input("Nhập số phần tử: "))
a = tuple(int(input(f"Nhập số thứ {i+1}: ")) for i in range(n))

a = sorted(set(a), reverse=True)  
if len(a) >= 2:
    second_largest = a[1]
    second_largest_position = a.index(second_largest)
else:
    second_largest = None
    second_largest_position = None

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
if second_largest is not None:
    print(f"Phần tử lớn thứ hai trong danh sách là {second_largest} và vị trí của nó là {second_largest_position}.")
else:
    print("Không có phần tử lớn thứ hai trong danh sách.")

print(f"Số lượng số dương liên tiếp nhiều nhất: {max_duong}")
print(f"Số lượng số âm liên tiếp nhiều nhất: {max_am}")