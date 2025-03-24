Str = input("Nhập chuỗi ký tự: ")

so = ""
for c in Str:
    if c.isdigit():
        so += c

print("Chuỗi số sau khi loại bỏ ký tự không phải số là:", so)

if so != "":
    n = int(so)
    tong_uoc = 0
    for i in range(1, n):
        if n % i == 0:
            tong_uoc += i

    if tong_uoc == n:
        print(n, "là số hoàn hảo.")
    else:
        print(n, "không phải là số hoàn hảo.")
else:
    print("Không có chữ số nào trong chuỗi.")
