# Bai 2
n = int(input("Nhập số phần tử của danh sách: "))

lst = list(map(int, input("Nhập danh sách các số tự nhiên, cách nhau bởi dấu cách: ").split()))

# Kiểm tra nếu danh sách có ít nhất 2 phần tử
if len(lst) < 2:
    print("Danh sách phải có ít nhất 2 phần tử để tìm phần tử lớn thứ hai.")
else:
    # 1. Tìm phần tử lớn thứ hai và vị trí của nó
    unique_lst = list(set(lst)) 
    unique_lst.sort(reverse=True)  

    if len(unique_lst) >= 2:
        second_largest = unique_lst[1]
        index_second_largest = lst.index(second_largest)
        print("Phần tử lớn thứ hai:", second_largest)
        print("Vị trí của phần tử lớn thứ hai:", index_second_largest)
    else:
        print("Không có phần tử lớn thứ hai trong danh sách.")

# 2. Tính số lượng số dương liên tiếp nhiều nhất
max_count = 0
current_count = 0

for num in lst:
    if num > 0:
        current_count += 1
        max_count = max(max_count, current_count)
    else:
        current_count = 0

print("Số lượng số dương liên tiếp nhiều nhất:", max_count)

# 3. Tính số lượng số dương liên tiếp có tổng lớn nhất
max_sum = 0
current_sum = 0
current_count = 0
max_count_sum = 0 

for num in lst:
    if num > 0:
        current_sum += num
        current_count += 1
        if current_sum > max_sum:
            max_sum = current_sum
            max_count_sum = current_count
