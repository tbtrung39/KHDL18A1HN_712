a = [2, -4, 1, 9, -3, 6, 3, -2, 6, 8]

# 1. Tính tổng các phần tử của danh sách
total_sum = sum(a)
print("Tổng các phần tử trong danh sách:", total_sum)

# 2. Đếm số lượng các số dương và tổng của chúng
positive_numbers = [x for x in a if x > 0]
count_positive = len(positive_numbers)
sum_positive = sum(positive_numbers)
print("Số lượng số dương:", count_positive)
print("Tổng các số dương:", sum_positive)

# 3. Tìm vị trí phần tử âm đầu tiên
first_negative_index = next((i for i, x in enumerate(a) if x < 0), -1)
print("Vị trí phần tử âm đầu tiên:", first_negative_index)

# 4. Tìm vị trí phần tử dương cuối cùng
last_positive_index = next((i for i in range(len(a)-1, -1, -1) if a[i] > 0), -1)
print("Vị trí phần tử dương cuối cùng:", last_positive_index)

# 5. Tìm phần tử lớn nhất và vị trí phần tử lớn nhất cuối cùng
max_value = max(a)
last_max_index = len(a) - 1 - a[::-1].index(max_value)
print("Phần tử lớn nhất:", max_value)
print("Vị trí phần tử lớn nhất cuối cùng:", last_max_index)