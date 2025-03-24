Str = input("Nhập chuỗi ký tự: ")
dem = 0
for ky_tu in Str:
    if ky_tu.isdigit():
        dem += 1
print("Số lượng ký tự là số trong chuỗi:", dem)
