str = input("Nhập chuỗi ký tự: ")
so = ""
for c in str:
    if c.isdigit():
        so += c
print("Chuỗi chỉ gồm các chữ số là:", so)

if so != "":
    n = int(so)
    tong = 0
    for i in range(1, n):
        if n % i == 0:
            tong += i
    if tong == n:
        print(n, "là số hoàn hảo.")
    else:
        print(n, "không phải là số hoàn hảo.")
