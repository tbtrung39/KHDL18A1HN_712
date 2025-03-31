import random
List_ = [["mon", 73], ["tue", 89], ["wed", 95],  ["thu", 103], ["fri", 115], ["sat", 128], ["sun", 120]]
print("Danh sách gốc:")
for item in List_:
    print(item)

# Lấy phần tử thứ 2 của sublist thứ 3 (index 2)
phan_tu = List_[2][1]
print("Phần tử thứ 2 của sublist thứ 3:", phan_tu)

# Kiểm tra độ dài và thêm sublist ngẫu nhiên
print("Độ dài ban đầu của List_:", len(List_))
List_.append(["new_day", random.randint(50, 150)])
print("Độ dài sau khi thêm:", len(List_))

# Tính tổng doanh số các ngày cụ thể
ngay_can_tinh = ["mon", "tue", "sat", "sun"]
tong = sum(item[1] for item in List_ if item[0] in ngay_can_tinh)
print("Tổng doanh số các ngày được chọn:", tong)