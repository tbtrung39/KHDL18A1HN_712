# bai 7
data = [["mon", 73], ["tue", 89], ["wed", 95], ["thu", 103], ["fri", 115], ["sat", 128]]

values = [item[1] for item in data]

tong = sum(values)

max_value = max(values)

print("Danh sách giá trị số:", values)
print("Tổng các giá trị số:", tong)
print("Giá trị lớn nhất:", max_value)
