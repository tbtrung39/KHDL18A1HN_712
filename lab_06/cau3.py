lst2 = []
while True:
    num = int(input())
    if num == 0:
        break
    lst2.append(num)

positives = [x for x in lst2 if x > 0]
negatives = [x for x in lst2 if x <= 0]
lst2 = positives + negatives
print("Danh sách sau khi chuyển số dương lên đầu:", lst2)

m = int(input("Nhập số m: "))
if len(lst2) >= 3:
    lst2.insert(2, m)
else:
    lst2.append(m)
print("Danh sách sau khi chèn m:", lst2)