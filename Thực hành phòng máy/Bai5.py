Str = input("Nhập chuỗi ký tự: ")
so_str = ""
for ky_tu in Str:
    if ky_tu.isdigit():
        so_str += ky_tu
if so_str == "":
    print("Không có ký tự nào là số trong chuỗi.")
else:
    n = int(so_str)
    # Kiểm tra số hoàn hảo
    tong_uoc = 0
    for i in range(1, n):
        if n % i == 0:
            tong_uoc += i
    print("Chuỗi số sau khi loại bỏ ký tự không phải số là:", so_str)
    if tong_uoc == n:
        print(n, "là số hoàn hảo.")
    else:
        print(n, "không phải là số hoàn hảo.")
