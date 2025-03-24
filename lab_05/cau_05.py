chuoi = input("Nhập chuỗi ký tự: ")
so_str = ""
for ky_tu in chuoi:
    if '0' <= ky_tu <= '9':
        so_str += ky_tu
if so_str == "":
    print("Không có ký tự nào là số trong chuỗi!")
else:
    so_nguyen = int(so_str)
    print("Chuỗi sau khi lọc chỉ chứa số là:", so_str)
    tong_uoc = 0
    for i in range(1, so_nguyen):
        if so_nguyen % i == 0:
            tong_uoc += i

    if tong_uoc == so_nguyen:
        print(f"{so_nguyen} là số hoàn hảo.")
    else:
        print(f"{so_nguyen} không phải là số hoàn hảo.")
