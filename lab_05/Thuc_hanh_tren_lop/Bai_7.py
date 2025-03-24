#Trùng bài 5
s = input("Nhập chuỗi ký tự: ")
a = ""
for c in s:
    if c.isdigit():
        a += c

if a == "":
    print("Chuỗi không chứa số hợp lệ.")
else:
    number = int(a)
    tong = 0
    for i in range(1, number):
        if number % i == 0:
            tong += i
    if tong == number:
        print(f"{number} là số hoàn hảo.")
    else:
        print(f"{number} không phải là số hoàn hảo.")