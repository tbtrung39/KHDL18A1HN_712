from random import randint
List_ = [["mon", 73], ["tue", 89], ["wed", 95],  ["thu", 103], ["fri", 115], ["sat", 128], ["sun", 120]]
print("Danh sách gốc:")
for item in List_:
    print(item)

phan_tu = List_[2][1]
print("Phần tử thứ 2 của sublist thứ 3:", phan_tu)

print("Độ dài ban đầu của List_:", len(List_))
List_.append(["new_day", randint(50, 150)])
print("Độ dài sau khi thêm:", len(List_))

ngay = ["mon", "tue", "sat", "sun"]
tong = sum(item[1] for item in List_ if item[0] in ngay)
print("Tổng doanh số các ngày được chọn:", tong)