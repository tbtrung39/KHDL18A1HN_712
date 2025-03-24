Str = input("Nhập đoạn văn bản: ")
tu_can_tim = input("Nhập từ cần tìm: ")
tu = ""
dem = 0
Str += " "
for ky_tu in Str:
    if ky_tu != " " and ky_tu != "\n":
        tu += ky_tu
    else:
        if tu == tu_can_tim:
            dem += 1
        tu = ""
print("Số lần xuất hiện của từ", '"' + tu_can_tim + '"', "là:", dem)
