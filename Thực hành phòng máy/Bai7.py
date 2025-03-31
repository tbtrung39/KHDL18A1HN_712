List = [["mon", 73], ["tue", 89], ["wed", 95], ["thu", 103], ["fri", 115], ["sat", 128], ["sun", 120]]
print("Danh sách List ban đầu:", List)
phantu_2 = List[1]
phantu_3 = List[2]
print("\nPhần tử thứ hai:", phantu_2)
print("Phần tử thứ ba:", phantu_3)
test = [10, 20, 30, "abc", 40, "xyz"]
for item in test:
    if isinstance(item, int):
        List.append(["extra", item])
print("\nDanh sách sau khi kiểm tra test và thêm sublist nếu có số nguyên:", List)
tong_sale = List[1][1] + List[2][1] + List[5][1] + List[6][1]
print("\nTổng sale value của các ngày thứ hai, thứ ba, thứ bảy và chủ nhật:", tong_sale)
