list_numbers = list(iter(lambda: int(input("Nhập số: ")), 0))
list_numbers[:0] = [[1, 2, 3]]
list_numbers.append([1, 2, 3])
list_numbers.insert(5, [1, 2, 3])
k = int(input("Nhập số k: "))
list_numbers.insert(k, k)
print("Danh sách sau khi chèn:", list_numbers)