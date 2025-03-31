n = int(input("Nhập số phần tử của danh sách: "))
a = []
for i in range(n):
    a.append(int(input(f"Nhập phần tử thứ {i+1}: ")))
sorted_a = sorted(set(a), reverse=True)
if len(sorted_a) > 1:
    second_largest = sorted_a[1]
    position = a.index(second_largest)
    print("Phần tử lớn thứ hai:", second_largest)
    print("Vị trí của phần tử lớn thứ hai:", position)
else:
    print("Không có phần tử lớn thứ hai.")
max_count = 0
count = 0
for x in a:
    if x > 0:
        count += 1
        max_count = max(max_count, count)
    else:
        count = 0
print("Số lượng số dương liên tiếp nhiều nhất:", max_count)
max_sum = 0
current_sum = 0
for x in a:
    if x > 0:
        current_sum += x
        max_sum = max(max_sum, current_sum)
    else:
        current_sum = 0
print("Tổng lớn nhất của dãy số dương liên tiếp:", max_sum)
