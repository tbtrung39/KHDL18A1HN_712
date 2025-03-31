n = int(input("Nhập số phần tử của danh sách: "))
arr = list(map(int, input("Nhập các phần tử cách nhau bởi dấu cách: ").split()))

if len(arr) != n:
    print("Số phần tử nhập vào không đúng!")
else:
    unique_arr = list(set(arr))  
    if len(unique_arr) < 2:
        print("Không có phần tử lớn thứ hai.")
    else:
        unique_arr.sort(reverse=True)
        second_largest_value = unique_arr[1]
        positions = [i for i in range(len(arr)) if arr[i] == second_largest_value]
        print(f"Phần tử lớn thứ hai là {second_largest_value}, xuất hiện tại vị trí {positions}")
    
    max_count = 0
    count = 0
    for num in arr:
        if num > 0:
            count += 1
            if count > max_count:
                max_count = count
        else:
            count = 0
    print(f"Số lượng số dương liên tiếp nhiều nhất: {max_count}")
    
   
    max_sum = 0
    cur_sum = 0
    for num in arr:
        if num > 0:
            cur_sum += num
            if cur_sum > max_sum:
                max_sum = cur_sum
        else:
            cur_sum = 0
    print(f"Tổng lớn nhất của các số dương liên tiếp: {max_sum}")