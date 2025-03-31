n = int(input("Nhập số phần tử của danh sách: "))
lst = []
for _ in range(n):
    lst.append(int(input()))

# a) Tìm phần tử lớn thứ hai và vị trí của nó
max1, max2 = float('-inf'), float('-inf')
pos_max2 = -1
for i in range(n):
    if lst[i] > max1:
        max2, max1 = max1, lst[i]
        pos_max2 = i if max2 != float('-inf') else -1
    elif lst[i] > max2 and lst[i] < max1:
        max2, pos_max2 = lst[i], i
print("Phần tử lớn thứ hai:", max2, "vị trí:", pos_max2)

# b) Tính số lượng số có đúng 3 chữ số
count_3_digit = sum(1 for x in lst if 100 <= x <= 999)
print("Số lượng số có đúng 3 chữ số:", count_3_digit)

# c) Tìm số lượng số dương liên tiếp có tổng lớn nhất
max_sum = 0
current_sum = 0
for x in lst:
    if x > 0:
        current_sum += x
    else:
        max_sum = max(max_sum, current_sum)
        current_sum = 0
max_sum = max(max_sum, current_sum)
print("Tổng lớn nhất của các số dương liên tiếp:", max_sum)