a = list(map(int, input("Nhập các số tự nhiên cách nhau bởi dấu cách: ").split()))
max1 = max(a)
index_max1 = a.index(max1)
a_temp = a.copy()
a_temp.remove(max1)
max2 = max(a_temp)
index_max2 = a.index(max2)

print(f"Phần tử lớn nhất: {max1}, vị trí: {index_max1}")
print(f"Phần tử lớn thứ hai: {max2}, vị trí: {index_max2}")

max_count = count = 0
for num in a:
    if num > 0:
        count += 1
        max_count = max(max_count, count)
    else:
        count = 0
print(f"Số lượng số dương liên tiếp nhiều nhất: {max_count}")

max_sum = temp_sum = 0
current_count = max_sum_count = 0

for num in a:
    if num > 0:
        temp_sum += num
        current_count += 1
        if temp_sum > max_sum:
            max_sum = temp_sum
            max_sum_count = current_count
    else:
        temp_sum = 0
        current_count = 0

print(f"Số lượng số dương liên tiếp có tổng lớn nhất: {max_sum_count} (Tổng: {max_sum})")
