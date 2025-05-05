# 1. Tạo danh sách và in từng phần tử
List_ = [["mon", 73], ["tue", 89], ["'wed", 95], ["thu", 103], ["fri", 115], ["sat", 128], ["sun", 120]]

print("Các phần tử trong List_:")
for item in List_:
    print(item)

# 2. Lấy phần tử thứ hai, thuộc vị trí thứ 3 của sublist
# (sublist thứ 3 là: ["'wed", 95] => phần tử thứ hai là 95)
pt_thu_2 = List_[2][1]
print("\nPhần tử thứ hai, thuộc sublist thứ 3 là:", pt_thu_2)

# 3. Kiểm tra độ dài list test và thêm 1 sublist ngẫu nhiên
test = List_.copy()  # Tạo bản sao để thao tác

print("\nĐộ dài ban đầu của list test:", len(test))

# Thêm một sublist ngẫu nhiên, ví dụ ["random", 111]
test.append(["random", 111])

print("Độ dài sau khi thêm sublist:", len(test))
print("Sublist mới được thêm:", test[-1])

# 4. Tính tổng sale value của các ngày: mon, tue, sat, sun
# Tạo dict để dễ truy xuất
sale_dict = dict(List_)

# Do 'wed' bị ghi sai (có dấu nháy đơn), cần chú ý.
tong_sale = sale_dict["mon"] + sale_dict["tue"] + sale_dict["sat"] + sale_dict["sun"]
print("\nTổng sale value của các ngày thứ hai, ba, bảy, chủ nhật là:", tong_sale)