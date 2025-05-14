n = int(input("Nhập số lượng phần tử n: "))
a = []

for i in range(n):
    x = int(input(f"Nhập phần tử thứ {i+1}: "))
    a.append(x)

max1 = max2 = float('-inf')
for x in a:
    if x > max1:
        max2 = max1
        max1 = x
    elif x > max2 and x != max1:
        max2 = x

pos2 = -1
for i in range(len(a)):
    if a[i] == max2:
        pos2 = i
        break
print("Vị trí phần tử lớn thứ hai:", pos2)

max_len = cur_len = 0
for x in a:
    if x > 0:
        cur_len += 1
        if cur_len > max_len:
            max_len = cur_len
    else:
        cur_len = 0
print("Độ dài dãy số dương liên tiếp dài nhất:", max_len)

max_sum = cur_sum = 0
for x in a:
    if x > 0:
        cur_sum += x
        if cur_sum > max_sum:
            max_sum = cur_sum
    else:
        cur_sum = 0
print("Tổng dãy số dương liên tiếp lớn nhất:", max_sum)
